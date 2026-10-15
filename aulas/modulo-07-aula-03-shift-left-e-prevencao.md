# Roteiro de Aula — Módulo 7, Aula 3

# Shift Left e Prevenção

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-07-aula-03-shift-left-e-prevencao.md).

## Objetivo da aula

Aplicar Shift Left como antecipação de qualidade, refinando regras e exemplos antes da implementação sem abandonar verificações posteriores.

Ao final, o aluno deverá conseguir:

- explicar Shift Left sem reduzi-lo a ‘testar cedo’
- identificar ambiguidades antes do código
- produzir critérios observáveis
- mostrar colaboração Produto–Dev–QA
- manter plano de verificação após a implementação

## Conteúdos e conceitos

### Shift Left como antecipação
- qualidade discutida cedo
- risco e testabilidade
- não elimina teste posterior

### Exemplos e critérios
- exemplo concreto reduz interpretação
- positivo/negativo
- estado também importa

### Três perspectivas
- Produto: valor/regra
- Dev: implementação/viabilidade
- QA: risco/exemplos

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

- E-book do Módulo 7
- regras Agenda Clara
- quadro de refinamento

## Exemplos planejados

### Exemplo 1
Nome obrigatório e espaços.

### Exemplo 2
Cancelamento ‘simples’ sem regra de ID.

### Exemplo 3
Conflito de horário discutido antes da implementação.

## Demonstração planejada — Refinar ‘nome obrigatório’ antes do código

1. Apresentar a frase vaga.
2. Pedir perguntas de Produto, Dev e QA.
3. Criar exemplos válidos e inválidos.
4. Definir comportamento do estado.
5. Transformar em critério verificável.
6. Planejar como testar depois.

**Resultado pedagógico esperado:** o aluno vê prevenção e verificação como partes complementares.

## Dinâmica em grupo — Três perspectivas

**Cenário:** Cada trio recebe uma regra curta e distribui Produto, Dev e QA para refiná-la.

1. Produto explica objetivo e contexto.
2. Dev aponta decisão/limitação técnica a esclarecer.
3. QA propõe riscos e exemplos.
4. O trio escreve critérios verificáveis.
5. Trocar regra com outro trio para revisão.

**Entrega esperada:** regra refinada + exemplos

**Critérios:** perspectivas distintas; ambiguidade reduzida; critério verificável; teste posterior previsto.

## Exercício individual

A frase ‘o usuário pode cancelar uma reserva’ é vaga. Escreva duas perguntas de esclarecimento e dois critérios verificáveis, incluindo um cenário de ID inexistente.

**Entrega:** perguntas + critérios

**Critérios:** ambiguidades reais; positivo/negativo; estado esperado; sem inventar autorização não definida.

## Perguntas de verificação

- Shift Left elimina necessidade de testes depois do código?
- QA deve ser dono de todos os critérios?
- Perguntar cedo garante que nenhum bug ocorrerá?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Escolher uma regra do projeto.
2. Registrar pergunta antes da solução.
3. Criar exemplos positivos e negativos.
4. Definir evidência futura.
5. Entregar `m07-aula-03-revisao.md`.

**Entrega:** regra refinada + exemplos + plano de verificação

## Conexão com a trilha

A Aula 4 fecha o módulo com release, operação, critérios de liberação e resposta a falhas.

## Referências

- [E-book correspondente](../ebooks/modulo-07-ciclo-de-vida-do-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-07-aula-03-shift-left-e-prevencao.md)
