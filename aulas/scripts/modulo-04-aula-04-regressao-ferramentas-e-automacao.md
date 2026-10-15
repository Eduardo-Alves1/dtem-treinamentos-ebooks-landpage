# Script do Professor — Regressão, Ferramentas e Automação

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 4, Aula 4](../modulo-04-aula-04-regressao-ferramentas-e-automacao.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-04-qualidade-de-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Distinguir reteste e regressão, organizar evidências em ferramentas e apresentar automação como forma de repetir verificações úteis, não como substituta do raciocínio de QA.
- **Demonstração central:** Do reteste ao parecer de regressão.
- **Prática em grupo:** Da correção à decisão.
- **Exercício individual:** emitir parecer com um caso crítico pendente.
- **Tarefa:** consolidar plano, casos, bug, reteste e parecer.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Preparar versão com comportamento corrigido/referência.
- [ ] Selecionar cenários adjacentes.
- [ ] Separar trecho curto de automação apenas para ilustração, sem instalação obrigatória.
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

> O bug de nome foi corrigido. Isso significa que podemos declarar todo o sistema aprovado? Hoje vamos separar confirmação da correção, regressão e automação.

**Pergunta diagnóstica:** Qual diferença entre repetir exatamente o caso do bug e testar outros fluxos depois da mudança?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** o primeiro é reteste; os demais compõem regressão para investigar efeitos colaterais.

**Transição:**

> Vamos começar pelo defeito conhecido, ampliar para riscos próximos e só então discutir como repetir parte dessas verificações com código.

## 08–25 — Conceitos e exemplos

### 1. Reteste e regressão

**Fala sugerida:**

> Reteste responde ‘o bug específico foi corrigido?’. Regressão pergunta ‘a mudança que corrigiu isso afetou algo que funcionava?’.

**Mostrar/fazer:** BUG01 + reserva/cancelamento.

**Perguntar:** Depois de corrigir nome, qual comportamento adjacente você verificaria?

**Compreensão esperada:** cenários relevantes como reserva válida e conflito/cancelamento.

### 2. Ferramentas e rastreabilidade

**Fala sugerida:**

> Ferramentas ajudam a organizar trabalho, mas um status ‘Passed’ sem saber versão, dados e evidência é fraco.

**Mostrar/fazer:** fluxo requisito → caso → bug → reteste.

**Perguntar:** Que dado você precisa para confiar em um ‘aprovado’?

**Compreensão esperada:** versão, caso, resultado/evidência e contexto.

### 3. Automação

**Fala sugerida:**

> Automação é código que executa verificações. Não transforma teste ruim em teste bom. Playwright e Cypress frequentemente usam JavaScript/TypeScript; Python também possui ecossistemas de automação.

**Mostrar/fazer:** comparação conceitual manual x automatizado.

**Perguntar:** Qual teste vale automatizar primeiro: algo raro e instável ou um fluxo crítico repetido?

**Compreensão esperada:** tende a fazer mais sentido o crítico/repetitivo/estável, avaliando contexto.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Do reteste ao parecer de regressão

### Passo 1 — Retestar BUG01

**Fazer:** Execute exatamente a entrada que reproduzia o bug.

**Fala sugerida:**

> Não vamos começar por toda a regressão. Primeiro confirmamos se a correção atacou o problema original.

**Checar com a turma:** Peça esperado, observado e versão.

### Passo 2 — Selecionar regressão

**Fazer:** Execute dois ou três fluxos adjacentes.

**Fala sugerida:**

> Não é necessário repetir tudo cegamente. Vamos escolher cenários que podem ter sido afetados pela validação.

**Checar com a turma:** Peça justificativa para cada cenário.

### Passo 3 — Conectar à automação

**Fazer:** Mostre pseudocódigo ou trecho curto de teste.

**Fala sugerida:**

> A automação repete a verificação que já sabemos explicar. Mais adiante, ferramentas como Playwright usam muito JS/TS; a lógica de dado, ação e esperado continua a mesma.

**Checar com a turma:** Pergunte o que ainda precisa ser decidido por uma pessoa.

**Resultado de referência:** Parecer deve indicar o que foi retestado/regredido, em qual versão, quais evidências passaram/falharam e quais riscos permanecem fora do escopo.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Da correção à decisão

**Cenário:** A equipe recebeu uma correção para BUG01 e precisa decidir o mínimo de regressão antes de uma demonstração.

**Orientação para a turma:**

> Não escrevam ‘aprovado’ de forma absoluta. Digam exatamente o que foi verificado e qual decisão esse recorte sustenta.

1. Definir o reteste obrigatório.
2. Escolher três casos de regressão e justificar.
3. Registrar o que permanece fora do escopo.
4. Emitir parecer limitado às evidências.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** mini plano de reteste/regressão + parecer

**O professor observa:** reteste separado de regressão; seleção justificada; limites declarados; parecer coerente.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Imagine que nome foi corrigido, mas o caso crítico de cancelamento ainda não foi executado. Escreva um parecer de três a cinco linhas com decisão, risco e próxima ação.

**Entrega:** parecer individual

**Critérios:** não inventa aprovação; risco explícito; próxima ação objetiva.

**Se houver dificuldade:** use estrutura ‘verificado / pendente / impacto / decisão’.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** “BUG corrigido = versão aprovada.”

> O reteste confirma apenas o defeito específico. Que outros riscos relevantes a mudança pode afetar?

**Se aparecer:** “Automatizado é sempre melhor.”

> Qual o custo de criar/manter e qual valor da repetição? Automação é uma decisão de investimento.

**Se aparecer:** “Para Playwright preciso esquecer Python e reaprender lógica.”

> Não. Condições, funções, dados e asserts seguem a mesma lógica; o que muda é a linguagem e a API da ferramenta.

### Perguntas de verificação

- **Reteste e regressão são sinônimos?** — Não. Reteste verifica a correção específica; regressão verifica possíveis efeitos em comportamentos existentes.
- **Automação substitui teste exploratório?** — Não. Automatiza verificações programadas; exploração e raciocínio continuam necessários.
- **Por que introduzir JS/TS aqui sem trocar a linguagem do módulo de lógica?** — Porque JS/TS aparecem muito em automação moderna; a base de lógica aprendida em Python transfere para essas ferramentas.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Automação é uma evolução natural de testes bem pensados. O valor vem da regra, do risco e do esperado; a ferramenta vem depois.

**Tarefa para casa:**

1. Organizar o plano de testes.
2. Consolidar oito casos e execuções.
3. Revisar BUG01 e reteste.
4. Anexar parecer de regressão.
5. Registrar uma nota: que verificação você automatizaria primeiro e por quê?

**Entrega:** entrega final do Módulo 4

**Ponte para a próxima aula:**

> No próximo módulo vamos olhar para a mesma solução do ponto de vista de Produto: por que construir, para quem e como transformar necessidade em decisões verificáveis.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
