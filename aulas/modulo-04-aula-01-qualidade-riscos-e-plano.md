# Roteiro de Aula — Módulo 4, Aula 1

# Qualidade, Riscos e Plano de Testes

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-04-aula-01-qualidade-riscos-e-plano.md).

## Objetivo da aula

Introduzir qualidade orientada a risco e produzir um plano de testes enxuto com escopo, prioridades, estratégia e limites.

Ao final, o aluno deverá conseguir:

- explicar qualidade como responsabilidade compartilhada
- identificar riscos do produto
- priorizar o que testar
- produzir plano de uma página
- declarar limites do laboratório

## Conteúdos e conceitos

### Qualidade compartilhada
- prevenção antes do código
- verificação depois
- QA não trabalha isolado

### Risco
- probabilidade e impacto
- prioridade
- contexto

### Plano de testes
- objetivo
- escopo
- estratégia
- ambiente/dados
- entrada/saída
- limites

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
- caso RN01–RN08
- modelo de plano de testes
- laboratório

## Exemplos planejados

### Exemplo 1
Risco de reserva duplicada.

### Exemplo 2
Risco de cancelamento incorreto.

### Exemplo 3
Limites de um laboratório educacional.

## Demonstração planejada — Construir um plano de testes de uma página

1. Definir objetivo e escopo RN01–RN08.
2. Listar três riscos e justificar prioridade.
3. Definir estratégia e dados.
4. Definir condições de início e encerramento.
5. Registrar explicitamente o que está fora do escopo.

**Resultado pedagógico esperado:** o aluno produz um plano que orienta decisão e não apenas lista ferramentas.

## Dinâmica em grupo — Planejar antes de executar

**Cenário:** A equipe precisa decidir o foco de testes do MVP Agenda Clara antes de iniciar execução.

1. Escolher três riscos.
2. Ordená-los com justificativa.
3. Relacionar cada risco a um tipo de evidência/teste.
4. Registrar um limite que a estratégia não cobre.

**Entrega esperada:** recorte de plano de testes

**Critérios:** risco justificado; evidência relacionada; limite explícito; sem promessa de ‘zero bugs’.

## Exercício individual

Escolha o risco de cancelamento e escreva objetivo, dados necessários, sequência de investigação, evidência esperada e uma limitação do teste.

**Entrega:** bloco individual do plano

**Critérios:** risco claro; evidência observável; sequência coerente; limite declarado.

## Perguntas de verificação

- Testes provam que não existem bugs?
- Plano de testes precisa ser um documento enorme?
- Quem é responsável pela qualidade?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar o plano com feedback.
2. Acrescentar pelo menos uma limitação relevante.
3. Entregar `m04-aula-01-revisao.md`.

**Entrega:** plano de testes revisado

## Conexão com a trilha

A Aula 2 transforma regras em cenários e casos funcionais reproduzíveis.

## Referências

- [E-book correspondente](../ebooks/modulo-04-qualidade-de-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-04-aula-01-qualidade-riscos-e-plano.md)
