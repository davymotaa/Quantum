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

## Documentos principais

O mapa completo de documentos do Google Drive fica em `oraculo/docs.json`.
