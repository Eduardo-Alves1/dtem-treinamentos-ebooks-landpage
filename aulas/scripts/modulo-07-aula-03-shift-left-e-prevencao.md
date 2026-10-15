# Script do Professor — Shift Left e Prevenção

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar uma aula paralela.

**Roteiro:** [Módulo 7, Aula 3](../modulo-07-aula-03-shift-left-e-prevencao.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-07-ciclo-de-vida-do-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Aplicar Shift Left como antecipação de qualidade, refinando regras e exemplos antes da implementação sem abandonar verificações posteriores.
- **Demonstração central:** Refinar ‘nome obrigatório’ antes do código.
- **Prática em grupo:** Três perspectivas.
- **Exercício individual:** refinar ‘cancelamento simples’.
- **Tarefa:** revisar uma regra com exemplos e decisão registrada.

## Antes da aula

- [ ] Separar regras vagas.
- [ ] Preparar tabela Produto/Dev/QA.
- [ ] Evitar apresentar Shift Left como responsabilidade exclusiva de QA.
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

> Quanto trabalho podemos evitar fazendo uma boa pergunta antes de implementar? Hoje vamos transformar regras curtas em decisões compartilhadas e testáveis.

**Pergunta diagnóstica:** Shift Left significa testar tudo antes de programar?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** Não. Significa antecipar atividades e perguntas de qualidade/risk; verificação posterior continua necessária.

**Transição:**

> Vamos começar com uma frase aparentemente simples e descobrir quantas interpretações ela permite.

## 08–25 — Conceitos e exemplos

### 1. Shift Left como antecipação

**Fala sugerida:**

> Shift Left não significa mover todos os testes para o começo. Significa trazer perguntas de qualidade e risco para decisões anteriores, quando mudar é mais barato.

**Mostrar/fazer:** regra ‘nome obrigatório’.

**Perguntar:** Que ambiguidade existe se não definirmos espaços?

**Compreensão esperada:** nome com apenas espaços pode ser interpretado de formas diferentes.

### 2. Exemplos e critérios

**Fala sugerida:**

> Uma frase curta melhora quando adicionamos exemplos que pessoas diferentes conseguem verificar.

**Mostrar/fazer:** Ana aceita; vazio/espaços recusados.

**Perguntar:** Depois de recusar, o que deve acontecer com o estado?

**Compreensão esperada:** não deve criar reserva.

### 3. Três perspectivas

**Fala sugerida:**

> Colaboração antecipada não significa QA escrever tudo. Cada área traz uma perspectiva para reduzir lacunas antes da implementação.

**Mostrar/fazer:** perguntas de cada papel.

**Perguntar:** Que pergunta técnica Dev faria? E que risco QA levantaria?

**Compreensão esperada:** respostas diferentes, complementares.

## 25–45 — Demonstração guiada — Refinar ‘nome obrigatório’ antes do código

### Passo 1 — Expor a ambiguidade

**Fazer:** Escreva apenas ‘nome obrigatório’.

**Fala sugerida:**

> Parece claro até duas pessoas implementarem interpretações diferentes. Vamos descobrir o que ainda não está definido.

**Checar com a turma:** Pergunte sobre vazio, espaços e tipo inválido.

### Passo 2 — Criar exemplos

**Fazer:** Monte tabela entrada/esperado/estado.

**Fala sugerida:**

> Exemplos ajudam Produto, Dev e QA a discutir a mesma coisa antes de existir código.

**Checar com a turma:** Peça um caso positivo e dois negativos.

### Passo 3 — Preservar verificação posterior

**Fazer:** Anote quais casos serão executados depois.

**Fala sugerida:**

> Antecipar não substitui testar a implementação. Primeiro reduzimos ambiguidade; depois verificamos se o código respeitou a decisão.

**Checar com a turma:** Pergunte que evidência confirmaria a implementação.

**Resultado de referência:** Critério exemplo: nome textual com conteúdo após remoção de espaços; ‘Ana’ aceita; vazio/espaços recusados; recusa não altera estado da agenda.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Três perspectivas

**Cenário:** Cada trio recebe uma regra curta e distribui Produto, Dev e QA para refiná-la.

> Não tentem fazer QA decidir produto nem Produto desenhar código. Usem as perspectivas para construir entendimento compartilhado.

1. Produto explica objetivo e contexto.
2. Dev aponta decisão/limitação técnica a esclarecer.
3. QA propõe riscos e exemplos.
4. O trio escreve critérios verificáveis.
5. Trocar regra com outro trio para revisão.

**Entrega:** regra refinada + exemplos

**Observar:** perspectivas distintas; ambiguidade reduzida; critério verificável; teste posterior previsto.

## 65–77 — Exercício individual

> A frase ‘o usuário pode cancelar uma reserva’ é vaga. Escreva duas perguntas de esclarecimento e dois critérios verificáveis, incluindo um cenário de ID inexistente.

**Entrega:** perguntas + critérios

**Critérios:** ambiguidades reais; positivo/negativo; estado esperado; sem inventar autorização não definida.

**Ajuda graduada:** pergunte ‘quem pode cancelar? qual reserva? o que acontece se ela não existir?’.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** o aluno traduz Shift Left como ‘rodar automação mais cedo’

> Automação pode participar, mas o conceito é mais amplo: requisitos, design, segurança, testabilidade e exemplos também podem ser antecipados.

**Se aparecer:** QA passa a definir regra de negócio sozinho

> Quem possui contexto de valor e decisão de produto? QA ajuda a revelar lacunas; a regra é construída/decidida colaborativamente.

**Se aparecer:** os critérios não falam do estado após falha

> A saída está descrita, mas o que não pode mudar? Inclua o estado relevante.

### Perguntas de verificação

- **Shift Left elimina necessidade de testes depois do código?** — Não. Antecipação reduz ambiguidades e riscos; a implementação ainda precisa ser verificada.
- **QA deve ser dono de todos os critérios?** — Não. Critérios são colaborativos; Produto, Dev e QA trazem perspectivas complementares.
- **Perguntar cedo garante que nenhum bug ocorrerá?** — Não. Reduz certos riscos, mas não elimina defeitos nem incerteza.

## 85–90 — Fechamento e tarefa

> Prevenção não substitui detecção. Shift Left melhora a qualidade das decisões antes do código e prepara verificações mais fortes depois.

1. Escolher uma regra do projeto.
2. Registrar pergunta antes da solução.
3. Criar exemplos positivos e negativos.
4. Definir evidência futura.
5. Entregar `m07-aula-03-revisao.md`.

**Entrega:** regra refinada + exemplos + plano de verificação

**Ponte:**

> Na próxima aula vamos usar tudo isso para uma decisão concreta: podemos liberar? E o que fazemos se uma verificação crítica falhar?

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
