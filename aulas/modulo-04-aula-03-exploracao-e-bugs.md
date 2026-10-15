# Roteiro de Aula — Módulo 4, Aula 3

# Exploração e Reporte de Bugs

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-04-aula-03-exploracao-e-bugs.md).

## Objetivo da aula

Ensinar exploração orientada por missão e reporte de bugs baseado em referência, passos reproduzíveis, esperado, observado e impacto.

Ao final, o aluno deverá conseguir:

- distinguir exploração de improviso
- separar observado de hipótese
- reproduzir BUG01
- escrever reporte útil
- discutir severidade/prioridade como decisões contextuais

## Conteúdos e conceitos

### Exploração com missão
- charter/pergunta
- aprendizado e adaptação
- registro

### Bug, dúvida ou melhoria
- referência define esperado
- observado precisa de evidência
- hipótese não é fato

### Reporte reproduzível
- título
- ambiente/versão
- passos
- esperado/observado
- impacto/evidência

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
- laboratório referência e variante
- modelo de bug report

## Exemplos planejados

### Exemplo 1
Sessão de cancelamento/reutilização.

### Exemplo 2
BUG01 de nome com espaços.

### Exemplo 3
Hipótese de causa separada do observado.

## Demonstração planejada — Explorar uma sequência e reportar BUG01

1. Executar reserva/cancelamento/reutilização.
2. Definir missão curta de exploração.
3. Reproduzir espaços na variante.
4. Comparar com RN03 e referência.
5. Montar BUG01 com evidência.

**Resultado pedagógico esperado:** o aluno diferencia exploração, defeito comprovado e hipótese.

## Dinâmica em grupo — Investigar e comunicar

**Cenário:** Uma dupla explora uma sequência; outra deve reproduzir o achado usando apenas o registro produzido.

1. Definir uma missão de 1 frase.
2. Executar sequência curta.
3. Registrar qualquer divergência.
4. Trocar o registro com outra dupla para reprodução.
5. Classificar como bug, dúvida ou melhoria com justificativa.

**Entrega esperada:** nota de exploração + reporte/reclassificação

**Critérios:** missão explícita; observado separado de hipótese; reprodução possível; classificação justificada.

## Exercício individual

Produza um reporte de BUG01 sem copiar o exemplo: título, versão, pré-condição, passos, esperado, observado, efeito no estado e impacto. Acrescente uma hipótese claramente marcada como não confirmada.

**Entrega:** bug report individual

**Critérios:** reproduzível; esperado ligado à regra; observado factual; hipótese identificada.

## Perguntas de verificação

- Todo comportamento estranho é bug?
- Se tenho uma hipótese da causa, posso colocá-la como fato?
- Severidade e prioridade são sempre iguais?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Pedir que outra pessoa tente reproduzir.
2. Registrar onde ela teve dúvida.
3. Revisar o reporte.
4. Entregar `m04-aula-03-revisao.md`.

**Entrega:** BUG01 revisado + nota do feedback

## Conexão com a trilha

A Aula 4 fecha o módulo com reteste, regressão, ferramentas e uma introdução responsável à automação.

## Referências

- [E-book correspondente](../ebooks/modulo-04-qualidade-de-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-04-aula-03-exploracao-e-bugs.md)
