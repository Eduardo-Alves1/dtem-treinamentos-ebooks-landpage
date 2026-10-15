# Roteiro de Aula — Módulo 2, Aula 3

# Laços e Listas

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-02-aula-03-lacos-e-listas.md).

## Objetivo da aula

Usar listas e estruturas de repetição para percorrer dados, filtrar horários e compreender condição de parada.

Ao final, o aluno deverá conseguir:

- explicar o papel de uma lista
- rastrear um `for` item a item
- explicar condição de parada de um `while`
- prever comportamento de lista vazia
- produzir um filtro simples de horários livres em Python

## Conteúdos e conceitos

### Listas e coleções
- sequência de valores
- ordem e conteúdo
- lista vazia é um estado válido

### `for` e rastreamento
- um item por passagem
- condição dentro do laço
- acumular resultado

### `while` e progresso
- repete enquanto condição é verdadeira
- estado precisa mudar
- risco de loop infinito

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
- editor/REPL Python
- tabela de rastreamento

## Exemplos planejados

### Exemplo 1
Filtrar horários livres.

### Exemplo 2
Percorrer produtos de carrinho.

### Exemplo 3
Limitar tentativas com contador.

## Demonstração planejada — Filtrar horários livres e controlar tentativas

1. Usar catálogo H09/H10/H11 e H10 ocupado.
2. Rastrear o `for` item a item.
3. Repetir com todos ocupados.
4. Criar um `while` de três tentativas.
5. Remover mentalmente o incremento e discutir o efeito.

**Resultado pedagógico esperado:** o aluno consegue prever lista final e explicar por que o laço termina.

## Dinâmica em grupo — Rastreie o filtro

**Cenário:** Cada dupla recebe um conjunto de horários e ocupações diferente.

1. Rastrear o filtro item a item.
2. Registrar a lista parcial após cada passo.
3. Trocar o conjunto com outra dupla para revisão.
4. Explicar o comportamento se a coleção estiver vazia.

**Entrega esperada:** tabela de rastreamento do filtro

**Critérios:** uma linha por passagem; lista parcial correta; lista vazia interpretada corretamente; revisão feita por outra pessoa.

## Exercício individual

Use H09/H10/H11 com H11 ocupado. Registre a lista final e uma tabela de passagens. Depois explique quantas vezes executa um contador iniciado em 0 enquanto menor que 2, incrementando 1.

**Entrega:** rastreamento individual de `for` e `while`

**Critérios:** lista correta; passagens visíveis; condição de parada explicada.

## Perguntas de verificação

- O que acontece quando a lista de entrada está vazia?
- O que torna um `while` perigoso?
- Por que rastrear antes de executar ajuda?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar o filtro e o contador.
2. Criar um conjunto diferente de horários.
3. Prever a saída antes de executar.
4. Entregar `m02-aula-03-revisao.md` com previsão, resultado e explicação.

**Entrega:** rastreamento revisado + novo caso executado

## Conexão com a trilha

A Aula 4 organiza lógica em funções e usa depuração para investigar um erro de validação.

## Referências

- [E-book correspondente](../ebooks/modulo-02-logica-de-programacao.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Script do professor](scripts/modulo-02-aula-03-lacos-e-listas.md)
