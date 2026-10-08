# Roteiro — Módulo 7, Aula 4

**Condução com falas prontas:** [script do professor](scripts/modulo-07-aula-04-release-e-operacao.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Release e operação. **Objetivo observável:** produzir checklist e resposta a falha simulada.

**Leitura:** [E-book do módulo](../ebooks/modulo-07-ciclo-de-vida-do-software.md), tópicos 4. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

## Duração sugerida

| Etapa | Minutos |
|---|---:|
| Abertura e diagnóstico | 8 |
| Conceitos e exemplos | 17 |
| Demonstração guiada | 20 |
| Pausa | 5 |
| Dinâmica em dupla ou grupo | 15 |
| Exercício individual | 12 |
| Correção e dúvidas | 8 |
| Fechamento e orientação da tarefa | 5 |
| Total | 90 |

## Materiais necessários

versão de referência e registro de execução. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Pergunte se abrir o programa significa que pode liberar um serviço real. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Deploy, release, observação e resposta a falhas

**Conceito:** Entrega precisa identificar versão, critérios de liberação e forma de perceber e tratar falhas.

**Explicação simples:** Colocar algo no ar e confirmar que está útil são decisões relacionadas, mas distintas.

**Aprofundamento:** Deploy disponibiliza versão em ambiente; release libera a entrega para uso conforme estratégia. Eles podem ocorrer juntos ou separadamente. No curso, deploy é simulado: escolher versão, executar verificações e registrar decisão, sem publicar serviço. Defina verificação rápida, indicador, responsável e condição de reversão. Rollback nem sempre é seguro: mudanças em dados ou esquema podem exigir plano específico. No laboratório em memória, voltar à classe anterior é comparação didática e perde estado; não é um procedimento de produção. Observação precisa de ação diante de sinal ruim.

**Exemplo cotidiano:** Uma atualização pode ser instalada para um grupo pequeno antes de ser liberada a todos.

**Cenário empresarial:** Time só demonstra referência após reteste; falha crítica exige voltar ao plano e revisar evidências.

**Erros a observar:** Chamar execução local de deploy real; rollback como solução universal; medir sem ação.

**Orientação:** Versão identificada, checklist, condição de parada e limites explícitos.

Distribua os 17 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Faça verificações rápidas e emita decisão limitada ao laboratório.

**Exemplo 1:** Liberar demonstração da referência se cenários críticos passam. Se duplicidade ou cancelamento incorreto ocorrer, interromper, registrar entrada/estado, corrigir e repetir. Reinício perde reservas; nenhuma estratégia de migração real foi implementada.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Liberar ou interromper. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 4: Criar checklist de release e reversão simuladas**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Criar checklist de release e reversão simuladas, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Identifique versão e escopo.
2. Defina verificações de reserva e cancelamento.
3. Defina sinal de falha e responsável.
4. Descreva parar demonstração e retornar à versão de referência.
5. Registre perda de estado e limites.

**Entrega esperada:** checklist, decisão e plano de resposta simulado Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m07-atividade-04.md`.

**Critérios específicos:** Versão e evidências; gatilho acionável; não confundir com produção.

**Exemplo de resposta comentada:** Liberar demonstração da referência se cenários críticos passam. Se duplicidade ou cancelamento incorreto ocorrer, interromper, registrar entrada/estado, corrigir e repetir. Reinício perde reservas; nenhuma estratégia de migração real foi implementada.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Qual risco aparece se uma versão nova altera dados persistidos?


## Exercício individual

Defina gatilho de parada para falha em RN02.

**Tempo:** 12 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual é o escopo liberado?
- Quais dados se perdem ao reiniciar?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Execução local é deploy real? | Não neste exercício; publicação e infraestrutura não foram implementadas. |
| Rollback é sempre seguro? | Não; depende de dados e compatibilidade. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: diagrama completo de SDLC, matriz de rastreabilidade, checklist de release simulada e plano de resposta a falha. O projeto final integra todas essas decisões.

## Tarefa para casa

Consolidar fluxo, matriz e checklist.

**Tempo sugerido:** 30–45 minutos. Entregar `m07-aula-04-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. Organizar também a entrega final e a reflexão individual.
