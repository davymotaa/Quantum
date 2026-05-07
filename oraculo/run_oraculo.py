#!/usr/bin/env python3
"""Executor local do Oraculo.

Le arquivos de contexto, monta um prompt e chama OpenAI API ou LM Studio.
Nao imprime chaves nem grava segredos.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTEXT_FILES = [
    ROOT / "01_contexto" / "estado_atual.md",
    ROOT / "01_contexto" / "canone.md",
    ROOT / "01_contexto" / "personagens.md",
    ROOT / "01_contexto" / "padrao_escrita.md",
]
PROMPTS = {
    "brainstorm": ROOT / "oraculo" / "prompts" / "brainstorm.md",
    "revisao-canone": ROOT / "oraculo" / "prompts" / "revisao_canone.md",
    "changelog": ROOT / "oraculo" / "prompts" / "changelog.md",
    "cena-sultry": ROOT / "oraculo" / "prompts" / "cena_sultry.md",
}


def load_env(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_prompt(task: str, user_request: str, extra_file: Path | None) -> str:
    prompt_path = PROMPTS[task]
    parts = [
        "# INSTRUCOES DA TAREFA",
        read_text(prompt_path),
        "# CONTEXTO DO ORACULO",
    ]
    for context_file in CONTEXT_FILES:
        parts.append(f"## {context_file.relative_to(ROOT)}")
        parts.append(read_text(context_file))
    if extra_file:
        parts.append(f"# MATERIAL EXTRA — {extra_file}")
        parts.append(read_text(extra_file))
    parts.append("# PEDIDO DO AUTOR")
    parts.append(user_request)
    return "\n\n".join(parts)


def post_json(url: str, headers: dict[str, str], payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Falha de conexao: {exc.reason}") from exc


def call_openai(prompt: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY nao encontrada no .env ou ambiente.")
    model = os.environ.get("OPENAI_MODEL", "gpt-5.4-mini")
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Voce e o Oraculo de QUANTUM. Responda em portugues e siga estritamente o contexto fornecido.",
            },
            {"role": "user", "content": prompt},
        ],
    }
    response = post_json(
        "https://api.openai.com/v1/chat/completions",
        {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        payload,
    )
    return response["choices"][0]["message"]["content"]


def call_lmstudio(prompt: str) -> str:
    base_url = os.environ.get("LMSTUDIO_URL", "http://localhost:1234/v1").rstrip("/")
    model = os.environ.get("LMSTUDIO_MODEL", "sultrysilicon-7b-v2")
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Voce e o escritor/editor Sultry Silicon para QUANTUM. Entregue apenas a cena ou edicao solicitada.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.8,
    }
    response = post_json(
        f"{base_url}/chat/completions",
        {"Content-Type": "application/json"},
        payload,
    )
    return response["choices"][0]["message"]["content"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Executa tarefas do Oraculo via OpenAI API ou LM Studio.")
    parser.add_argument("task", choices=sorted(PROMPTS))
    parser.add_argument("request", help="Pedido do autor entre aspas.")
    parser.add_argument("--extra-file", type=Path, help="Arquivo extra para incluir no prompt.")
    parser.add_argument("--output", type=Path, help="Arquivo de saida para salvar a resposta.")
    parser.add_argument("--provider", choices=["auto", "openai", "lmstudio"], default="auto")
    args = parser.parse_args()

    load_env(ROOT / ".env")

    provider = args.provider
    if provider == "auto":
        provider = "lmstudio" if args.task == "cena-sultry" else "openai"

    prompt = build_prompt(args.task, args.request, args.extra_file)
    result = call_lmstudio(prompt) if provider == "lmstudio" else call_openai(prompt)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
        print(f"Resposta salva em {args.output}")
    else:
        print(result)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        raise SystemExit(1)
