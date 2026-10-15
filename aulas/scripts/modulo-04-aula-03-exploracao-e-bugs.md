# Script do Professor — Exploração e Reporte de Bugs

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 4, Aula 3](../modulo-04-aula-03-exploracao-e-bugs.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-04-qualidade-de-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Ensinar exploração orientada por missão e reporte de bugs baseado em referência, passos reproduzíveis, esperado, observado e impacto.
- **Demonstração central:** Explorar uma sequência e reportar BUG01.
- **Prática em grupo:** Investigar e comunicar.
- **Exercício individual:** reescrever BUG01 com palavras próprias.
- **Tarefa:** revisar BUG01 após tentativa de reprodução por colega.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Resetar estado entre demonstrações.
- [ ] Preparar referência e variante.
- [ ] Ter modelo de bug report aberto.
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

> A variante aceita um nome composto apenas por espaços. Isso é bug, dúvida ou melhoria? A resposta depende de referência e evidência.

**Pergunta diagnóstica:** O que precisamos para chamar uma divergência de bug?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Um comportamento esperado sustentado por regra/requisito e evidência do comportamento observado.

**Transição:**

> Primeiro vamos explorar com uma pergunta clara; depois transformamos um achado reproduzível em comunicação útil para o time.

## 08–25 — Conceitos e exemplos

### 1. Exploração com missão

**Fala sugerida:**

> Teste exploratório não é clicar aleatoriamente. Entramos com uma missão, aprendemos durante a execução e registramos o que encontramos.

**Mostrar/fazer:** missão: investigar cancelamento e reutilização de horário.

**Perguntar:** Que sequência poderia revelar problema de estado?

**Compreensão esperada:** reservar, cancelar, consultar e reservar novamente.

### 2. Bug, dúvida ou melhoria

**Fala sugerida:**

> Para chamar algo de bug precisamos de uma referência que diga que o comportamento deveria ser diferente. Sem isso pode ser dúvida ou pedido de melhoria.

**Mostrar/fazer:** RN03 versus variante.

**Perguntar:** Qual regra é violada por espaços aceitos?

**Compreensão esperada:** RN03.

### 3. Reporte reproduzível

**Fala sugerida:**

> O objetivo do bug report é permitir decisão e reprodução, não demonstrar que o QA ‘achou um erro’.

**Mostrar/fazer:** BUG01 estruturado.

**Perguntar:** O que faltaria se o reporte dissesse apenas ‘campo nome aceita espaço’?

**Compreensão esperada:** contexto, dados, versão, passos, esperado/observado e estado.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Explorar uma sequência e reportar BUG01

### Passo 1 — Explorar cancelamento

**Fazer:** Execute sequência de reservar/cancelar/reservar.

**Fala sugerida:**

> Vou mudar uma coisa de cada vez e observar estado. A missão é aprender se o horário volta a ficar disponível corretamente.

**Checar com a turma:** Pergunte o que observar após cada ação.

### Passo 2 — Reproduzir BUG01

**Fazer:** Execute nome apenas com espaços na variante.

**Fala sugerida:**

> Antes de chamar de bug, vamos voltar à RN03. A divergência existe porque temos uma referência explícita.

**Checar com a turma:** Peça esperado e observado separados.

### Passo 3 — Escrever reporte

**Fazer:** Preencha título, versão, passos, esperado, observado, evidência e impacto.

**Fala sugerida:**

> Hipótese de causa pode existir, mas ficará marcada como hipótese. Não vamos inventar explicação técnica.

**Checar com a turma:** Peça a outra pessoa para repetir só lendo o reporte.

**Resultado de referência:** BUG01: variante aceita nome com espaços, retorna sucesso e altera estado; esperado pela RN03 é `nome_invalido` sem alteração da agenda.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Investigar e comunicar

**Cenário:** Uma dupla explora uma sequência; outra deve reproduzir o achado usando apenas o registro produzido.

**Orientação para a turma:**

> Não tentem maximizar quantidade de achados. Maximizem clareza sobre o que observaram.

1. Definir uma missão de 1 frase.
2. Executar sequência curta.
3. Registrar qualquer divergência.
4. Trocar o registro com outra dupla para reprodução.
5. Classificar como bug, dúvida ou melhoria com justificativa.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** nota de exploração + reporte/reclassificação

**O professor observa:** missão explícita; observado separado de hipótese; reprodução possível; classificação justificada.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Produza um reporte de BUG01 sem copiar o exemplo: título, versão, pré-condição, passos, esperado, observado, efeito no estado e impacto. Acrescente uma hipótese claramente marcada como não confirmada.

**Entrega:** bug report individual

**Critérios:** reproduzível; esperado ligado à regra; observado factual; hipótese identificada.

**Se houver dificuldade:** comece por esperado e observado; depois complete os passos que levam de um ao outro.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** o reporte contém ‘acho que o banco está errado’ como observado

> Isso é hipótese. O que você realmente viu na entrada, saída e estado?

**Se aparecer:** título genérico ‘sistema com erro’

> Que comportamento, em qual ação e com qual consequência? O título deve permitir triagem.

**Se aparecer:** o aluno pula a regra e chama tudo de bug

> Qual requisito ou comportamento esperado está sendo violado?

### Perguntas de verificação

- **Todo comportamento estranho é bug?** — Não. É preciso referência/expectativa; sem ela pode ser dúvida, limitação ou melhoria.
- **Se tenho uma hipótese da causa, posso colocá-la como fato?** — Não. Deve ser marcada como hipótese até haver evidência.
- **Severidade e prioridade são sempre iguais?** — Não. Severidade trata impacto técnico/usuário; prioridade considera contexto de negócio, prazo e risco.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Explorar bem é aprender com intenção; reportar bem é separar fato, expectativa, impacto e hipótese para que o time consiga agir.

**Tarefa para casa:**

1. Pedir que outra pessoa tente reproduzir.
2. Registrar onde ela teve dúvida.
3. Revisar o reporte.
4. Entregar `m04-aula-03-revisao.md`.

**Entrega:** BUG01 revisado + nota do feedback

**Ponte para a próxima aula:**

> Na próxima aula vamos imaginar que BUG01 foi corrigido: como confirmar a correção sem esquecer que a mudança pode ter afetado outros comportamentos?

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
