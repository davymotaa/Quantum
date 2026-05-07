# QUANTUM — Fluxo do Oraculo

Este arquivo define o processo basico para usar o Oraculo durante a escrita.

## Quando o autor disser "use o Oraculo"

1. Ler `oraculo/docs.json` para localizar os documentos certos.
2. Consultar no Drive:
   - regras de orquestracao;
   - canone atual;
   - personagens atual;
   - padrao de escrita;
   - estado atual.
3. Entender o pedido do autor: brainstorm, cena, capitulo, revisao, continuidade ou subida para Docs.
4. Alinhar com o autor antes de gerar texto final:
   - funcao da parte;
   - personagens em foco;
   - onde comeca;
   - onde termina;
   - tom emocional;
   - possiveis impactos de canone.
5. Escolher o modelo pela regra de roteamento.
6. Criar ou usar um documento temporario de rascunho quando a parte for longa.
7. Executar a etapa em uma ou mais requisicoes, se necessario.
8. Rodar uma etapa de editor antes do texto final:
   - continuidade;
   - canone;
   - ritmo;
   - dialogos;
   - excesso de bate-bola;
   - tom;
   - idioma;
   - estilo fisico/sensorial.
   - motivacao de decisoes importantes (nomes, escolhas, viradas emocionais);
   - se conclusoes nasceram em cena ou apareceram como tese pronta.
9. Montar o texto final no documento temporario.
10. Trazer o resultado para aprovacao quando for texto criativo.
11. Inserir no documento final apenas quando o autor aprovar ou pedir explicitamente.
12. Se o autor editar diretamente no documento final, ler a versao editada antes de continuar. Tratar a edicao do autor como fonte preferencial de:
   - ritmo;
   - nivel de dialogo;
   - formatacao;
   - tom de humor;
   - modo como decisoes importantes devem nascer em cena.
13. Ao finalizar cena/capitulo, verificar impacto em:
   - canone;
   - personagens;
   - estilo;
   - estado atual;
   - changelog geral.
14. Atualizar arquivos principais se houver mudanca real.
15. Registrar a origem e o motivo da mudanca no changelog correspondente.

## Roteamento simples

| Tarefa | Modelo/ferramenta preferida |
| --- | --- |
| Brainstorm geral | OpenAI/API |
| Estrutura de capitulo | OpenAI/API |
| Continuidade e analise de arco | OpenAI/API |
| Cena quente/adulta | Sultry Silicon via LM Studio |
| Edicao de cena criada pelo Sultry | Sultry Silicon via LM Studio |
| Checagem de canone | Codex + documentos do Oraculo |
| Insercao no Google Docs | Codex + Google Drive |
| Changelog | Codex + Google Drive |

## Regra de cenas adultas

Cenas sexuais ou explicitamente sensuais so podem envolver personagens adultos. Personagens menores de idade nunca entram nesse modo.

## Tamanho minimo das partes

Cada parte de capitulo deve mirar pelo menos 4000 palavras, salvo pedido contrario do autor. Se uma unica requisicao nao comportar a parte inteira, dividir em blocos com continuidade clara e depois montar o texto final no documento temporario.

## Regra de dialogos

Dialogo nao deve virar pingue-pongue automatico. O padrao e fala com corpo, intencao, gesto, silencio, reacao ou consequencia. Bate-bola curto so deve aparecer como recurso pontual de humor, tensao ou ritmo.

Quando o autor pedir "igual a parte anterior", comparar com a parte imediatamente anterior no documento final, nao com o rascunho local. Dialogos devem usar travessao, falas isoladas quando forem curtas e narracao entre falas quando o peso emocional pedir.

## Regra de decisoes e nomes

Nomes heroicos, viradas emocionais e decisoes importantes nao podem aparecer do nada. Antes de afirmar uma escolha, construir:

- friccao externa;
- memoria ou sensacao corporal;
- conversa com outro personagem;
- humor ou reacao concreta;
- consequencia pratica.

Exemplos atuais:

- `Quantum` nasce de apelidos ruins, humor publico, conversa com Peter e Mateus percebendo que precisa escolher o proprio contorno.
- `Aero` deve nascer do controle de ar de Toro como respiracao, passagem, pressao, casa, liberdade e precisao; `Skyward` e uma possibilidade bonita, mas externa demais.

## Documentos temporarios

Texto criativo longo deve ser trabalhado primeiro em documento temporario. O documento final do volume so recebe texto depois de aprovacao do autor.

## Regra de autoria operacional

Quando a cena for gerada pelo Sultry e o pedido for preservar a voz dele, Codex nao reescreve a cena como autor. Codex pode organizar, copiar, colar, pedir nova edicao ao Sultry e atualizar documentos.

## Registro de mudancas

Toda mudanca canonica deve responder:

- O que mudou?
- Em qual volume/capitulo/cena a mudanca nasceu?
- Por que mudou?
- Qual arquivo principal foi alterado?
- Qual impacto isso tem para capitulos futuros?

## Documento final atual

O destino padrao para texto aprovado do Volume IV e:

https://docs.google.com/document/d/1-BwgZEy83W_B8OvziGCMvwLpI2CdQ99m6ZjyEVvaqbo

## Comando operacional: finalizar capitulo

Quando o autor disser `finalizar o capitulo X`, Codex deve tratar isso como rotina de fechamento editorial e canonico.

Etapas obrigatorias:

1. Ler o capitulo X no documento final do volume. A versao final editada pelo autor e fonte soberana.
2. Ler o rascunho correspondente, quando existir, e comparar com o texto final.
3. Identificar o que mudou nas edicoes do autor: cortes, acrescimos, ritmo, dialogo, tom, nivel de explicacao, construcao emocional, cenas adicionadas/removidas e escolhas de continuidade.
4. Extrair aprendizado editorial para a IA, mesmo quando nao houver mudanca de canone. O aprendizado deve ensinar como escrever melhor os proximos capitulos, nao apenas registrar fatos.
5. Atualizar `Estado Atual`, `Canone Atual`, `Personagens Atual` e `Padrao de Escrita` apenas quando houver mudanca real.
6. Registrar as mudancas nos changelogs correspondentes e no changelog geral quando a atualizacao for transversal.
7. Considerar o capitulo fechado para continuidade futura.

Comando relacionado: quando o autor pedir `adicionar a historia ao capitulo`, Codex deve inserir o texto aprovado/rascunho no fim do capitulo correspondente no documento final, para leitura e edicao do autor. A finalizacao so acontece depois que o autor disser explicitamente `finalizar o capitulo X`.
