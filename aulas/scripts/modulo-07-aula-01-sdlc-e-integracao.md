# Script do Professor — SDLC e Integração entre Áreas

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar uma aula paralela.

**Roteiro:** [Módulo 7, Aula 1](../modulo-07-aula-01-sdlc-e-integracao.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-07-ciclo-de-vida-do-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Conectar Produto, Desenvolvimento, QA, Dados, Infraestrutura e Gestão ao longo do ciclo de vida do software, mostrando que o SDLC possui feedback e não é uma linha rígida.
- **Demonstração central:** Construir o ciclo completo do Agenda Clara.
- **Prática em grupo:** Conectar áreas.
- **Exercício individual:** transformar feedback em nova passagem pelo ciclo.
- **Tarefa:** revisar o diagrama com áreas, artefatos e limites.

## Antes da aula

- [ ] Separar artefatos reais do curso para mostrar conexões.
- [ ] Preparar um diagrama SDLC vazio.
- [ ] Reforçar diferença entre release simulada e produção real.
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

> Até aqui estudamos Produto, Dev, QA e organização do trabalho em módulos separados. Hoje vamos juntar as peças e seguir uma necessidade desde o problema até o feedback.

**Pergunta diagnóstica:** Em que momento do ciclo a qualidade começa a ser discutida?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** Desde o entendimento do problema e dos requisitos; não apenas na execução de testes.

**Transição:**

> Vamos construir um ciclo que tenha pessoas, artefatos e retorno de informação, e não apenas caixas em sequência.

## 08–25 — Conceitos e exemplos

### 1. SDLC como ciclo

**Fala sugerida:**

> O ciclo de vida não é uma esteira que nunca volta. Informação nova pode fazer o time revisar requisito, código, teste ou prioridade.

**Mostrar/fazer:** fluxo com seta de feedback voltando ao início.

**Perguntar:** Que tipo de informação pode fazer o time voltar a um requisito?

**Compreensão esperada:** feedback, defeito, métrica, mudança de regra ou restrição técnica.

### 2. Integração entre áreas

**Fala sugerida:**

> As áreas participam em momentos diferentes, mas várias contribuições acontecem em paralelo. QA não nasce na etapa chamada ‘teste’.

**Mostrar/fazer:** marque contribuições sobre o fluxo.

**Perguntar:** Onde QA pode contribuir antes do código?

**Compreensão esperada:** exemplos, critérios, riscos e revisão de requisitos.

### 3. Artefatos e evidências

**Fala sugerida:**

> O ciclo fica mais compreensível quando conseguimos ligar cada decisão a um artefato ou evidência.

**Mostrar/fazer:** artefatos dos módulos 4–6.

**Perguntar:** Qual artefato ajuda a explicar por que um comportamento foi testado?

**Compreensão esperada:** regra/história/critério ligado ao caso.

## 25–45 — Demonstração guiada — Construir o ciclo completo do Agenda Clara

### Passo 1 — Partir da necessidade

**Fazer:** Escreva o problema e uma história relacionada.

**Fala sugerida:**

> SDLC começa antes do código. Se não entendemos o problema, todo o restante pode estar tecnicamente correto e ainda resolver a coisa errada.

**Checar com a turma:** Peça um artefato produzido antes da implementação.

### Passo 2 — Conectar construção e qualidade

**Fazer:** Adicione código, teste e bug.

**Fala sugerida:**

> QA aparece antes e depois da construção: ajuda a discutir exemplos e depois produz evidências sobre o comportamento implementado.

**Checar com a turma:** Pergunte qual vínculo existe entre critério, caso e defeito.

### Passo 3 — Fechar o ciclo com feedback

**Fazer:** Adicione release, uso e seta de retorno.

**Fala sugerida:**

> A entrega em produção ou numa demonstração não encerra aprendizado. O resultado observado pode exigir nova decisão.

**Checar com a turma:** Peça um exemplo de feedback que mudaria backlog ou requisito.

**Resultado de referência:** Fluxo possível: problema → descoberta/requisito → planejamento → implementação/versionamento → verificação → release → uso/observação → feedback → nova decisão. As atividades podem se sobrepor.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Conectar áreas

**Cenário:** A equipe recebe uma reclamação pós-entrega e precisa mostrar por onde a informação passa até virar uma melhoria verificada.

> Evitem desenhar QA como uma caixa isolada depois de Dev. Mostrem contribuições antes e depois da construção.

1. Desenhar o ciclo da reclamação até nova decisão.
2. Marcar pelo menos quatro áreas participantes.
3. Associar um artefato a cada passagem relevante.
4. Incluir um ponto em que o fluxo pode voltar para trás.

**Entrega:** diagrama SDLC anotado

**Observar:** ciclo com feedback; áreas distribuídas sem silos rígidos; artefatos coerentes; retorno/iteração explícito.

## 65–77 — Exercício individual

> Uma pessoa da recepção relata que o cancelamento está confuso. Descreva quais artefatos ou decisões você revisaria antes de mudar código e como verificaria a mudança depois.

**Entrega:** sequência curta de impacto no SDLC

**Critérios:** feedback ligado a requisito; revisão antes do código; verificação posterior; áreas relacionadas.

**Ajuda graduada:** use a pergunta ‘o que precisa ser entendido, alterado e verificado?’.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** o aluno desenha QA apenas entre Dev e deploy

> Que pergunta de qualidade poderia ser feita quando o requisito ainda está sendo definido? Inclua essa contribuição antes.

**Se aparecer:** o aluno usa ‘produção’ para o laboratório local

> Nosso laboratório simula comportamento local. Não chame isso de produção ou deploy real sem infraestrutura correspondente.

**Se aparecer:** o aluno descreve ciclo sem feedback

> O que acontece quando usuário, suporte ou dados mostram algo inesperado? Desenhe o retorno.

### Perguntas de verificação

- **SDLC é sempre uma sequência fixa e linear?** — Não. Modelos variam e feedback pode levar a revisões de etapas anteriores.
- **QA começa somente depois do desenvolvimento?** — Não. Pode contribuir com critérios, exemplos, risco e testabilidade antes do código.
- **Deploy significa fim do ciclo?** — Não. Operação, monitoramento, feedback e evolução continuam.

## 85–90 — Fechamento e tarefa

> O valor do SDLC está em enxergar dependências e feedback. Quando uma informação muda, conseguimos descobrir quais decisões precisam ser revisitadas.

1. Revisar o diagrama SDLC.
2. Adicionar pelo menos uma contribuição antecipada de QA.
3. Adicionar feedback pós-entrega.
4. Registrar o que é simulação no laboratório.
5. Entregar `m07-aula-01-revisao.md`.

**Entrega:** diagrama SDLC revisado

**Ponte:**

> Na próxima aula vamos transformar essas conexões em vínculos concretos para responder: se uma regra mudar, o que precisa ser revisado?

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
