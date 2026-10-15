# Roteiro de Aula — Módulo 7, Aula 1

# SDLC e Integração entre Áreas

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-07-aula-01-sdlc-e-integracao.md).

## Objetivo da aula

Conectar Produto, Desenvolvimento, QA, Dados, Infraestrutura e Gestão ao longo do ciclo de vida do software, mostrando que o SDLC possui feedback e não é uma linha rígida.

Ao final, o aluno deverá conseguir:

- desenhar um SDLC básico com feedback
- relacionar áreas e artefatos às etapas
- identificar contribuição de QA antes, durante e depois da construção
- diferenciar etapa de atividade isolada
- explicar limites entre laboratório educacional e operação real

## Conteúdos e conceitos

### SDLC como ciclo
- necessidade e descoberta
- requisitos e planejamento
- construção e verificação
- release/operação
- feedback

### Integração entre áreas
- Produto esclarece valor
- Dev constrói
- QA antecipa e verifica riscos
- Dados/Infra apoiam observação e operação

### Artefatos e evidências
- brief/história
- código/commit
- caso/bug
- release/checklist
- feedback

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
- artefatos de Produto, QA e Gestão dos módulos anteriores
- quadro para diagrama SDLC

## Exemplos planejados

### Exemplo 1
Reclamação da recepção voltando a requisito.

### Exemplo 2
BUG01 levando a correção e reteste.

### Exemplo 3
Feedback de uso alimentando nova priorização.

## Demonstração planejada — Construir o ciclo completo do Agenda Clara

1. Começar pelo problema da recepção.
2. Adicionar requisito/história.
3. Adicionar desenvolvimento e versionamento.
4. Adicionar verificação e decisão de release.
5. Adicionar uso/feedback.
6. Marcar onde Produto, QA, Dev, Dados, Infra e Gestão contribuem.

**Resultado pedagógico esperado:** o aluno visualiza um ciclo integrado e iterativo.

## Dinâmica em grupo — Conectar áreas

**Cenário:** A equipe recebe uma reclamação pós-entrega e precisa mostrar por onde a informação passa até virar uma melhoria verificada.

1. Desenhar o ciclo da reclamação até nova decisão.
2. Marcar pelo menos quatro áreas participantes.
3. Associar um artefato a cada passagem relevante.
4. Incluir um ponto em que o fluxo pode voltar para trás.

**Entrega esperada:** diagrama SDLC anotado

**Critérios:** ciclo com feedback; áreas distribuídas sem silos rígidos; artefatos coerentes; retorno/iteração explícito.

## Exercício individual

Uma pessoa da recepção relata que o cancelamento está confuso. Descreva quais artefatos ou decisões você revisaria antes de mudar código e como verificaria a mudança depois.

**Entrega:** sequência curta de impacto no SDLC

**Critérios:** feedback ligado a requisito; revisão antes do código; verificação posterior; áreas relacionadas.

## Perguntas de verificação

- SDLC é sempre uma sequência fixa e linear?
- QA começa somente depois do desenvolvimento?
- Deploy significa fim do ciclo?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar o diagrama SDLC.
2. Adicionar pelo menos uma contribuição antecipada de QA.
3. Adicionar feedback pós-entrega.
4. Registrar o que é simulação no laboratório.
5. Entregar `m07-aula-01-revisao.md`.

**Entrega:** diagrama SDLC revisado

## Conexão com a trilha

A Aula 2 aprofunda rastreabilidade e análise de impacto entre regra, história, teste, bug e versão.

## Referências

- [E-book correspondente](../ebooks/modulo-07-ciclo-de-vida-do-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-07-aula-01-sdlc-e-integracao.md)
