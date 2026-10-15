# Roteiro de Aula — Módulo 2, Aula 4

# Funções e Resolução de Problemas

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-02-aula-04-funcoes-e-desafios.md).

## Objetivo da aula

Usar funções para encapsular responsabilidades e aplicar depuração orientada por hipótese em uma validação simples.

Ao final, o aluno deverá conseguir:

- explicar parâmetro e retorno
- distinguir `print` de `return`
- implementar `validar_nome` em Python
- reproduzir e explicar a falha com espaços
- corrigir a validação e repetir os testes

## Conteúdos e conceitos

### Funções e responsabilidade
- entrada por parâmetros
- retorno
- uma responsabilidade clara

### `print` versus `return`
- exibir não é devolver
- chamador usa retorno
- teste deve observar o valor correto

### Depuração por hipótese
- reproduzir
- formular hipótese
- mudar uma coisa
- retestar

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
- casos de entrada `Ana`, `''` e `'   '`

## Exemplos planejados

### Exemplo 1
Função de validação de nome.

### Exemplo 2
Função para calcular desconto como exemplo cotidiano.

### Exemplo 3
Bug lógico causado por espaços.

## Demonstração planejada — Implementar, reproduzir e corrigir `validar_nome`

1. Criar `validar_nome(nome)`.
2. Testar Ana, vazio e espaços.
3. Comparar `print` e `return`.
4. Reproduzir a validação defeituosa `nome != ''`.
5. Trocar pela validação com `strip` e repetir os casos.

**Resultado pedagógico esperado:** o aluno relaciona responsabilidade da função, retorno e processo de depuração.

## Dinâmica em grupo — Função sob revisão

**Cenário:** Uma dupla recebe uma função de validação e três entradas; uma pessoa explica e a outra tenta encontrar um contraexemplo.

1. Definir responsabilidade da função.
2. Executar/prever três entradas.
3. Comparar validação defeituosa e corrigida.
4. Trocar papéis e propor um novo caso.

**Entrega esperada:** função + tabela entrada/esperado/observado

**Critérios:** responsabilidade delimitada; retornos corretos; hipótese do bug explicada; reteste após correção.

## Exercício individual

Escreva `validar_nome` em Python ou pseudocódigo e registre os retornos para Ana, vazio e espaços. Depois responda: quem deve decidir se um horário pode ser reservado — `validar_nome` ou a operação de reserva? Justifique.

**Entrega:** função + três resultados + justificativa

**Critérios:** função correta; retorno em vez de apenas impressão; responsabilidade separada; justificativa coerente.

## Perguntas de verificação

- Mostrar um resultado com `print` significa que a função o retornou?
- Por que espaços passam em `nome != ''`?
- Depois de corrigir o bug, por que testar novamente um nome válido?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar a função e a investigação do bug.
2. Organizar as atividades do módulo.
3. Resolver um mini desafio próprio de validação ou repetição.
4. Registrar uma reflexão sobre o que mudou no seu raciocínio.

**Entrega:** entrega final do Módulo 2 organizada e revisada

## Conexão com a trilha

O Módulo 3 mostra como software é organizado, lido e versionado. A lógica aprendida aqui será reconhecida em código e depois comparada com outras linguagens.

## Referências

- [E-book correspondente](../ebooks/modulo-02-logica-de-programacao.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Script do professor](scripts/modulo-02-aula-04-funcoes-e-desafios.md)
