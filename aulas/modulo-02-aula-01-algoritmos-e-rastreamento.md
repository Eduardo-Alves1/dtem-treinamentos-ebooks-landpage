# Roteiro de Aula — Módulo 2, Aula 1

# Algoritmos e Rastreamento

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-02-aula-01-algoritmos-e-rastreamento.md).

## Objetivo da aula

Ensinar o aluno a descrever um algoritmo e rastrear manualmente entradas, decisões, saídas e estado antes de escrever código.

Ao final, o aluno deverá conseguir:

- identificar entrada, processamento, saída e estado
- escrever algoritmo em linguagem natural/pseudocódigo
- rastrear tentativas válidas e recusadas
- explicar por que uma recusa não deve corromper o estado anterior

## Conteúdos e conceitos

### Algoritmo
- sequência finita de passos
- entradas e saídas
- ordem e decisões

### Rastreamento manual
- seguir passo a passo
- anotar estado
- comparar previsto e observado

### Falha sem corrupção de estado
- recusa tem saída
- estado anterior deve permanecer
- ordem de validação importa

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

- [E-book do Módulo 2](../ebooks/modulo-02-logica-de-programacao.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- quadro ou tabela de rastreamento
- papel ou editor Markdown

## Exemplos planejados

### Exemplo 1
Reserva de horário no Agenda Clara.

### Exemplo 2
Fluxo de compra que valida antes de confirmar.

### Exemplo 3
Login que rejeita entrada inválida sem criar sessão.

## Demonstração planejada — Algoritmo de reserva sem código

1. Ler RN01–RN05 e RN08.
2. Definir entradas e verificações.
3. Rastrear Ana/H09 em agenda vazia.
4. Rastrear Bruno/H09 na mesma agenda.
5. Registrar o estado após cada tentativa.

**Resultado pedagógico esperado:** o aluno consegue explicar sucesso, conflito e preservação do estado.

## Dinâmica em grupo — Rastreamento cruzado de reservas

**Cenário:** Agenda inicialmente vazia com H09, H10 e H11 disponíveis.

1. Rastrear Lia/H10.
2. Rastrear Rui/H10 na mesma agenda.
3. Trocar papéis de autor e revisor.
4. Avaliar nome somente com espaços/H11 e justificar a saída.

**Entrega esperada:** tabela de rastreamento com estado após cada tentativa

**Critérios:** ordem de validação explícita; saída coerente; estado preservado; revisão entre pares.

## Exercício individual

Em nova agenda, H10 está ocupado por Carla e H09/H11 estão livres. Rastreie Rui/H10, nome somente com espaços/H09 e Dani/H11, nessa ordem. Para cada tentativa, registre o passo decisivo, a saída e o estado final.

**Entrega:** rastreamento individual das três tentativas

**Critérios:** decisão correta; estado coerente; explicação de uma aprovação e uma recusa.

## Perguntas de verificação

- Se a segunda tentativa falhar, por que o estado anterior deve permanecer?
- Algoritmo precisa estar em Python?
- O que muda entre duas execuções com as mesmas entradas quando o estado é diferente?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar a atividade com o feedback.
2. Adicionar um caso novo de sucesso ou recusa.
3. Registrar o que mudou entre a primeira e a segunda versão.
4. Entregar `m02-aula-01-revisao.md`.

**Entrega:** algoritmo e rastreamento revisados

## Conexão com a trilha

A Aula 2 transforma informações em variáveis/tipos e decisões condicionais.

## Referências

- [E-book correspondente](../ebooks/modulo-02-logica-de-programacao.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Script do professor](scripts/modulo-02-aula-01-algoritmos-e-rastreamento.md)
