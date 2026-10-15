# Script do Professor — User Stories e Critérios de Aceite

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar outra aula paralela.

**Roteiro:** [Módulo 5, Aula 3](../modulo-05-aula-03-historias-e-criterios.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-05-product-owner-e-produto.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  

## Alinhamento obrigatório

- **Objetivo:** Transformar necessidades em User Stories compreensíveis e critérios de aceite positivos e negativos que possam ser discutidos e testados.
- **Demonstração central:** Escrever US03 e derivar critérios.
- **Prática em grupo:** Conversa e confirmação.
- **Exercício individual:** criar critério de conflito e caso derivado.
- **Tarefa:** revisar três histórias e critérios com olhar de QA/Dev.

## Antes da aula

- [ ] Separar template de User Story.
- [ ] Revisar RN05–RN07.
- [ ] Preparar exemplo de critério ruim ‘funcionar corretamente’.
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

> ‘Como usuário, quero cancelar para poder cancelar’ parece uma história, mas explica muito pouco. Hoje vamos aprender a escrever valor e comportamento de forma que o time consiga conversar.

**Pergunta diagnóstica:** O que falta em uma história que descreve apenas a ação?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** contexto/benefício e critérios que expliquem comportamento.

**Transição:**

> Vamos começar pela intenção e depois transformar essa intenção em exemplos verificáveis.

## 08–25 — Conceitos e exemplos

### 1. História como conversa

**Fala sugerida:**

> A frase da User Story é um convite para conversa, não uma especificação completa. O valor precisa fazer sentido para a pessoa que usa ou para o negócio.

**Mostrar/fazer:** história de cancelamento bem e mal escrita.

**Perguntar:** ‘Quero cancelar para cancelar’ explica valor?

**Compreensão esperada:** não; falta benefício/contexto.

### 2. Critério de aceite

**Fala sugerida:**

> Critério bom permite que pessoas diferentes imaginem o mesmo comportamento. Ele evita ‘funcionar corretamente’ sem definição.

**Mostrar/fazer:** Dado/Quando/Então de conflito.

**Perguntar:** Além de retornar conflito, o que não pode mudar?

**Compreensão esperada:** reserva original.

### 3. Conexão Produto–Dev–QA

**Fala sugerida:**

> Critério não pertence a uma única área. É um ponto de alinhamento para construir e verificar a mesma intenção.

**Mostrar/fazer:** critério → caso de teste.

**Perguntar:** Que pergunta QA faria antes de implementar?

**Compreensão esperada:** cenários de erro/estado/limites.

## 25–45 — Demonstração guiada — Escrever US03 e derivar critérios

### Passo 1 — Escrever história com valor

**Fazer:** Monte ‘Como recepcionista...’.

**Fala sugerida:**

> Se o motivo puder ser removido sem mudar nada, talvez a história esteja descrevendo só uma ação, não o valor.

**Checar com a turma:** Peça uma versão melhor do ‘para quê’.

### Passo 2 — Criar critérios

**Fazer:** Escreva positivo e negativo.

**Fala sugerida:**

> Vamos incluir o que deve acontecer e o que deve permanecer igual. Estado faz parte do comportamento.

**Checar com a turma:** Pergunte o esperado para ID inexistente.

### Passo 3 — Derivar teste

**Fazer:** Transforme critério de conflito em caso.

**Fala sugerida:**

> Critério e teste não são a mesma coisa, mas um bom critério facilita criar testes relevantes.

**Checar com a turma:** Peça dados concretos para H09/Ana/Bruno.

**Resultado de referência:** US03: recepcionista cancela reserva ativa para liberar horário. Critérios cobrem cancelamento válido e ID inexistente; conflito preserva reserva original quando aplicado.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Conversa e confirmação

**Cenário:** Cada dupla recebe uma necessidade do Agenda Clara e deve produzir história + critérios que outra dupla consiga desafiar.

> A dupla revisora não deve corrigir estilo; deve procurar comportamento ambíguo ou ausente.

1. Escrever User Story.
2. Criar um critério positivo.
3. Criar um critério negativo.
4. Trocar com outra dupla e levantar uma pergunta/ambiguidade.

**Entrega:** história + critérios revisados

**Observar:** valor explícito; critérios observáveis; positivo e negativo; pergunta de refinamento.

## 65–77 — Exercício individual

> Escreva um critério para H09 já ocupado por Ana quando Bruno tenta reservar. Inclua retorno esperado e o que não pode mudar. Depois derive um caso de teste curto.

**Entrega:** critério + caso de teste

**Critérios:** regra correta; estado preservado; dados concretos; teste deriva do critério.

**Ajuda graduada:** comece por Dado/Quando/Então e só depois transforme em passos.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** história sem valor

> Para que a pessoa quer isso? O benefício precisa fazer sentido no contexto.

**Se aparecer:** critério descreve implementação

> Isso é comportamento esperado ou decisão técnica? Tente escrever o que o usuário/sistema observa.

**Se aparecer:** critério negativo esquece estado

> Depois da recusa, o que deve permanecer igual? Escreva isso explicitamente.

### Perguntas de verificação

- **User Story substitui requisito detalhado?** — Não. É um artefato de comunicação que precisa de conversa, critérios e contexto.
- **Critério ‘funcionar corretamente’ é suficiente?** — Não. Precisa descrever comportamento observável.
- **Critério deve cobrir só cenário feliz?** — Não. Cenários negativos e limites relevantes também precisam ser discutidos.

## 85–90 — Fechamento e tarefa

> Histórias não são formulários burocráticos. Elas funcionam quando ajudam pessoas diferentes a discutir a mesma necessidade com menos ambiguidade.

1. Revisar as histórias.
2. Adicionar pelo menos um critério negativo em cada conjunto relevante.
3. Registrar uma pergunta de refinamento.
4. Entregar `m05-aula-03-revisao.md`.

**Entrega:** histórias e critérios revisados

**Ponte:**

> Na próxima aula vamos sair de ‘o que poderia ser feito’ para ‘o que faz sentido fazer primeiro e por quê’.

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
