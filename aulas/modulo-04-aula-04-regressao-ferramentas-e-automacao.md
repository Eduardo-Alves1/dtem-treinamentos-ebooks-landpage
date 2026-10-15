# Roteiro de Aula — Módulo 4, Aula 4

# Regressão, Ferramentas e Automação

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-04-aula-04-regressao-ferramentas-e-automacao.md).

## Objetivo da aula

Distinguir reteste e regressão, organizar evidências em ferramentas e apresentar automação como forma de repetir verificações úteis, não como substituta do raciocínio de QA.

Ao final, o aluno deverá conseguir:

- distinguir reteste de regressão
- selecionar uma regressão baseada em risco
- emitir parecer limitado às evidências
- explicar valor e limites de automação
- reconhecer JavaScript/TypeScript como opções comuns em ferramentas de automação sem exigir domínio nesta formação

## Conteúdos e conceitos

### Reteste e regressão
- reteste confirma a correção
- regressão procura efeitos colaterais
- seleção por risco

### Ferramentas e rastreabilidade
- caso, execução e bug ligados
- status não substitui evidência
- Jira/ADO são meios

### Automação
- repete verificações
- custo de manutenção
- boa escolha depende de estabilidade/valor

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
- laboratório
- registro de BUG01
- quadro de rastreabilidade

## Exemplos planejados

### Exemplo 1
Reteste de BUG01.

### Exemplo 2
Regressão de reserva e cancelamento.

### Exemplo 3
Teste automatizado conceitual com Playwright/TypeScript como ponte futura.

## Demonstração planejada — Do reteste ao parecer de regressão

1. Retestar espaços na versão corrigida/referência.
2. Executar reserva válida.
3. Executar conflito e cancelamento selecionados.
4. Registrar versão e resultados.
5. Mostrar como a mesma verificação poderia ser automatizada conceitualmente.

**Resultado pedagógico esperado:** o aluno toma decisão de qualidade proporcional à evidência e entende automação como continuidade da lógica.

## Dinâmica em grupo — Da correção à decisão

**Cenário:** A equipe recebeu uma correção para BUG01 e precisa decidir o mínimo de regressão antes de uma demonstração.

1. Definir o reteste obrigatório.
2. Escolher três casos de regressão e justificar.
3. Registrar o que permanece fora do escopo.
4. Emitir parecer limitado às evidências.

**Entrega esperada:** mini plano de reteste/regressão + parecer

**Critérios:** reteste separado de regressão; seleção justificada; limites declarados; parecer coerente.

## Exercício individual

Imagine que nome foi corrigido, mas o caso crítico de cancelamento ainda não foi executado. Escreva um parecer de três a cinco linhas com decisão, risco e próxima ação.

**Entrega:** parecer individual

**Critérios:** não inventa aprovação; risco explícito; próxima ação objetiva.

## Perguntas de verificação

- Reteste e regressão são sinônimos?
- Automação substitui teste exploratório?
- Por que introduzir JS/TS aqui sem trocar a linguagem do módulo de lógica?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Organizar o plano de testes.
2. Consolidar oito casos e execuções.
3. Revisar BUG01 e reteste.
4. Anexar parecer de regressão.
5. Registrar uma nota: que verificação você automatizaria primeiro e por quê?

**Entrega:** entrega final do Módulo 4

## Conexão com a trilha

O Módulo 5 muda a lente para Produto: problema, requisitos, histórias, backlog e comunicação com o time.

## Referências

- [E-book correspondente](../ebooks/modulo-04-qualidade-de-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-04-aula-04-regressao-ferramentas-e-automacao.md)
