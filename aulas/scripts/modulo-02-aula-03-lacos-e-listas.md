# Script do Professor — Laços e Listas

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 2, Aula 3](../modulo-02-aula-03-lacos-e-listas.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-02-logica-de-programacao.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  

## Alinhamento obrigatório

- **Objetivo:** Usar listas e estruturas de repetição para percorrer dados, filtrar horários e compreender condição de parada.
- **Demonstração central:** Filtrar horários livres e controlar tentativas.
- **Prática em grupo:** Rastreie o filtro.
- **Exercício individual:** resolver um filtro novo e explicar um contador.
- **Tarefa:** revisar os laços e criar um caso novo.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Preparar duas tabelas de rastreamento.
- [ ] Confirmar editor Python.
- [ ] Ter um exemplo de lista vazia pronto.
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

> Se o catálogo tiver cem horários, faz sentido escrever cem verificações separadas? Hoje vamos aprender a repetir uma operação sem perder controle sobre cada decisão.

**Pergunta diagnóstica:** O que aconteceria com um `while` se a variável usada na condição nunca mudasse?

Dê cerca de dois minutos para respostas curtas no chat, voz ou caderno. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** A condição pode permanecer verdadeira e causar repetição indefinida.

**Transição:**

> Vamos começar com uma coleção pequena e acompanhar cada passagem antes de deixar o computador executar por nós.

## 08–25 — Conceitos e exemplos

### 1. Listas e coleções

**Fala sugerida:**

> Uma lista nos permite representar vários valores relacionados. Se não houver horários livres, uma lista vazia pode ser exatamente o resultado correto.

**Mostrar/fazer:** `['H09','H10','H11']` e `[]`.

**Perguntar:** Lista vazia significa erro?

**Compreensão esperada:** Não necessariamente; pode significar que nenhum item atende ao filtro.

### 2. `for` e rastreamento

**Fala sugerida:**

> O `for` percorre cada elemento. Para filtrar horários, decidimos em cada passagem se o item entra na lista de livres.

**Mostrar/fazer:** tabela item/ocupado?/livres.

**Perguntar:** Quantas passagens teremos com três horários?

**Compreensão esperada:** três, uma por item.

### 3. `while` e progresso

**Fala sugerida:**

> No `while`, nós controlamos a condição de parada. Se nada muda, a repetição pode nunca terminar.

**Mostrar/fazer:** contador de 0 até 3.

**Perguntar:** O que acontece se esquecermos o incremento?

**Compreensão esperada:** a condição pode permanecer verdadeira indefinidamente.

Evite transformar este bloco em leitura do E-book. Use o E-book como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Filtrar horários livres e controlar tentativas

### Passo 1 — Rastrear o `for`

**Fazer:** Monte tabela com H09, H10 e H11.

**Fala sugerida:**

> Não vamos saltar direto para a saída. Vamos observar cada passagem e como a lista `livres` muda.

**Checar com a turma:** Peça a lista após cada item.

### Passo 2 — Testar lista vazia

**Fazer:** Marque todos os horários como ocupados.

**Fala sugerida:**

> Zero resultados também é um resultado. O importante é diferenciar ‘nenhum item atende’ de ‘o código falhou’.

**Checar com a turma:** Pergunte se o `for` com catálogo vazio executa alguma passagem.

### Passo 3 — Rastrear o `while`

**Fazer:** Use contador 0, condição `< 3` e incremento.

**Fala sugerida:**

> Aqui a pergunta principal é: o que muda a cada passagem para nos aproximar da parada?

**Checar com a turma:** Remova o incremento e peça previsão.

**Resultado de referência:** Com H10 ocupado, livres = [H09, H11]. Com todos ocupados, livres = []. Um contador 0 enquanto <3, incrementando 1, executa três vezes.

Antes de mostrar o resultado, peça uma previsão. Depois compare previsão, comportamento observado e explicação.

## 45–50 — Pausa

Informar claramente o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Rastreie o filtro

**Cenário:** Cada dupla recebe um conjunto de horários e ocupações diferente.

**Orientação para a turma:**

> Não aceitem apenas a lista final. O objetivo é mostrar como ela foi construída.

1. Rastrear o filtro item a item.
2. Registrar a lista parcial após cada passo.
3. Trocar o conjunto com outra dupla para revisão.
4. Explicar o comportamento se a coleção estiver vazia.

**Tempo sugerido:** 2 min para organização, 8 min para produção, 3 min para revisão entre pares e 2 min para compartilhamento.

**Entrega esperada:** tabela de rastreamento do filtro

**O professor observa:** uma linha por passagem; lista parcial correta; lista vazia interpretada corretamente; revisão feita por outra pessoa.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Use H09/H10/H11 com H11 ocupado. Registre a lista final e uma tabela de passagens. Depois explique quantas vezes executa um contador iniciado em 0 enquanto menor que 2, incrementando 1.

**Entrega:** rastreamento individual de `for` e `while`

**Critérios:** lista correta; passagens visíveis; condição de parada explicada.

**Se houver dificuldade:** dê a primeira linha da tabela e peça que o aluno repita o padrão.

## 77–85 — Correção, intervenções e dúvidas

Comece pedindo que o aluno explique como chegou à resposta antes de mostrar uma referência.

**Se aparecer:** o aluno inclui um horário ocupado na lista final

> Em qual passagem essa decisão aconteceu? Volte à condição daquele item.

**Se aparecer:** o aluno considera lista vazia como erro automático

> A regra pede pelo menos um resultado ou apenas os itens que atendem ao filtro? Se nenhum atende, `[]` pode estar correto.

**Se aparecer:** o aluno prevê uma passagem extra no `while`

> A condição é verificada antes de entrar no corpo. Quando o contador chega a 2, `2 < 2` é verdadeiro ou falso?

### Perguntas de verificação

- **O que acontece quando a lista de entrada está vazia?** — O `for` executa zero passagens; isso pode ser comportamento normal.
- **O que torna um `while` perigoso?** — Uma condição que nunca se torna falsa, normalmente porque o estado de controle não muda.
- **Por que rastrear antes de executar ajuda?** — Permite prever comportamento e localizar em qual passagem o raciocínio diverge.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Laços economizam repetição de código, mas só são seguros quando entendemos o que acontece em cada passagem e como a repetição termina.

**Tarefa para casa:**

1. Revisar o filtro e o contador.
2. Criar um conjunto diferente de horários.
3. Prever a saída antes de executar.
4. Entregar `m02-aula-03-revisao.md` com previsão, resultado e explicação.

**Entrega:** rastreamento revisado + novo caso executado

**Ponte para a próxima aula:**

> Na próxima aula vamos dar responsabilidades claras a funções e aprender a investigar quando o resultado não bate com a regra.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se a atividade usada foi a mesma definida no roteiro.
- [ ] Anotar qualquer ajuste de tempo para a próxima turma.
- [ ] Não alterar critérios ou respostas de referência apenas na fala; se a regra mudar, atualizar roteiro e script juntos.
