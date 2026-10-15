# Roteiro de Aula — Módulo 2, Aula 2

# Variáveis, Tipos e Decisões

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-02-aula-02-variaveis-e-condicoes.md).

## Objetivo da aula

Usar variáveis, tipos de dados e condições para representar informações e decisões do caso Agenda Clara em Python introdutório.

Ao final, o aluno deverá conseguir:

- distinguir texto, número, booleano e lista
- explicar por que o tipo importa
- montar um dicionário de dados inicial
- construir uma tabela de decisão
- representar condições simples em Python sem perder a regra de negócio

## Conteúdos e conceitos

### Variáveis e tipos
- nome e valor
- str, int, bool e list
- tipo representa a natureza do dado

### Atribuição e comparação
- = atribui
- == compara
- operações dependem do tipo

### Condições e ordem
- if/elif/else
- expressão booleana
- ordem de validação

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
- editor de código ou REPL Python
- quadro/tabela de decisão

## Exemplos planejados

### Exemplo 1
Dicionário de dados da reserva.

### Exemplo 2
Tabela de decisão nome válido × horário válido.

### Exemplo 3
Validação simples em Python.

## Demonstração planejada — Dicionário de dados e tabela de decisão

1. Definir nome, horário, quantidade e lista de disponíveis.
2. Associar tipo, exemplo e restrição.
3. Comparar operações com número e texto.
4. Montar quatro combinações de nome/horário válidos ou inválidos.
5. Converter duas decisões em if/elif simples.

**Resultado pedagógico esperado:** o aluno liga tipo e condição à regra de negócio.

## Dinâmica em grupo — Dicionário e decisão em dupla

**Cenário:** O time precisa documentar os dados e as decisões antes de expandir o código.

1. Montar o dicionário de dados.
2. Comparar `2 + 3` com `'2' + '3'`.
3. Completar a tabela de quatro combinações.
4. Trocar a ordem de validação e discutir o efeito.

**Entrega esperada:** dicionário de dados + tabela de decisão

**Critérios:** tipo coerente; restrição explícita; quatro combinações cobertas; ordem de validação explicada.

## Exercício individual

Explique o que se perde se `H09` virar apenas `9`. Depois escreva ou represente uma condição que rejeita nome vazio/espaços antes de validar o horário. Diga se a regra foi atendida ou se apenas uma mensagem foi exibida.

**Entrega:** resposta curta + condição/tabela

**Critérios:** tipo justificado; condição coerente; diferença entre saída e regra compreendida.

## Perguntas de verificação

- `2` e `'2'` são a mesma coisa?
- Qual diferença entre `=` e `==`?
- A ordem dos `if` pode alterar a resposta?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar os dois artefatos com feedback.
2. Adicionar uma entrada nova ou restrição.
3. Executar ao menos um exemplo em Python.
4. Entregar `m02-aula-02-revisao.md` com previsão, resultado e explicação.

**Entrega:** dicionário/tabela revisados + evidência de um exemplo Python

## Conexão com a trilha

A Aula 3 introduz listas e repetição para trabalhar com vários horários sem copiar a mesma lógica.

## Referências

- [E-book correspondente](../ebooks/modulo-02-logica-de-programacao.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Script do professor](scripts/modulo-02-aula-02-variaveis-e-condicoes.md)
