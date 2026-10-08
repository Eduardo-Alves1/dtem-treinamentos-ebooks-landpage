# Roteiro — Módulo 6, Aula 4

**Condução com falas prontas:** [script do professor](scripts/modulo-06-aula-04-kanban-e-ferramentas.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Kanban e ferramentas. **Objetivo observável:** aplicar WIP e comunicar uma decisão de projeto.

**Leitura:** [E-book do módulo](../ebooks/modulo-06-gestao-de-projetos-tech.md), tópicos 5, 6. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

quadro ou cartões e IDs. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Mostre cinco itens iniciados e nenhum concluído. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Kanban, políticas e métricas de fluxo

**Conceito:** Kanban torna trabalho visível e orienta melhoria do fluxo com políticas explícitas.

**Explicação simples:** Começar menos tarefas pode ajudar a terminar mais.

**Aprofundamento:** Um quadro é parte da prática, não Kanban completo por si só. Defina fluxo, ponto de início e fim, limites de WIP e políticas. Exemplo: pronto, em execução, em verificação e concluído; WIP de dois itens somando execução e verificação. Bloqueio deve permanecer visível e normalmente continua contando como trabalho iniciado. Lead time depende do ponto de compromisso escolhido; cycle time mede início até fim; throughput conta itens concluídos por período. Não comparar números de times diferentes sem contexto.

**Exemplo cotidiano:** Dez pedidos iniciados e nenhum entregue não significam boa capacidade de atendimento.

**Cenário empresarial:** Time limita início para ajudar a concluir cancelamento antes de abrir relatório.

**Erros a observar:** Quadro sem políticas; mover bloqueado para esconder WIP; contar iniciado como entregue.

**Orientação:** Definir limites, observar gargalos e concluir antes de iniciar.

### Ferramentas e comunicação de projeto

**Conceito:** Ferramentas registram acordos e estados; gestão exige interpretar e agir sobre essas informações.

**Explicação simples:** Mudar de Jira para Azure DevOps não deveria apagar o sentido do trabalho.

**Aprofundamento:** Use título, objetivo, responsável, estado, dependências, evidência e motivo de bloqueio. Campos variam por ferramenta e configuração. Links devem ligar história, tarefa, bug e teste. Defina estados e política de transição antes de configurar a tela. O relatório de andamento deve comunicar objetivo, progresso, risco e decisão necessária, sem apenas enumerar tarefas. Cartões em papel ou Markdown são alternativas para o curso.

**Exemplo cotidiano:** Uma lista de tarefas sem dependências não mostra que um atraso bloqueia outras entregas.

**Cenário empresarial:** Time mantém US02, TC03 e BUG01 relacionados e comunica impacto na meta.

**Erros a observar:** Ferramenta como substituta de conversa; estados contraditórios; relatório longo sem decisão.

**Orientação:** Uma fonte de estado, vínculos e mensagens orientadas a ação.

Distribua os 17 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Limite WIP e relacione história, teste e bug.

**Exemplo 1:** Com dois itens ativos, não puxar terceiro; ajudar a verificar ou remover bloqueio. Throughput de dois itens em uma rodada informa conclusão, sem inferir produtividade individual.

**Exemplo 2:** Meta: reserva íntegra. Progresso: sucesso/conflito verificados. Risco: RN03 falha na variante. Pedido: priorizar correção antes da liberação simulada. BUG01 ligado a US02 e TC03.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Concluir antes de começar. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 5: Simular quadro com limite de WIP**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Simular quadro com limite de WIP, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Crie quatro colunas e políticas.
2. Use cinco cartões do backlog.
3. Defina WIP 2 para execução mais verificação.
4. Introduza bloqueio e decida como manter visível.
5. Conte concluídos e identifique gargalo.

**Entrega esperada:** quadro antes/depois, políticas e análise de fluxo Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m06-atividade-05.md`.

**Critérios específicos:** Limite respeitado; bloqueio visível; métrica com período definido.

**Exemplo de resposta comentada:** Com dois itens ativos, não puxar terceiro; ajudar a verificar ou remover bloqueio. Throughput de dois itens em uma rodada informa conclusão, sem inferir produtividade individual.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Por que mover bloqueado para fora do limite pode distorcer a análise?

**Atividade 6: Produzir quadro e atualização executiva**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Produzir quadro e atualização executiva, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Represente história, tarefa, bug e teste com IDs.
2. Vincule os quatro artefatos.
3. Defina transição para concluído.
4. Escreva atualização de quatro linhas: meta, progresso, risco e pedido.

**Entrega esperada:** cartões vinculados e comunicação breve Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m06-atividade-06.md`.

**Critérios específicos:** Rastreabilidade; estado coerente; pedido acionável.

**Exemplo de resposta comentada:** Meta: reserva íntegra. Progresso: sucesso/conflito verificados. Risco: RN03 falha na variante. Pedido: priorizar correção antes da liberação simulada. BUG01 ligado a US02 e TC03.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Qual decisão seu relatório espera de quem recebe?


## Exercício individual

Escreva atualização de quatro linhas com pedido de decisão.

**Tempo:** 12 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual é o gargalo?
- Bloqueio conta como trabalho iniciado?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Quadro basta para Kanban? | São necessárias políticas e gestão do fluxo. |
| Preciso de conta? | Cartões ou Markdown permitem o exercício. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: plano de Sprint simulada, quadro com políticas e limites, registros de Daily, Review e Retrospectiva e análise de capacidade. SDLC conecta decisões até operação.

## Tarefa para casa

Consolidar Sprint simulada e análise.

**Tempo sugerido:** 30–45 minutos. Entregar `m06-aula-04-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. Organizar também a entrega final e a reflexão individual.
