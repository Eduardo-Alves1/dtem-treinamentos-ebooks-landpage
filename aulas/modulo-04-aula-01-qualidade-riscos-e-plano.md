# Roteiro — Módulo 4, Aula 1

**Condução com falas prontas:** [script do professor](scripts/modulo-04-aula-01-qualidade-riscos-e-plano.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Qualidade, riscos e plano. **Objetivo observável:** produzir um plano de uma página com riscos e limites.

**Leitura:** [E-book do módulo](../ebooks/modulo-04-qualidade-de-software.md), tópicos 1. **Pré-requisito:** lógica, leitura de código e execução do laboratório dos módulos 2 e 3.

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

quadro, regras RN01–RN08 e modelo de plano. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Mostre duas reservas no mesmo horário e peça uma consequência operacional. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Qualidade, riscos e plano de testes

**Conceito:** QA contribui para prevenir e identificar problemas; qualidade depende de decisões compartilhadas pelo time.

**Explicação simples:** Discutir uma regra confusa antes de construir pode evitar um defeito que seria caro descobrir no final.

**Aprofundamento:** Um plano define objetivo, escopo, riscos, estratégia, ambiente, dados, responsabilidades e condições de início e encerramento. Não é necessário um documento enorme, mas deve orientar decisões. Priorize impacto e probabilidade com justificativa. Testes podem revelar falhas e aumentar confiança, sem provar ausência de todo defeito. No laboratório, RN02 importa por conflito operacional; persistência, segurança e concorrência real estão fora do escopo. Registre essas limitações para que um resultado aprovado não seja interpretado como autorização para uso em produção.

**Exemplo cotidiano:** Uma agenda bonita ainda pode permitir duas pessoas no mesmo horário.

**Cenário empresarial:** Produto explica o impacto, Dev discute controles e QA prepara cenários desde a conversa sobre regras.

**Erros a observar:** Esperar tudo ficar pronto; escrever plano como lista de ferramentas; prometer zero defeitos.

**Orientação:** Relacionar cada risco à evidência necessária e documentar limites.

Distribua os 17 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Escreva objetivo, risco de duplicidade e teste correspondente. Modele uma condição de encerramento mensurável.

**Exemplo 1:** Prioridade maior para integridade da reserva por conflito operacional. Executar testes sequenciais nas duas classes; persistência e acesso simultâneo não são comprovados. Não liberar um produto real com base apenas neste laboratório.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Planejar antes de executar. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 1: Criar plano de testes de uma página**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Criar plano de testes de uma página, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Defina escopo RN01–RN08 e o que está fora.
2. Liste duplicidade, nome inválido e cancelamento incorreto como riscos.
3. Identifique versões, dados e ambiente.
4. Defina início: regras e laboratório disponíveis.
5. Defina encerramento: casos críticos executados, sem defeito impeditivo aberto no escopo.

**Entrega esperada:** plano com objetivo, riscos, estratégia e critérios Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m04-atividade-01.md`.

**Critérios específicos:** Riscos justificados; escopo delimitado; condições observáveis de início e fim.

**Exemplo de resposta comentada:** Prioridade maior para integridade da reserva por conflito operacional. Executar testes sequenciais nas duas classes; persistência e acesso simultâneo não são comprovados. Não liberar um produto real com base apenas neste laboratório.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Qual risco não pode ser investigado pelo simulador e o que seria necessário para testá-lo?


## Exercício individual

Escolha o risco de cancelamento e detalhe uma evidência que permita investigar seu impacto.

**Tempo:** 12 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Quem contribui para qualidade antes do código?
- O que não será comprovado por este plano?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Plano precisa ser longo? | Precisa orientar decisões; uma página pode ser suficiente. |
| Testar prova ausência de bugs? | Não; define confiança no escopo e nas condições investigadas. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: plano de testes, oito casos ligados a RN01–RN08, registro de execução das duas versões, BUG01 e evidência de reteste. A próxima aula transforma regras em casos.

## Tarefa para casa

Revisar o plano e acrescentar uma limitação relevante.

**Tempo sugerido:** 30–45 minutos. Entregar `m04-aula-01-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro.
