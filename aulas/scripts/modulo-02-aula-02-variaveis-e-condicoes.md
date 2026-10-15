# Script do Professor — Variáveis, Tipos e Decisões

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 2, Aula 2](../modulo-02-aula-02-variaveis-e-condicoes.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-02-logica-de-programacao.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  

## Alinhamento obrigatório

- **Objetivo:** Usar variáveis, tipos de dados e condições para representar informações e decisões do caso Agenda Clara em Python introdutório.
- **Demonstração central:** Dicionário de dados e tabela de decisão.
- **Prática em grupo:** Dicionário e decisão em dupla.
- **Exercício individual:** explicar uma escolha de tipo e uma condição.
- **Tarefa:** revisar dicionário e tabela com um caso novo.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Confirmar Python disponível ou preparar alternativa online.
- [ ] Preparar tabela de quatro combinações vazia.
- [ ] Usar exemplos simples; ainda não aprofundar estruturas complexas.
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

> O valor `2` e o texto `'2'` representam a mesma coisa para um programa? Hoje vamos ver como o tipo de dado e a ordem das condições mudam o comportamento.

**Pergunta diagnóstica:** Por que um identificador como H09 pode ser melhor como texto?

Dê cerca de dois minutos para respostas curtas no chat, voz ou caderno. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Porque carrega formato e significado que se perderiam se fosse tratado apenas como número.

**Transição:**

> Vamos representar os dados primeiro e só depois transformar as regras em condições.

## 08–25 — Conceitos e exemplos

### 1. Variáveis e tipos

**Fala sugerida:**

> Variável é um nome que usamos para referenciar um valor. O tipo ajuda a entender o que podemos fazer com esse valor.

**Mostrar/fazer:** compare 2 + 3 e '2' + '3'.

**Perguntar:** Por que H09 é melhor representado como texto do que como número 9 neste caso?

**Compreensão esperada:** porque H09 é identificador de horário e perder o H pode perder significado/formato.

### 2. Atribuição e comparação

**Fala sugerida:**

> Guardar um valor e comparar um valor são operações diferentes. Esse detalhe muda muito quando começamos a escrever condições.

**Mostrar/fazer:** nome = 'Ana' e nome == 'Ana'.

**Perguntar:** Qual linha altera um valor e qual apenas pergunta algo?

**Compreensão esperada:** o aluno diferencia atribuição de comparação.

### 3. Condições e ordem

**Fala sugerida:**

> Uma condição escolhe um caminho. Quando duas entradas estão erradas ao mesmo tempo, a ordem de validação define qual resposta aparece primeiro.

**Mostrar/fazer:** nome inválido e H12 em uma tabela de decisão.

**Perguntar:** Se nome é validado primeiro, qual erro será retornado?

**Compreensão esperada:** nome_invalido antes de avaliar horário.

Evite transformar este bloco em leitura do E-book. Use o E-book como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Dicionário de dados e tabela de decisão

### Passo 1 — Representar os dados

**Fazer:** Monte tabela campo/tipo/exemplo/restrição.

**Fala sugerida:**

> Antes de escrever condição, precisamos saber o que cada dado significa. Tipo é parte dessa explicação.

**Checar com a turma:** Pergunte qual tipo faria sentido para quantidade e para H09.

### Passo 2 — Montar a decisão

**Fazer:** Crie as quatro combinações válido/inválido.

**Fala sugerida:**

> Uma tabela de decisão deixa visível o que deve acontecer em cada combinação. Isso reduz ambiguidades antes de codificar.

**Checar com a turma:** Peça a saída quando nome e horário são inválidos.

### Passo 3 — Levar a regra para Python

**Fazer:** Mostre if/elif curto.

**Fala sugerida:**

> Python é nossa linguagem didática aqui. A lógica vem primeiro; a sintaxe apenas expressa a decisão.

**Checar com a turma:** Troque uma entrada e peça previsão antes de executar.

**Resultado de referência:** Exemplo: `nome` como str não vazio após strip; `horario` como str do catálogo; `quantidade` como int não negativo; lista de horários como list[str]. Se nome é validado primeiro, nome inválido prevalece quando ambas entradas são inválidas.

Antes de mostrar o resultado, peça uma previsão. Depois compare previsão, comportamento observado e explicação.

## 45–50 — Pausa

Informar claramente o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Dicionário e decisão em dupla

**Cenário:** O time precisa documentar os dados e as decisões antes de expandir o código.

**Orientação para a turma:**

> Não escolham o tipo só porque ‘funciona’. Justifiquem o significado do dado e o comportamento esperado.

1. Montar o dicionário de dados.
2. Comparar `2 + 3` com `'2' + '3'`.
3. Completar a tabela de quatro combinações.
4. Trocar a ordem de validação e discutir o efeito.

**Tempo sugerido:** 2 min para organização, 8 min para produção, 3 min para revisão entre pares e 2 min para compartilhamento.

**Entrega esperada:** dicionário de dados + tabela de decisão

**O professor observa:** tipo coerente; restrição explícita; quatro combinações cobertas; ordem de validação explicada.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Explique o que se perde se `H09` virar apenas `9`. Depois escreva ou represente uma condição que rejeita nome vazio/espaços antes de validar o horário. Diga se a regra foi atendida ou se apenas uma mensagem foi exibida.

**Entrega:** resposta curta + condição/tabela

**Critérios:** tipo justificado; condição coerente; diferença entre saída e regra compreendida.

**Se houver dificuldade:** permita começar pela tabela antes de pedir sintaxe Python.

## 77–85 — Correção, intervenções e dúvidas

Comece pedindo que o aluno explique como chegou à resposta antes de mostrar uma referência.

**Se aparecer:** o aluno trata H09 como número por parecer horário

> Que informação do identificador se perde ao remover a letra? O tipo deve representar o significado do dado, não só sua aparência.

**Se aparecer:** o aluno usa `=` para comparar

> Aqui você quer guardar um valor ou fazer uma pergunta? Em Python, `==` responde à comparação.

**Se aparecer:** o aluno acha que exibir mensagem prova que estado está correto

> Mensagem é uma saída. Que evidência mostra que a agenda não foi alterada indevidamente?

### Perguntas de verificação

- **`2` e `'2'` são a mesma coisa?** — Não. Um é número inteiro e o outro é texto; operações podem produzir resultados diferentes.
- **Qual diferença entre `=` e `==`?** — `=` atribui valor; `==` compara valores.
- **A ordem dos `if` pode alterar a resposta?** — Sim, quando mais de uma condição poderia ser inválida/verdadeira; a ordem precisa representar a regra desejada.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> A sintaxe de Python é só a forma que estamos usando para expressar decisões. O que vocês precisam levar é a capacidade de escolher dados e regras de forma consciente.

**Tarefa para casa:**

1. Revisar os dois artefatos com feedback.
2. Adicionar uma entrada nova ou restrição.
3. Executar ao menos um exemplo em Python.
4. Entregar `m02-aula-02-revisao.md` com previsão, resultado e explicação.

**Entrega:** dicionário/tabela revisados + evidência de um exemplo Python

**Ponte para a próxima aula:**

> Na próxima aula vamos parar de escrever a mesma verificação várias vezes e aprender a percorrer coleções.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se a atividade usada foi a mesma definida no roteiro.
- [ ] Anotar qualquer ajuste de tempo para a próxima turma.
- [ ] Não alterar critérios ou respostas de referência apenas na fala; se a regra mudar, atualizar roteiro e script juntos.
