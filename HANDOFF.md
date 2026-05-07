# HANDOFF — QUANTUM / QuantumAI

Cole este bloco em qualquer chat novo do Codex para retomar o projeto sem reexplicar tudo.

---

Voce esta trabalhando no projeto **QUANTUM**, usando o repo:

https://github.com/davymotaa/Quantum

## Regra de seguranca

- Nao usar nenhuma API key que tenha aparecido em conversa anterior.
- Nunca imprimir, copiar ou commitar `.env`.
- Se precisar de chave, pedir por forma segura.
- `.env` fica local e ignorado pelo Git; `.env.example` e apenas modelo.

## Primeira acao no chat novo

1. Clonar/abrir o repo `davymotaa/Quantum`.
2. Ler, nesta ordem:
   - `README.md`
   - `oraculo/fluxo.md`
   - `oraculo/docs.json`
   - `01_contexto/estado_atual.md`
   - `01_contexto/canone.md`
   - `01_contexto/personagens.md`
   - `01_contexto/padrao_escrita.md`
3. Se for usar Google Docs/Drive, garantir que o conector Google Drive/Docs esteja autorizado no ambiente.

## Documentos principais

- Pasta do Drive / Oraculo: https://drive.google.com/drive/folders/1aTb8aUDZGGJ2y4qdVYsT2NcToDv4aiZN
- Documento final Volume IV: https://docs.google.com/document/d/1-BwgZEy83W_B8OvziGCMvwLpI2CdQ99m6ZjyEVvaqbo
- Rascunho Capitulo II: https://docs.google.com/document/d/1nPGSu0wanIWFA1gp6Kk7y45wILZX7XwJtinhocIRmes

O mapa completo esta em `oraculo/docs.json`.

## Fluxo combinado

- OpenAI/API: brainstorm, estrutura, continuidade, revisao geral, capitulos normais.
- LM Studio / Sultry Silicon: cenas adultas/quentes ou quando o autor pedir preservar aquela voz.
- Codex: orquestra, le contexto, chama o executor local quando necessario, edita/substitui/insere no Google Docs, atualiza Oraculo, changelog e Git.

Executor local:

```bash
python3 oraculo/run_oraculo.py brainstorm "pedido do autor"
python3 oraculo/run_oraculo.py cena-sultry "pedido do autor"
python3 oraculo/run_oraculo.py brainstorm "pedido do autor" --output 02_capitulos/saida.md
```

## Comandos operacionais do autor

### "adicionar a historia ao capitulo"

Inserir texto aprovado/rascunho no fim do capitulo correspondente no documento final do Volume IV. O autor vai ler e editar no documento final.

### "finalizar o capitulo X"

Rotina obrigatoria:

1. Ler o capitulo X no documento final. A versao editada pelo autor e soberana.
2. Ler o rascunho correspondente, se existir.
3. Comparar rascunho vs. final.
4. Extrair aprendizado editorial das edicoes do autor.
5. Atualizar, se houver mudanca real:
   - Estado Atual
   - Canone Atual
   - Personagens Atual
   - Padrao de Escrita
   - Regras de Orquestracao, se o fluxo mudou
6. Atualizar changelogs correspondentes e changelog geral quando for transversal.
7. Atualizar arquivos locais do repo, commitar e subir para GitHub.

## Estado atual canonico

- Volume I, II e III concluidos.
- Volume IV em andamento.
- Capitulo I concluido.
- Capitulo II, `Ar Mais Leve`, finalizado.
- Proximo trabalho provavel: Capitulo III ou consequencias do Capitulo II.

Resumo do Cap II:

- `Quantum` ja e usado operacionalmente em campo por Sam/SWORD.
- Mateus ainda assimila internamente o nome.
- Mateus atua no Mar de Java em desastre publico e sai quando deixa a missao estavel para Sam.
- Mateus ouve passivamente Toro chamando do outro lado do planeta durante crise medica da mae.
- A mae de Toro tem instabilidade ligada ao fio residual/Camada Cinco.
- Toro chama Mateus como pai e depois verifica se ele esta respirando quando dorme profundamente.
- Jasper ajusta alertas para a mae de Toro e fica com Toro em silencio; o vinculo Toro/Jasper avanca com pudor.
- Fury/SWORD discutem possiveis jovens com poderes, incluindo Erik Svanberg e Aminata Diop.
- Regra atual: sem time jovem, sem campo, sem introducoes surpresa, com estabilidade medica, estabilidade de Mateus e consentimento em cada etapa.

## Regras de estilo essenciais

- Narracao em portugues.
- Dialogos com anglofonos em ingles.
- Mateus nao fala portugues com Peter/outros anglofonos, exceto ensino.
- Peter so usa portugues em palavras soltas com sotaque errado.
- Shuri sempre fala ingles.
- Mateus e poderoso demais para obstaculos fisicos simples; conflito vem de consequencia, nao incapacidade.
- Poder de Mateus deve ser narrado por efeito, reacao e ausencia de esforco.
- Nomes heroicos e viradas emocionais nascem em cena, nao como tese pronta.
- Cenas adolescentes Toro/Jasper devem preservar pudor, presenca e silencio.
- Cenas adultas/quentes so com adultos, nunca envolvendo menores.

## Ao terminar qualquer trabalho

- Atualizar Drive se necessario.
- Atualizar arquivos locais se necessario.
- Rodar Git:

```bash
git status
git add .
git commit -m "mensagem objetiva"
git push
```

Se o push pedir chave SSH, usar a chave local ja criada no Mac:

```bash
GIT_SSH_COMMAND='ssh -i /Users/davy/.ssh/id_ed25519_quantum_github -o IdentitiesOnly=yes' git push
```
