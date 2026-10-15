# Roteiro de Aula — Módulo 4, Aula 2

# Cenários e Testes Funcionais

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-04-aula-02-cenarios-e-testes-funcionais.md).

## Objetivo da aula

Transformar regras em cenários e casos funcionais reproduzíveis, separando resultado esperado de resultado observado.

Ao final, o aluno deverá conseguir:

- escrever casos com pré-condição, dados, passos e esperado
- relacionar caso à regra
- executar e registrar observado
- cobrir caminhos positivos e negativos
- preservar estado como parte da evidência

## Conteúdos e conceitos

### Cenário versus caso
- cenário descreve situação
- caso detalha execução
- regra dá referência

### Esperado antes do observado
- regra define referência
- não adaptar esperado ao resultado
- divergência pode indicar bug

### Cobertura funcional
- positivo e negativo
- estado depois da ação
- prioridade pelo risco

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

- E-book do Módulo 4
- RN01–RN08
- modelo de caso de teste
- laboratório

## Exemplos planejados

### Exemplo 1
TC03 para nome com espaços.

### Exemplo 2
Conflito de H09.

### Exemplo 3
Cancelamento de ID inexistente.

## Demonstração planejada — Escrever e executar casos funcionais

1. Escolher RN03 e escrever esperado.
2. Executar na referência e variante.
3. Registrar observado e estado.
4. Escrever caso de conflito RN05.
5. Comparar resultados sem alterar o esperado.

**Resultado pedagógico esperado:** o aluno produz evidência repetível e identifica divergência entre versões.

## Dinâmica em grupo — Do requisito à evidência

**Cenário:** Cada dupla recebe uma regra diferente de RN01–RN08.

1. Escrever um caso com dados e estado inicial.
2. Definir esperado antes de executar.
3. Executar ou simular declaradamente.
4. Registrar observado e estado final.
5. Trocar caso com outra dupla para verificar reproduzibilidade.

**Entrega esperada:** caso funcional revisado por outra dupla

**Critérios:** vínculo com regra; esperado explícito; dados suficientes; estado final observado.

## Exercício individual

Escreva o caso de RN07 para cancelar um ID inexistente enquanto existe outra reserva válida. Inclua estado inicial, ação, esperado e o que deve permanecer inalterado.

**Entrega:** caso funcional individual

**Critérios:** RN07 ligada; estado preservado; dados claros; resultado verificável.

## Perguntas de verificação

- O esperado pode ser definido depois de executar?
- Caso de teste é só uma lista de cliques?
- Por que registrar estado depois de uma recusa?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar os casos com feedback.
2. Executar nas versões disponíveis.
3. Registrar versão, esperado, observado e evidência.
4. Entregar `m04-aula-02-revisao.md`.

**Entrega:** casos revisados + registros de execução

## Conexão com a trilha

A Aula 3 usa os casos para explorar o sistema e registrar um defeito de forma útil.

## Referências

- [E-book correspondente](../ebooks/modulo-04-qualidade-de-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-04-aula-02-cenarios-e-testes-funcionais.md)
