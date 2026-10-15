# Roteiro de Aula — Módulo 7, Aula 4

# Release, Operação e Resposta a Falhas

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-07-aula-04-release-e-operacao.md).

## Objetivo da aula

Ensinar decisão de release baseada em evidências, diferenciar deploy de release e praticar resposta a falha dentro dos limites do laboratório educacional.

Ao final, o aluno deverá conseguir:

- diferenciar deploy e release
- produzir checklist de liberação
- definir gatilho de parada
- explicar limites de rollback/recuperação no laboratório
- emitir decisão proporcional às evidências

## Conteúdos e conceitos

### Deploy versus release
- deploy coloca versão em ambiente
- release disponibiliza/autoriza uso
- processos podem variar

### Critérios de liberação
- casos críticos
- defeitos impeditivos
- limites conhecidos
- decisão explícita

### Operação e resposta a falhas
- detectar
- interromper/mitigar
- registrar
- recuperar
- aprender

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

- E-book do Módulo 7
- checklist de release
- laboratório
- matriz de rastreabilidade

## Exemplos planejados

### Exemplo 1
Falha de RN02 antes de demonstração.

### Exemplo 2
Checklist de release simulada.

### Exemplo 3
Reinício do laboratório não tratado como rollback real.

## Demonstração planejada — Executar checklist e tomar decisão de liberação

1. Revisar critérios críticos.
2. Executar verificações rápidas de reserva/conflito/cancelamento.
3. Inserir uma falha crítica simulada.
4. Decidir liberar, interromper ou restringir.
5. Registrar limites e plano de resposta.

**Resultado pedagógico esperado:** o aluno emite decisão clara e honesta sobre o escopo autorizado.

## Dinâmica em grupo — Liberar ou interromper

**Cenário:** A equipe está a dez minutos de uma demonstração e um teste crítico de conflito falha.

1. Identificar requisito/risco afetado.
2. Classificar impacto.
3. Decidir release/demonstração.
4. Registrar justificativa e próxima ação.
5. Indicar claramente o que não será demonstrado.

**Entrega esperada:** decisão de release + mini plano de resposta

**Critérios:** evidência citada; escopo afetado claro; sem mascarar falha; limite da simulação declarado.

## Exercício individual

Escreva um gatilho de parada para falha de RN02 e uma resposta de quatro passos. Diferencie o que é possível no laboratório do que exigiria ambiente de produção real.

**Entrega:** gatilho + resposta

**Critérios:** gatilho observável; ação coerente; reteste previsto; limites reais declarados.

## Perguntas de verificação

- Deploy e release são sempre a mesma coisa?
- Reiniciar o laboratório é rollback?
- Uma falha crítica precisa bloquear todo o produto?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Revisar o diagrama SDLC.
2. Concluir matriz de rastreabilidade.
3. Finalizar checklist de release.
4. Registrar plano de resposta a falha.
5. Entregar `m07-aula-04-revisao.md` e organizar a entrega do módulo.

**Entrega:** pacote final do Módulo 7

## Conexão com a trilha

O Módulo 8 reúne os artefatos em um projeto final integrado e verificável.

## Referências

- [E-book correspondente](../ebooks/modulo-07-ciclo-de-vida-do-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-07-aula-04-release-e-operacao.md)
