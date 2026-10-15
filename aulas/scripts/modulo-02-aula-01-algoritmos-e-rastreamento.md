# Script do Professor — Algoritmos e Rastreamento

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 2, Aula 1](../modulo-02-aula-01-algoritmos-e-rastreamento.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-02-logica-de-programacao.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  

## Alinhamento obrigatório

- **Objetivo:** Ensinar o aluno a descrever um algoritmo e rastrear manualmente entradas, decisões, saídas e estado antes de escrever código.
- **Demonstração central:** Algoritmo de reserva sem código.
- **Prática em grupo:** Rastreamento cruzado de reservas.
- **Exercício individual:** rastrear três novas tentativas em sequência.
- **Tarefa:** revisar o algoritmo e acrescentar um exemplo próprio.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Revisar RN01–RN05 e RN08.
- [ ] Preparar a tabela de rastreamento vazia.
- [ ] Não abrir código no início da aula; o objetivo é lógica antes de sintaxe.
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

> Hoje vamos organizar uma solução antes de escrever código. Se eu disser apenas ‘faça uma reserva’, essa instrução é suficiente para outra pessoa executar sem inventar regras?

**Pergunta diagnóstica:** Quais informações entram em uma reserva e o que precisa ser verificado antes de confirmar?

Dê cerca de dois minutos para respostas curtas no chat, voz ou caderno. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Nome/identidade e horário entram; é preciso validar os dados e o estado/disponibilidade antes de alterar a agenda.

**Transição:**

> Vamos transformar uma regra de negócio em passos que qualquer pessoa consiga rastrear no papel.

## 08–25 — Conceitos e exemplos

### 1. Algoritmo

**Fala sugerida:**

> Um algoritmo é uma descrição organizada de como resolver um problema. Antes de pensar em Python, precisamos deixar claro o que entra, o que é verificado e qual resultado sai.

**Mostrar/fazer:** escreva um algoritmo simples de reserva sem código.

**Perguntar:** Qual é a entrada e qual é a primeira verificação?

**Compreensão esperada:** o aluno separa dados de entrada da regra.

### 2. Rastreamento manual

**Fala sugerida:**

> Rastrear é executar a lógica no papel. Isso ajuda a entender comportamento sem depender de uma linguagem.

**Mostrar/fazer:** tabela Passo / Entrada / Decisão / Estado.

**Perguntar:** Depois de uma reserva bem-sucedida, o que mudou no estado?

**Compreensão esperada:** o aluno reconhece que H09 passa a estar ocupado.

### 3. Falha sem corrupção de estado

**Fala sugerida:**

> Uma tentativa recusada também é um resultado. Ela não deve apagar ou alterar uma reserva válida anterior sem uma regra que permita isso.

**Mostrar/fazer:** compare Ana/H09 e Bruno/H09.

**Perguntar:** O que precisa permanecer igual quando Bruno é recusado?

**Compreensão esperada:** H09 continua associado à reserva de Ana.

Evite transformar este bloco em leitura do E-book. Use o E-book como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Algoritmo de reserva sem código

### Passo 1 — Definir entradas e ordem

**Fazer:** Escreva nome e horário; liste validações.

**Fala sugerida:**

> Ainda não vamos programar. Primeiro vamos deixar a regra explícita e decidir em que ordem cada verificação acontece.

**Checar com a turma:** Pergunte o que deve ser validado antes de alterar a agenda.

### Passo 2 — Rastrear Ana/H09

**Fazer:** Percorra o algoritmo e marque H09 como ocupado.

**Fala sugerida:**

> A cada passo eu vou dizer o estado antes e depois. Isso é o que permite outra pessoa conferir meu raciocínio.

**Checar com a turma:** Peça à turma para prever a saída antes de marcar a reserva.

### Passo 3 — Rastrear Bruno/H09

**Fazer:** Repita na mesma agenda.

**Fala sugerida:**

> Agora o dado de entrada é válido, mas o estado mudou. A decisão depende do que já aconteceu.

**Checar com a turma:** Pergunte por que a recusa não pode remover a reserva de Ana.

**Resultado de referência:** Ana/H09 resulta em sucesso e H09 ocupado por Ana. Bruno/H09 resulta em conflito; H09 continua ocupado por Ana.

Antes de mostrar o resultado, peça uma previsão. Depois compare previsão, comportamento observado e explicação.

## 45–50 — Pausa

Informar claramente o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Rastreamento cruzado de reservas

**Cenário:** Agenda inicialmente vazia com H09, H10 e H11 disponíveis.

**Orientação para a turma:**

> Uma pessoa executa e a outra confere cada mudança de estado. Troquem os papéis antes do terceiro caso.

1. Rastrear Lia/H10.
2. Rastrear Rui/H10 na mesma agenda.
3. Trocar papéis de autor e revisor.
4. Avaliar nome somente com espaços/H11 e justificar a saída.

**Tempo sugerido:** 2 min para organização, 8 min para produção, 3 min para revisão entre pares e 2 min para compartilhamento.

**Entrega esperada:** tabela de rastreamento com estado após cada tentativa

**O professor observa:** ordem de validação explícita; saída coerente; estado preservado; revisão entre pares.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Em nova agenda, H10 está ocupado por Carla e H09/H11 estão livres. Rastreie Rui/H10, nome somente com espaços/H09 e Dani/H11, nessa ordem. Para cada tentativa, registre o passo decisivo, a saída e o estado final.

**Entrega:** rastreamento individual das três tentativas

**Critérios:** decisão correta; estado coerente; explicação de uma aprovação e uma recusa.

**Se houver dificuldade:** dê apenas a primeira entrada e peça que o aluno escreva ‘estado antes’ antes de decidir.

## 77–85 — Correção, intervenções e dúvidas

Comece pedindo que o aluno explique como chegou à resposta antes de mostrar uma referência.

**Se aparecer:** “Se deu erro, volta tudo para vazio.”

> Erro da nova tentativa não significa apagar um estado válido anterior. Qual regra autorizaria essa alteração?

**Se aparecer:** “Algoritmo é o código em Python.”

> Python será uma ferramenta depois. Primeiro estamos descrevendo a lógica de forma independente da linguagem.

**Se aparecer:** o aluno pula direto para a saída

> Mostre o estado inicial e peça para apontar qual verificação decidiu o caminho.

### Perguntas de verificação

- **Se a segunda tentativa falhar, por que o estado anterior deve permanecer?** — Porque a regra de conflito recusa a nova operação sem apagar a reserva existente.
- **Algoritmo precisa estar em Python?** — Não. Pode ser linguagem natural, fluxograma ou pseudocódigo.
- **O que muda entre duas execuções com as mesmas entradas quando o estado é diferente?** — A decisão pode mudar porque o sistema considera o estado atual.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Se vocês conseguem explicar a sequência e o estado sem depender de código, já construíram a base que depois poderá ser implementada em qualquer linguagem.

**Tarefa para casa:**

1. Revisar a atividade com o feedback.
2. Adicionar um caso novo de sucesso ou recusa.
3. Registrar o que mudou entre a primeira e a segunda versão.
4. Entregar `m02-aula-01-revisao.md`.

**Entrega:** algoritmo e rastreamento revisados

**Ponte para a próxima aula:**

> Na próxima aula vamos começar a representar essas informações em Python e entender como tipos e condições mudam o comportamento.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se a atividade usada foi a mesma definida no roteiro.
- [ ] Anotar qualquer ajuste de tempo para a próxima turma.
- [ ] Não alterar critérios ou respostas de referência apenas na fala; se a regra mudar, atualizar roteiro e script juntos.
