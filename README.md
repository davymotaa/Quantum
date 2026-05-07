# QuantumAI

Workspace de continuidade e orquestracao do projeto **QUANTUM**.

## Estrutura

- `01_contexto/`: contexto local do Oraculo, incluindo canone, personagens, estado atual e padrao de escrita.
- `02_capitulos/`: espaco local para capitulos ou materiais exportados.
- `oraculo/`: mapa dos documentos do Drive, fluxo operacional e prompts de apoio.

## Segredos

Use `.env.example` como modelo para criar um `.env` local.

O arquivo `.env` real fica fora do Git por regra do `.gitignore`. Nao versionar chaves de API, tokens ou credenciais.

## Fluxo principal

- `adicionar a historia ao capitulo`: inserir texto aprovado/rascunho no fim do capitulo correspondente no documento final.
- `finalizar o capitulo X`: ler a versao final editada pelo autor, comparar com rascunho, extrair aprendizado editorial, atualizar Oraculo e changelogs.

## Executor local

Use `oraculo/run_oraculo.py` para chamar a OpenAI API ou o LM Studio/Sultry usando o `.env` local.

Exemplos:

```bash
python3 oraculo/run_oraculo.py brainstorm "ideias para o Capitulo III"
python3 oraculo/run_oraculo.py cena-sultry "editar a cena adulta aprovada" --provider lmstudio
python3 oraculo/run_oraculo.py brainstorm "estrutura do Capitulo III" --output 02_capitulos/cap_iii_estrutura.md
```

## Documentos principais

O mapa completo de documentos do Google Drive fica em `oraculo/docs.json`.

## Novo chat

Para continuar em outro chat, use `HANDOFF.md`. Ele contem o bloco de contexto operacional que deve ser colado no chat novo.
