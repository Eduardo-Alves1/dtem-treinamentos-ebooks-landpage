# Roteiro de Aula — Módulo 3, Aula 1

# Sistemas e Construção de Software

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-03-aula-01-sistemas-e-construcao.md).

## Objetivo da aula

Explicar como um sistema é formado por componentes que recebem entradas, aplicam regras, mantêm estado e produzem saídas, distinguindo o que existe no laboratório do que seria uma arquitetura futura.

Ao final, o aluno deverá conseguir:

- identificar entrada, regra, estado e saída em um sistema
- distinguir interface, lógica e persistência
- explicar limites do laboratório Agenda Clara
- desenhar componentes de uma solução sem inventar infraestrutura inexistente

## Conteúdos e conceitos

### Sistema e componentes
- entrada
- regra
- estado
- saída

### Interface, lógica e estado
- interface é interação
- lógica decide
- estado representa situação atual

### Persistência e limite
- memória durante a execução
- persistência entre execuções
- limite precisa ser declarado

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

- [E-book do Módulo 3](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- editor de código
- terminal

## Exemplos planejados

### Exemplo 1
Agenda Clara executando regras sem interface web.

### Exemplo 2
Aplicação futura com front-end chamando uma regra por API.

### Exemplo 3
Sistema que perde estado ao reiniciar por não ter persistência.

## Demonstração planejada — Mapear os componentes reais do laboratório

1. Ler o README.
2. Localizar entradas, regra e estado.
3. Executar uma reserva e observar a saída.
4. Reiniciar e verificar perda de estado.
5. Desenhar uma interface futura marcando-a como hipótese.

**Resultado pedagógico esperado:** o aluno separa o que está implementado do que é desenho futuro.

## Dinâmica em grupo — Anatomia do laboratório

**Cenário:** A dupla precisa explicar o Agenda Clara para uma pessoa que nunca viu o projeto.

1. Identificar entrada, regra, estado e saída.
2. Marcar o que existe no código.
3. Desenhar uma interface/API futura como hipótese.
4. Listar dois limites do laboratório.

**Entrega esperada:** diagrama anotado do sistema

**Critérios:** componentes reais separados de hipóteses; limites explícitos; relações coerentes.

## Exercício individual

Escreva uma descrição curta do Agenda Clara contendo propósito, entrada, comportamento principal, estado e um limite. Depois diga qual componente faltaria para manter reservas após reiniciar.

**Entrega:** descrição técnica curta + resposta sobre persistência

**Critérios:** propósito claro; entrada/estado identificados; limite correto; sem inventar implementação.

## Perguntas de verificação

- Um desenho de tela significa que a interface foi implementada?
- Estado em memória é o mesmo que banco de dados?
- Como diferenciar observação de hipótese?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar o diagrama com feedback.
2. Adicionar dois limites e uma hipótese de evolução.
3. Entregar `m03-aula-01-revisao.md`.

**Entrega:** diagrama revisado + limites

## Conexão com a trilha

A Aula 2 usa o mesmo laboratório para aprender a ler código a partir do comportamento e introduz uma comparação controlada com JavaScript/TypeScript.

## Referências

- [E-book correspondente](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-03-aula-01-sistemas-e-construcao.md)
