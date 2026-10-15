# Script do Professor — Qualidade, Riscos e Plano de Testes

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 4, Aula 1](../modulo-04-aula-01-qualidade-riscos-e-plano.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-04-qualidade-de-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Introduzir qualidade orientada a risco e produzir um plano de testes enxuto com escopo, prioridades, estratégia e limites.
- **Demonstração central:** Construir um plano de testes de uma página.
- **Prática em grupo:** Planejar antes de executar.
- **Exercício individual:** detalhar risco de cancelamento.
- **Tarefa:** revisar o plano e acrescentar uma limitação.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Abrir RN01–RN08.
- [ ] Testar o laboratório.
- [ ] Preparar modelo de plano de uma página.
- [ ] Deixar o roteiro e este script abertos.
- [ ] Testar qualquer ferramenta, arquivo ou demonstração antes da turma entrar.
- [ ] Separar o material que o aluno deverá entregar ao final.

## Agenda de condução

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

**Fala de abertura:**

> Se vocês tivessem pouco tempo para testar a agenda, por onde começariam? A resposta não deveria ser ‘clicar em tudo’, e sim pensar no que pode dar errado e no impacto.

**Pergunta diagnóstica:** Qual risco do Agenda Clara você investigaria primeiro e por quê?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** qualquer escolha coerente precisa relacionar comportamento a impacto; duplicidade tende a ser crítica para integridade da agenda.

**Transição:**

> Vamos transformar risco em um plano objetivo, deixando claro o que será e o que não será investigado.

## 08–25 — Conceitos e exemplos

### 1. Qualidade compartilhada

**Fala sugerida:**

> QA não entra apenas no final. Qualidade melhora quando regras, riscos e exemplos são discutidos cedo e depois verificados com evidências.

**Mostrar/fazer:** uma regra ambígua e um exemplo claro.

**Perguntar:** Que problema poderíamos evitar antes de desenvolver?

**Compreensão esperada:** ambiguidade, regra conflitante ou caso crítico esquecido.

### 2. Risco

**Fala sugerida:**

> Se o tempo é limitado, não testamos tudo com a mesma profundidade. Risco ajuda a decidir onde investir esforço.

**Mostrar/fazer:** duplicidade, nome inválido e cancelamento.

**Perguntar:** Qual falha causaria maior impacto para uma recepção?

**Compreensão esperada:** resposta justificada, não necessariamente única.

### 3. Plano de testes

**Fala sugerida:**

> Plano não precisa ser longo. Ele precisa orientar decisão: o que investigaremos, por quê, com quais dados e o que não estaremos provando.

**Mostrar/fazer:** estrutura de uma página.

**Perguntar:** O que não podemos afirmar após testes apenas sequenciais e em memória?

**Compreensão esperada:** concorrência real, persistência, segurança etc.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Construir um plano de testes de uma página

### Passo 1 — Definir objetivo/escopo

**Fazer:** Escreva o que a equipe quer ganhar de confiança.

**Fala sugerida:**

> Plano começa com decisão, não com ferramenta. Vamos definir o que estamos tentando verificar e o que fica fora.

**Checar com a turma:** Peça um exemplo de fora de escopo.

### Passo 2 — Ligar risco a teste

**Fazer:** Associe duplicidade a cenário de conflito.

**Fala sugerida:**

> Cada risco importante deve apontar para uma evidência que nos ajude a avaliá-lo.

**Checar com a turma:** Pergunte qual teste investigaria cancelamento.

### Passo 3 — Definir encerramento

**Fazer:** Escreva condições observáveis.

**Fala sugerida:**

> ‘Testar tudo’ não é critério de fim. Precisamos de uma condição que possamos conferir.

**Checar com a turma:** Peça uma condição crítica de encerramento.

**Resultado de referência:** Plano enxuto contendo objetivo, RN01–RN08, riscos priorizados, abordagem, ambiente/dados, critérios de início/fim e limites como ausência de persistência/concorrência real.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Planejar antes de executar

**Cenário:** A equipe precisa decidir o foco de testes do MVP Agenda Clara antes de iniciar execução.

**Orientação para a turma:**

> Se duas duplas priorizarem diferente, a discussão deve ser sobre contexto e impacto, não sobre uma resposta decorada.

1. Escolher três riscos.
2. Ordená-los com justificativa.
3. Relacionar cada risco a um tipo de evidência/teste.
4. Registrar um limite que a estratégia não cobre.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** recorte de plano de testes

**O professor observa:** risco justificado; evidência relacionada; limite explícito; sem promessa de ‘zero bugs’.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Escolha o risco de cancelamento e escreva objetivo, dados necessários, sequência de investigação, evidência esperada e uma limitação do teste.

**Entrega:** bloco individual do plano

**Critérios:** risco claro; evidência observável; sequência coerente; limite declarado.

**Se houver dificuldade:** forneça a regra de cancelamento e peça primeiro apenas ‘qual comportamento provaria que está errado?’.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** “QA garante qualidade.”

> QA contribui com técnicas e investigação, mas Produto, Dev, Infra e outras áreas também tomam decisões que afetam qualidade.

**Se aparecer:** plano vira lista de ferramentas

> Que risco cada ferramenta ajudará a investigar? Se não houver relação, a ferramenta não é a estratégia.

**Se aparecer:** critério de fim ‘quando tudo passar’

> Quais casos são críticos? O que significa ‘tudo’ e em qual escopo?

### Perguntas de verificação

- **Testes provam que não existem bugs?** — Não. Eles aumentam confiança no escopo e condições investigadas.
- **Plano de testes precisa ser um documento enorme?** — Não. Precisa ser suficiente para orientar decisões e tornar premissas explícitas.
- **Quem é responsável pela qualidade?** — O time inteiro; QA tem contribuição especializada, não propriedade exclusiva.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Planejamento de QA não é burocracia: é tornar explícito onde queremos confiança, que evidência precisamos e quais limites ainda permanecem.

**Tarefa para casa:**

1. Revisar o plano com feedback.
2. Acrescentar pelo menos uma limitação relevante.
3. Entregar `m04-aula-01-revisao.md`.

**Entrega:** plano de testes revisado

**Ponte para a próxima aula:**

> Na próxima aula vamos pegar as regras do plano e escrever casos que outra pessoa consegue executar e conferir.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
