# Script do Professor — Kickoff, Escopo e Requisitos do Projeto Final

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar uma aula paralela.

**Roteiro:** [Módulo 8, Aula 1](../modulo-08-aula-01-kickoff-e-requisitos.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-08-projeto-final-hands-on.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Iniciar o projeto final definindo problema, escopo, limites, requisitos e histórias que servirão como base verificável para as próximas aulas.
- **Demonstração central:** Fechar escopo e revisar uma história.
- **Prática em grupo:** Acordar a entrega.
- **Exercício individual:** escrever uma decisão de escopo.
- **Tarefa:** revisar requisitos e jornada do projeto.

## Antes da aula

- [ ] Separar template do dossiê.
- [ ] Conferir regras/histórias fornecidas.
- [ ] Explicitar natureza educacional do projeto.
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

> Nosso projeto final não precisa parecer maior do que é. Ele precisa ser coerente, verificável e explicável. Hoje vamos fechar o que realmente será demonstrado.

**Pergunta diagnóstica:** O que vale mais para o portfólio: muitas funcionalidades incompletas ou um escopo pequeno que você consegue explicar e verificar?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** um escopo coerente, verificável e honestamente apresentado.

**Transição:**

> Vamos transformar tudo que aprendemos em um contrato claro de problema, escopo e critérios.

## 08–25 — Conceitos e exemplos

### 1. Kickoff e problema

**Fala sugerida:**

> Projeto final não começa com ‘vamos codar’. Começa com um acordo sobre qual problema educacional vamos simular e o que cada pessoa precisa produzir.

**Mostrar/fazer:** brief do Agenda Clara.

**Perguntar:** Que resultado educacional o projeto deve demonstrar?

**Compreensão esperada:** capacidade de conectar requisitos, execução, testes, decisões e comunicação.

### 2. Escopo e limites

**Fala sugerida:**

> Escopo pequeno e verificável é melhor que uma promessa de plataforma completa. Nosso laboratório é local, sequencial e educacional.

**Mostrar/fazer:** inclui consultar/reservar/cancelar; exclui autenticação/concorrência real/persistência.

**Perguntar:** O que não devemos apresentar como implementado?

**Compreensão esperada:** componentes fora do laboratório.

### 3. Requisitos e histórias

**Fala sugerida:**

> As histórias do projeto precisam conversar com regras e testes já trabalhados. Não queremos documentos soltos.

**Mostrar/fazer:** uma história e critérios ligados a RN.

**Perguntar:** Que critério garante preservação de reserva em conflito?

**Compreensão esperada:** tentativa ocupada retorna conflito e não altera reserva original.

## 25–45 — Demonstração guiada — Fechar escopo e revisar uma história

### Passo 1 — Acordar o problema

**Fazer:** Resuma a situação da recepção.

**Fala sugerida:**

> O projeto final é educacional: queremos mostrar como vocês pensam e conectam artefatos, não fingir uma implantação em cliente real.

**Checar com a turma:** Peça ao aluno para explicar o problema sem falar de tecnologia.

### Passo 2 — Delimitar MVP

**Fazer:** Monte tabela dentro/fora.

**Fala sugerida:**

> Tudo que fica fora precisa ser nomeado. Isso protege a apresentação de promessas que o laboratório não sustenta.

**Checar com a turma:** Pergunte se persistência e concorrência estão implementadas.

### Passo 3 — Revisar história

**Fazer:** Escolha história de conflito/cancelamento.

**Fala sugerida:**

> Vamos seguir a regra até o critério. Se não conseguirmos ligar os dois, há risco de construir e testar coisas diferentes.

**Checar com a turma:** Peça a referência da regra.

**Resultado de referência:** MVP educacional: consulta, reserva sequencial e cancelamento; sem autenticação, persistência, concorrência real ou operação de produção. Histórias/critérios devem mapear regras do caso.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Acordar a entrega

**Cenário:** A equipe precisa sair do kickoff com entendimento comum sobre o que será demonstrado no projeto final.

> Não usem ‘atuei como PO/QA em empresa’. Usem ‘no projeto educacional, produzi/revisei...’.

1. Escrever problema em uma frase.
2. Definir três itens dentro e três fora do escopo.
3. Revisar três histórias e critérios.
4. Registrar uma decisão e uma dúvida.
5. Distribuir responsabilidade de documentação/revisão, sem simular cargos reais.

**Entrega:** kickoff.md + escopo + histórias revisadas

**Observar:** problema claro; limites honestos; rastreabilidade inicial; contribuição identificada.

## 65–77 — Exercício individual

> Escolha um pedido fora do MVP — por exemplo, pagamento ou login — e escreva por que não entra agora, o que precisaria ser investigado e como registrar isso no backlog futuro.

**Entrega:** decisão de escopo individual

**Critérios:** razão coerente; investigação futura; sem estimativa inventada; distinção entre atual e futuro.

**Ajuda graduada:** use ‘pedido / benefício esperado / lacunas de informação / decisão atual’.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** o aluno adiciona login/pagamento sem revisar escopo

> Que problema e requisitos novos isso introduz? Registre como hipótese/backlog futuro antes de prometer implementação.

**Se aparecer:** o aluno descreve atividade educacional como trabalho em cliente

> Mantenha a natureza do projeto explícita. Evidência educacional é válida sem inventar experiência contratada.

**Se aparecer:** história sem regra/critério

> Qual comportamento do caso sustenta esta história? Adicione vínculo verificável.

### Perguntas de verificação

- **Projeto final precisa implementar uma aplicação web completa?** — Não. O objetivo é integrar os artefatos previstos e demonstrar raciocínio verificável dentro do escopo.
- **Podemos chamar a simulação de experiência profissional?** — Não. Deve ser apresentada como projeto educacional.
- **Fora de escopo significa ‘nunca será feito’?** — Não. Significa que não faz parte da entrega atual; pode virar backlog futuro após investigação.

## 85–90 — Fechamento e tarefa

> Um projeto forte começa por saber dizer tanto o que ele entrega quanto o que não entrega.

1. Revisar kickoff e escopo.
2. Concluir três histórias com critérios.
3. Atualizar matriz de rastreabilidade.
4. Registrar contribuição individual.
5. Entregar `m08-aula-01-revisao.md`.

**Entrega:** primeiro bloco do dossiê

**Ponte:**

> Na próxima aula o plano encontra a realidade: vamos organizar uma rodada de execução, registrar bloqueios e preservar a Definition of Done.

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
