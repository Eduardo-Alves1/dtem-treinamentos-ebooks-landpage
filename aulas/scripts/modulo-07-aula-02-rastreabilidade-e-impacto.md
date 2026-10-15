# Script do Professor — Rastreabilidade e Análise de Impacto

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar uma aula paralela.

**Roteiro:** [Módulo 7, Aula 2](../modulo-07-aula-02-rastreabilidade-e-impacto.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-07-ciclo-de-vida-do-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Ensinar rastreabilidade como conexão verificável entre necessidade, regra, história, teste, defeito e versão, usando esses vínculos para avaliar impacto de mudanças.
- **Demonstração central:** Montar cadeia e analisar uma mudança.
- **Prática em grupo:** Seguir a mudança.
- **Exercício individual:** analisar impacto de H12.
- **Tarefa:** revisar matriz e uma análise de impacto.

## Antes da aula

- [ ] Separar RN03, TC03, BUG01 e versões.
- [ ] Preparar matriz vazia.
- [ ] Escolher mudança simples de catálogo.
- [ ] Deixar roteiro e script abertos.
- [ ] Conferir materiais, dados e exemplos.
- [ ] Separar a entrega esperada da aula.

## Agenda

| Intervalo | Etapa |
|---|---|
| 00–08 | Abertura e diagnóstico |
| 08–25 | Conceitos e exemplos |
| 25–45 | Demonstração guiada |
| 45–50 | Pausa |
| 50–65 | Dinâmica |
| 65–77 | Exercício individual |
| 77–85 | Correção e dúvidas |
| 85–90 | Fechamento e tarefa |

## 00–08 — Abertura e diagnóstico

> Quando uma regra muda, como saber o que precisa ser revisto sem depender da memória de alguém? Hoje vamos construir vínculos que permitam responder isso.

**Pergunta diagnóstica:** Se RN03 mudar, um caso antigo aprovado ainda prova a regra nova?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** Não necessariamente; é preciso analisar se o caso cobre a nova condição e em qual versão foi executado.

**Transição:**

> Vamos construir primeiro a cadeia atual e depois alterar uma premissa para observar os efeitos.

## 08–25 — Conceitos e exemplos

### 1. Rastreabilidade

**Fala sugerida:**

> Rastreabilidade responde de onde veio uma decisão e onde ela foi verificada. Um link sozinho não ajuda se ninguém entende a relação.

**Mostrar/fazer:** RN03 → US02 → TC03 → BUG01 → versão.

**Perguntar:** O que cada seta significa?

**Compreensão esperada:** a relação precisa explicar derivação ou evidência, não só proximidade.

### 2. Análise de impacto

**Fala sugerida:**

> Quando uma regra muda, a evidência antiga pode continuar útil ou se tornar insuficiente. Precisamos descobrir quais artefatos dependiam da premissa anterior.

**Mostrar/fazer:** RN03 passando a exigir tamanho mínimo.

**Perguntar:** Que itens precisam ser revisados?

**Compreensão esperada:** história/critério, código, casos, documentação, talvez dados e release.

### 3. Versão e evidência

**Fala sugerida:**

> Um caso aprovado ontem não prova que a versão de hoje está coberta após uma mudança relevante.

**Mostrar/fazer:** BUG01 e versão corrigida.

**Perguntar:** Que informação precisa acompanhar o resultado?

**Compreensão esperada:** versão/build/commit ou identificação equivalente.

## 25–45 — Demonstração guiada — Montar cadeia e analisar uma mudança

### Passo 1 — Montar a cadeia

**Fazer:** Escreva RN03, US, TC e BUG em sequência.

**Fala sugerida:**

> Cada vínculo precisa responder ‘por que este artefato existe em relação ao anterior?’.

**Checar com a turma:** Peça a justificativa de TC03.

### Passo 2 — Amarrar à versão

**Fazer:** Adicione referência/variante/versão.

**Fala sugerida:**

> Evidência sem versão pode ser enganosa. O mesmo caso pode produzir resultados diferentes em duas versões.

**Checar com a turma:** Pergunte em qual versão BUG01 é reproduzível.

### Passo 3 — Simular mudança

**Fazer:** Mude catálogo para incluir H12 ou altere RN03.

**Fala sugerida:**

> Agora vamos evitar o erro de dizer ‘já estava aprovado’. A aprovação antiga depende de premissas que mudaram.

**Checar com a turma:** Peça três artefatos afetados.

**Resultado de referência:** A cadeia deve permitir seguir regra → história/critério → caso → execução/defeito → versão/reteste. Mudança exige revisar todos os artefatos dependentes da premissa alterada.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Seguir a mudança

**Cenário:** A regra de catálogo muda para incluir H12 depois de histórias, testes e documentação já existirem.

> Não marquem tudo como impactado por segurança. Expliquem a relação que torna o artefato dependente da mudança.

1. Localizar artefatos que mencionam catálogo.
2. Classificar impacto: precisa mudar / precisa verificar / não afetado.
3. Atualizar uma linha da matriz.
4. Explicar qual evidência precisa ser refeita.

**Entrega:** matriz de impacto

**Observar:** dependências identificadas; impacto justificado; versão/evidência considerada; nenhuma aprovação antiga reaproveitada sem análise.

## 65–77 — Exercício individual

> Com H12 entrando no catálogo, indique pelo menos uma regra, um caso, uma documentação ou exemplo e uma execução que precisam ser revistos. Justifique cada item.

**Entrega:** análise individual de impacto

**Critérios:** itens concretos; relação com mudança; justificativa; nova evidência proposta.

**Ajuda graduada:** comece procurando onde a lista H09/H10/H11 aparece explicitamente.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** o aluno marca tudo como impactado

> Qual premissa deste artefato depende da mudança? Se não houver relação, documente como não afetado.

**Se aparecer:** o aluno reutiliza evidência antiga sem versão

> Como você sabe que esse resultado pertence à implementação atual? Identifique versão/commit.

**Se aparecer:** o aluno confunde bug com requisito

> O bug registra divergência observada; a regra/história define comportamento esperado. Mantenha papéis separados.

### Perguntas de verificação

- **Rastreabilidade é apenas colocar links entre arquivos?** — Não. O vínculo precisa expressar a relação entre necessidade, decisão e evidência.
- **Teste aprovado em versão anterior continua válido após qualquer mudança?** — Não automaticamente; é preciso analisar impacto e repetir o que for relevante.
- **Todos os artefatos sempre mudam quando uma regra muda?** — Não. Devem ser avaliados conforme dependência real.

## 85–90 — Fechamento e tarefa

> Rastreabilidade boa reduz investigação por memória: ela mostra origem, consequência e evidência de cada decisão.

1. Completar vínculos principais.
2. Adicionar versão às evidências.
3. Escolher uma mudança e registrar impacto.
4. Entregar `m07-aula-02-revisao.md`.

**Entrega:** matriz de rastreabilidade + análise de impacto

**Ponte:**

> Na próxima aula vamos usar essa visão de impacto antes do código existir, para reduzir defeitos que poderiam nascer de requisito ambíguo.

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
