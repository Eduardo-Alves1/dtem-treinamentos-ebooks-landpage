# Script do Professor — Sistemas e Construção de Software

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 3, Aula 1](../modulo-03-aula-01-sistemas-e-construcao.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Explicar como um sistema é formado por componentes que recebem entradas, aplicam regras, mantêm estado e produzem saídas, distinguindo o que existe no laboratório do que seria uma arquitetura futura.
- **Demonstração central:** Mapear os componentes reais do laboratório.
- **Prática em grupo:** Anatomia do laboratório.
- **Exercício individual:** explicar propósito, comportamento e limite do sistema.
- **Tarefa:** revisar o diagrama e documentar dois limites.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Executar o laboratório antes da aula.
- [ ] Confirmar que o reinício zera o estado.
- [ ] Abrir README e arquivos relevantes.
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

> Um desenho de tela e um programa que executa uma reserva são a mesma entrega? Hoje vamos separar o que o sistema realmente possui do que ainda é apenas uma ideia de arquitetura.

**Pergunta diagnóstica:** Que evidência precisamos para afirmar que existe uma API ou um banco de dados?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Código/configuração/execução verificável; não basta imaginar que uma aplicação deveria ter esses componentes.

**Transição:**

> Vamos seguir uma operação concreta do laboratório e descobrir quais peças realmente participam.

## 08–25 — Conceitos e exemplos

### 1. Sistema e componentes

**Fala sugerida:**

> Um sistema não é apenas uma tela. Precisamos localizar onde entram dados, onde regras são aplicadas, que estado muda e que resultado é devolvido.

**Mostrar/fazer:** README e estrutura do laboratório.

**Perguntar:** Qual é a entrada principal de uma reserva no laboratório?

**Compreensão esperada:** nome e horário; o laboratório executa regras sobre esses dados.

### 2. Interface, lógica e estado

**Fala sugerida:**

> A interface pode nem existir e ainda assim a regra pode ser executável. No laboratório, vamos observar lógica e estado sem fingir que já existe uma aplicação web.

**Mostrar/fazer:** desenho hipotético de tela separado do código real.

**Perguntar:** Uma tela proposta prova que existe front-end implementado?

**Compreensão esperada:** não; é uma proposta/representação.

### 3. Persistência e limite

**Fala sugerida:**

> Se o programa termina e as reservas desaparecem, isso nos mostra um limite de estado em memória. Persistência exigiria outro componente e novas decisões.

**Mostrar/fazer:** reinicie o laboratório e compare o estado.

**Perguntar:** Que componente ou mecanismo faltaria para preservar os dados?

**Compreensão esperada:** algum mecanismo de persistência, como banco/arquivo, ainda não implementado.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Mapear os componentes reais do laboratório

### Passo 1 — Ler antes de executar

**Fazer:** Abra README e identifique o propósito.

**Fala sugerida:**

> Antes de navegar pelo código, vamos descobrir qual problema este laboratório pretende simular e quais limites ele declara.

**Checar com a turma:** Peça ao aluno para apontar uma frase que descreve o propósito.

### Passo 2 — Seguir entrada, regra e estado

**Fazer:** Execute uma reserva e mostre onde o estado muda.

**Fala sugerida:**

> Vamos acompanhar um comportamento concreto em vez de tentar entender o arquivo inteiro de uma vez.

**Checar com a turma:** Pergunte qual dado entrou, qual decisão aconteceu e o que mudou.

### Passo 3 — Testar o limite de persistência

**Fazer:** Reinicie o processo.

**Fala sugerida:**

> Quando o processo termina, o estado some. Isso não é um bug escondido; é um limite conhecido do laboratório.

**Checar com a turma:** Pergunte o que seria necessário investigar para tornar o estado persistente.

**Resultado de referência:** O laboratório possui lógica de agenda e estado em memória; não implementa interface web, API HTTP, banco persistente ou infraestrutura de produção.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Anatomia do laboratório

**Cenário:** A dupla precisa explicar o Agenda Clara para uma pessoa que nunca viu o projeto.

**Orientação para a turma:**

> Sempre marquem se algo foi observado no projeto ou se é uma proposta de evolução.

1. Identificar entrada, regra, estado e saída.
2. Marcar o que existe no código.
3. Desenhar uma interface/API futura como hipótese.
4. Listar dois limites do laboratório.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** diagrama anotado do sistema

**O professor observa:** componentes reais separados de hipóteses; limites explícitos; relações coerentes.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Escreva uma descrição curta do Agenda Clara contendo propósito, entrada, comportamento principal, estado e um limite. Depois diga qual componente faltaria para manter reservas após reiniciar.

**Entrega:** descrição técnica curta + resposta sobre persistência

**Critérios:** propósito claro; entrada/estado identificados; limite correto; sem inventar implementação.

**Se houver dificuldade:** use as perguntas ‘o que entra?’, ‘o que muda?’ e ‘o que se perde ao fechar?’.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** o aluno afirma que o laboratório tem API web

> Onde está o endpoint ou servidor executável? Se não existe evidência, descreva como proposta futura.

**Se aparecer:** o aluno chama perda de estado de bug sem considerar escopo

> O README promete persistência? Se não promete, trate como limitação de escopo, não automaticamente como defeito.

**Se aparecer:** o aluno tenta entender todo o código de uma vez

> Escolha uma entrada concreta e acompanhe apenas o caminho dessa operação.

### Perguntas de verificação

- **Um desenho de tela significa que a interface foi implementada?** — Não. É apenas uma proposta até existir código/execução correspondente.
- **Estado em memória é o mesmo que banco de dados?** — Não. Estado em memória normalmente desaparece ao encerrar o processo.
- **Como diferenciar observação de hipótese?** — Observação vem de arquivo/execução verificável; hipótese é uma possibilidade ainda não implementada ou confirmada.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Entender sistemas começa por separar comportamento observado, estado e limite. Isso evita falar de arquitetura como se fosse adivinhação.

**Tarefa para casa:**

1. Revisar o diagrama com feedback.
2. Adicionar dois limites e uma hipótese de evolução.
3. Entregar `m03-aula-01-revisao.md`.

**Entrega:** diagrama revisado + limites

**Ponte para a próxima aula:**

> Na próxima aula vocês vão ler código sem tentar decorar tudo e vão perceber que a mesma lógica pode aparecer com sintaxes diferentes.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
