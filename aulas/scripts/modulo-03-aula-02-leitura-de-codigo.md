# Script do Professor — Leitura de Código e Comportamento

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 3, Aula 2](../modulo-03-aula-02-leitura-de-codigo.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Ensinar o iniciante a ler código pelo comportamento, rastreando entradas, decisões e retornos sem exigir domínio completo da linguagem.
- **Demonstração central:** Rastrear duas chamadas e comparar uma lógica entre linguagens.
- **Prática em grupo:** Leia pelo comportamento.
- **Exercício individual:** rastrear uma entrada inválida.
- **Tarefa:** rastrear uma chamada nova e comparar uma função simples.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Abrir a função `reservar`.
- [ ] Preparar trechos equivalentes curtos de `validar_nome` em Python, JS e TS.
- [ ] Evitar introduzir Node, build ou configuração TypeScript nesta aula.
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

> Vocês não precisam escrever o programa inteiro para conseguir entender uma regra. Hoje vamos ler uma operação usando entradas concretas e depois comparar a mesma lógica em outra sintaxe.

**Pergunta diagnóstica:** Se eu trocar Python por JavaScript, a ideia de `if` e retorno deixa de existir?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Não. A linguagem muda a sintaxe, mas os conceitos lógicos permanecem.

**Transição:**

> Primeiro vamos provar isso lendo o comportamento em Python; depois fazemos uma comparação curta com JS e TS.

## 08–25 — Conceitos e exemplos

### 1. Ler pelo contrato

**Fala sugerida:**

> Ler código não significa entender cada linha do projeto. Começamos pela operação que queremos explicar: que dados recebe e o que promete devolver.

**Mostrar/fazer:** assinatura de `reservar`.

**Perguntar:** Que pergunta essa operação responde?

**Compreensão esperada:** se a reserva pode ser criada e qual resultado retorna.

### 2. Estado e retorno

**Fala sugerida:**

> Um `return` pode encerrar o caminho antes de qualquer alteração. Por isso rastrear retorno e estado juntos ajuda a entender o comportamento.

**Mostrar/fazer:** caminho de conflito antes da inserção.

**Perguntar:** Em qual ponto uma reserva deixa de poder ser criada?

**Compreensão esperada:** quando uma validação falha ou o horário já está ocupado.

### 3. Mesma lógica, outra sintaxe

**Fala sugerida:**

> A lógica aprendida no módulo anterior não pertence ao Python. Vamos comparar uma validação simples em outras linguagens apenas para enxergar que a ideia permanece.

**Mostrar/fazer:** `validar_nome` em Python, JS e TS lado a lado.

**Perguntar:** O que mudou: a regra ou a forma de escrevê-la?

**Compreensão esperada:** a regra permanece; sintaxe e tipagem mudam.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Rastrear duas chamadas e comparar uma lógica entre linguagens

### Passo 1 — Rastrear caminho de sucesso

**Fazer:** Siga Ana/H09 e marque condições.

**Fala sugerida:**

> Não vou explicar o arquivo inteiro. Vou seguir uma entrada concreta e observar as decisões que ela atravessa.

**Checar com a turma:** Peça o estado antes e depois.

### Passo 2 — Rastrear caminho de conflito

**Fazer:** Siga Bruno/H09.

**Fala sugerida:**

> Agora a mesma função recebe uma entrada parecida, mas encontra outro estado. Vamos localizar o retorno que encerra o caminho.

**Checar com a turma:** Pergunte se alguma alteração de estado ocorre depois do retorno.

### Passo 3 — Comparar linguagens

**Fazer:** Mostre uma função de validação equivalente em três sintaxes.

**Fala sugerida:**

> Python continua sendo nossa linguagem principal para lógica. JS e TS aparecem aqui só para provar uma ideia: a lógica transfere; a escrita muda.

**Checar com a turma:** Peça aos alunos para apontar entrada, decisão e retorno nas três versões.

**Resultado de referência:** O segundo pedido para H09 retorna conflito antes de inserir nova reserva. Na comparação de linguagens, a intenção de `validar_nome` permanece equivalente apesar da sintaxe.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Leia pelo comportamento

**Cenário:** Cada dupla recebe uma entrada diferente do laboratório e precisa explicar o caminho sem comentar o arquivo inteiro.

**Orientação para a turma:**

> Vocês não precisam explicar todas as linhas. Expliquem apenas as que afetam a entrada que receberam.

1. Identificar entrada.
2. Marcar as condições relevantes.
3. Registrar retorno e estado final.
4. Trocar com outra dupla para revisão.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** trilha de execução anotada

**O professor observa:** caminho coerente; retorno identificado; estado final correto; explicação focada.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Rastreie nome válido com H12 em agenda vazia. Indique onde a operação para, qual retorno é produzido e se o estado muda. Depois escreva em uma frase o que seria igual se essa regra estivesse em JavaScript.

**Entrega:** rastreamento + frase de transferência

**Critérios:** retorno correto; estado correto; linha/condição decisiva identificada; lógica separada da sintaxe.

**Se houver dificuldade:** peça primeiro só ‘qual condição falha?’ e depois complete retorno/estado.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** o aluno tenta traduzir cada linha para português

> Escolha primeiro a entrada e marque apenas as condições que ela realmente atravessa.

**Se aparecer:** o aluno assume que retorno de conflito também altera estado

> Onde está a instrução que modifica a agenda nesse caminho? O retorno pode acontecer antes dela.

**Se aparecer:** o aluno acha que agora precisa dominar TS

> Não. TS é apenas comparação introdutória. O objetivo é enxergar a portabilidade da lógica.

### Perguntas de verificação

- **Preciso entender todo o arquivo para explicar uma função?** — Não. É possível começar pelo contrato e rastrear uma entrada concreta.
- **Depois de um `return`, o restante daquele caminho executa?** — Não; a função encerra naquele ponto.
- **Ao passar de Python para JS/TS, a lógica precisa ser reaprendida do zero?** — Não. Conceitos como condição, laço e função permanecem; a sintaxe e a tipagem variam.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Ler código é seguir intenção, decisões e estado. A linguagem importa, mas a lógica é o fio que permite vocês aprenderem novas sintaxes depois.

**Tarefa para casa:**

1. Rastrear outra entrada do laboratório.
2. Registrar retorno e estado.
3. Escolher uma função simples de lógica do Módulo 2 e observar uma versão equivalente em JS ou TS, sem obrigação de programar um projeto.
4. Entregar `m03-aula-02-revisao.md`.

**Entrega:** rastreamento revisado + comparação curta

**Ponte para a próxima aula:**

> Agora que conseguimos ler uma mudança, precisamos aprender a registrá-la de forma que outra pessoa entenda o que aconteceu.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
