# Roteiro de Aula — Módulo 5, Aula 3

# User Stories e Critérios de Aceite

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-05-aula-03-historias-e-criterios.md).

## Objetivo da aula

Transformar necessidades em User Stories compreensíveis e critérios de aceite positivos e negativos que possam ser discutidos e testados.

Ao final, o aluno deverá conseguir:

- escrever história com usuário, necessidade e valor
- evitar histórias tautológicas
- criar critérios observáveis
- relacionar critérios a regras e testes
- identificar dependências e perguntas em aberto

## Conteúdos e conceitos

### História como conversa
- quem
- o que
- por quê
- não substitui refinamento

### Critério de aceite
- comportamento observável
- positivo e negativo
- estado importante

### Conexão Produto–Dev–QA
- Produto esclarece valor/regra
- Dev discute solução
- QA ajuda com exemplos/riscos

## Duração e blocos

| Bloco | Tempo previsto |
|---|---:|
| Abertura e diagnóstico | 8 min |
| Conceitos e exemplos | 17 min |
| Demonstração guiada | 20 min |
| Pausa | 5 min |
| Dinâmica em dupla ou grupo | 15 min |
| Exercício individual | 12 min |
| Correção e dúvidas | 8 min |
| Fechamento e tarefa | 5 min |
| **Total** | **90 min** |

## Materiais necessários

- E-book do Módulo 5
- caso Agenda Clara
- template de User Story e critérios

## Exemplos planejados

### Exemplo 1
US de cancelamento.

### Exemplo 2
Critério de conflito H09 ocupado.

### Exemplo 3
Critério para ID inexistente.

## Demonstração planejada — Escrever US03 e derivar critérios

1. Definir persona/usuário.
2. Escrever necessidade e valor.
3. Relacionar RN06/RN07.
4. Criar critério positivo de cancelamento.
5. Criar critério negativo de ID inexistente.
6. Derivar um caso de teste.

**Resultado pedagógico esperado:** o aluno conecta história, regra, critério e teste.

## Dinâmica em grupo — Conversa e confirmação

**Cenário:** Cada dupla recebe uma necessidade do Agenda Clara e deve produzir história + critérios que outra dupla consiga desafiar.

1. Escrever User Story.
2. Criar um critério positivo.
3. Criar um critério negativo.
4. Trocar com outra dupla e levantar uma pergunta/ambiguidade.

**Entrega esperada:** história + critérios revisados

**Critérios:** valor explícito; critérios observáveis; positivo e negativo; pergunta de refinamento.

## Exercício individual

Escreva um critério para H09 já ocupado por Ana quando Bruno tenta reservar. Inclua retorno esperado e o que não pode mudar. Depois derive um caso de teste curto.

**Entrega:** critério + caso de teste

**Critérios:** regra correta; estado preservado; dados concretos; teste deriva do critério.

## Perguntas de verificação

- User Story substitui requisito detalhado?
- Critério ‘funcionar corretamente’ é suficiente?
- Critério deve cobrir só cenário feliz?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar as histórias.
2. Adicionar pelo menos um critério negativo em cada conjunto relevante.
3. Registrar uma pergunta de refinamento.
4. Entregar `m05-aula-03-revisao.md`.

**Entrega:** histórias e critérios revisados

## Conexão com a trilha

A Aula 4 organiza as histórias em backlog, prioridade, dependências e decisões de refinamento.

## Referências

- [E-book correspondente](../ebooks/modulo-05-product-owner-e-produto.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Script do professor](scripts/modulo-05-aula-03-historias-e-criterios.md)
