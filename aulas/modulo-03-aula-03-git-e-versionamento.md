# Roteiro de Aula — Módulo 3, Aula 3

# Git e Histórico Local

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-03-aula-03-git-e-versionamento.md).

## Objetivo da aula

Ensinar versionamento local com Git, distinguindo diretório de trabalho, área de preparação e histórico de commits.

Ao final, o aluno deverá conseguir:

- explicar por que salvar arquivo não é versionar
- usar `git status`, `add`, `diff` e `commit`
- criar commits com intenção clara
- ler um histórico simples
- separar mudanças de propósitos diferentes

## Conteúdos e conceitos

### Estados do Git
- working tree
- staging area
- commit

### Diff e intenção
- ver mudança
- preparar mudança
- mensagem explica propósito

### Histórico
- commit é registro
- hash identifica
- mensagem não substitui conteúdo

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

- E-book do Módulo 3
- Git instalado
- pasta de laboratório
- terminal

## Exemplos planejados

### Exemplo 1
README criado em um commit.

### Exemplo 2
Código adicionado em outro.

### Exemplo 3
Correção de instrução separada de alteração funcional.

## Demonstração planejada — Criar três commits locais com intenção clara

1. Inicializar repositório.
2. Conferir status.
3. Criar commit de apresentação/README.
4. Criar commit do simulador.
5. Criar commit de melhoria de documentação.
6. Ler log e diffs.

**Resultado pedagógico esperado:** o aluno enxerga o ciclo editar → revisar → preparar → registrar.

## Dinâmica em grupo — Organize o histórico

**Cenário:** A dupla recebe um conjunto de mudanças misturadas em README e código.

1. Separar as mudanças por intenção.
2. Escolher o que seria preparado primeiro.
3. Propor mensagens de commit.
4. Revisar se cada commit conta uma ideia.

**Entrega esperada:** plano de commits + evidência de status/diff

**Critérios:** intenção clara; mudanças coerentes por commit; uso correto de status/diff.

## Exercício individual

Faça ou simule um terceiro commit de melhoria de documentação. Mostre o estado antes, o que foi preparado e a mensagem final. Explique a diferença entre `git diff` e `git diff --staged`.

**Entrega:** registro do commit ou evidência equivalente

**Critérios:** estado conferido; mudança preparada conscientemente; mensagem coerente; diferença entre diffs explicada.

## Perguntas de verificação

- Salvar um arquivo cria uma versão no Git?
- Para que serve a staging area?
- Um commit deve ser grande ou pequeno?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar os commits.
2. Corrigir mensagens se necessário em um laboratório descartável.
3. Registrar `git log --oneline`.
4. Entregar `m03-aula-03-revisao.md`.

**Entrega:** histórico local com explicação das intenções

## Conexão com a trilha

A Aula 4 leva o histórico local para o GitHub e introduz publicação, branch e revisão colaborativa.

## Referências

- [E-book correspondente](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-03-aula-03-git-e-versionamento.md)
