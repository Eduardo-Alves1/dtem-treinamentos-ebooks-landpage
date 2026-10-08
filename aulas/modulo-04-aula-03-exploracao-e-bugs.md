# Roteiro — Módulo 4, Aula 3

**Condução com falas prontas:** [script do professor](scripts/modulo-04-aula-03-exploracao-e-bugs.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Exploração e reporte de bugs. **Objetivo observável:** registrar uma sessão exploratória e reportar BUG01.

**Leitura:** [E-book do módulo](../ebooks/modulo-04-qualidade-de-software.md), tópicos 3, 4. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

simulador, notas de sessão e modelo de reporte. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Apresente a aceitação de espaços e pergunte qual regra permite afirmar divergência. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Teste exploratório

**Conceito:** Exploração combina aprendizagem, desenho e execução de testes durante uma investigação orientada.

**Explicação simples:** Testar com uma missão e anotações é diferente de tentar ações sem objetivo.

**Aprofundamento:** Defina charter, tempo, dados, área e riscos. Durante a sessão, anote caminho, observação, perguntas e hipóteses. Diferencie defeito confirmado, dúvida de requisito e sugestão. Se não existe referência que estabeleça a divergência, registre uma pergunta antes de declarar bug. Experimente cancelar duas vezes, re-reservar e consultar após recusa. Exploração complementa casos preparados e produz informação sobre áreas ainda pouco compreendidas.

**Exemplo cotidiano:** Remover e readicionar um item ao carrinho pode revelar um estado ausente no fluxo principal.

**Cenário empresarial:** QA investiga se cancelar um id antigo pode remover uma reserva nova no mesmo horário.

**Erros a observar:** Confundir exploração com falta de registro; assumir defeito sem regra.

**Orientação:** Missão curta, notas de sessão e relato dos limites de cobertura.

### Identificação e reporte de bugs

**Conceito:** Um reporte comunica divergência reproduzível entre esperado e observado.

**Explicação simples:** Quem lê precisa repetir o problema e entender o impacto sem refazer toda a investigação.

**Aprofundamento:** Inclua título, versão, ambiente, pré-condição, dados, passos, esperado, observado, evidência e impacto. Severidade descreve efeito; prioridade indica ordem de tratamento no contexto. Não são sinônimos e seus níveis variam entre equipes. Não atribua culpa nem trate causa hipotética como fato. No caso, RN03 é o oráculo; a variante aceita espaços. Mesmo podendo ler a causa no código, o reporte precisa mostrar o comportamento e estado resultante.

**Exemplo cotidiano:** “Não funciona” não distingue erro de rede, entrada ou regra.

**Cenário empresarial:** QA registra BUG01, Dev reproduz e o time discute prioridade antes da correção.

**Erros a observar:** Título vago; passos incompletos; classificar sem explicar impacto.

**Orientação:** Uma divergência por reporte; evidência mínima suficiente; hipótese identificada.

Distribua os 17 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Faça uma sequência de cancelamento e depois reproduza BUG01, separando observado e hipótese.

**Exemplo 1:** Reservar H10, cancelar seu id e reservar H10 outra vez gera novo id. Cancelar o antigo retorna nao_encontrado e preserva a reserva nova. O identificador distingue reservas no mesmo horário.

**Exemplo 2:** Esperado nome_invalido e H11 livre; observado sucesso, id 1 e H11 ocupado. Impacto: recepção não identifica cliente. Severidade moderada e prioridade alta são propostas contextuais para o MVP, não classificações universais.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Investigar e comunicar. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 3: Realizar sessão exploratória de dez minutos**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Realizar sessão exploratória de dez minutos, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Escreva missão: investigar cancelamento e re-reserva.
2. Use referência em agenda vazia.
3. Execute cinco sequências e registre entradas e estados.
4. Classifique descobertas como confirmação, dúvida ou sugestão.
5. Indique uma próxima investigação.

**Entrega esperada:** notas de sessão com missão, sequências e descobertas Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m04-atividade-03.md`.

**Critérios específicos:** Cinco sequências; observação separada de interpretação; conclusão ligada a regra.

**Exemplo de resposta comentada:** Reservar H10, cancelar seu id e reservar H10 outra vez gera novo id. Cancelar o antigo retorna nao_encontrado e preserva a reserva nova. O identificador distingue reservas no mesmo horário.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Investigue cancelamento inexistente quando há outra reserva ativa.

**Atividade 4: Reportar BUG01 — nome somente com espaços**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Reportar BUG01 — nome somente com espaços, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Inicie AgendaComDefeito vazia.
2. Reserve espaços em H11 e consulte depois.
3. Registre esperado e observado.
4. Explique impacto na identificação da pessoa.
5. Proponha severidade e prioridade justificadas.

**Entrega esperada:** reporte reproduzível com versão, passos e evidência Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m04-atividade-04.md`.

**Critérios específicos:** Reproduzível; ligado a RN03; estado conferido; impacto separado da prioridade.

**Exemplo de resposta comentada:** Esperado nome_invalido e H11 livre; observado sucesso, id 1 e H11 ocupado. Impacto: recepção não identifica cliente. Severidade moderada e prioridade alta são propostas contextuais para o MVP, não classificações universais.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Reescreva o título para permitir localizar rapidamente a funcionalidade e a divergência.


## Exercício individual

Escreva um reporte próprio sem consultar o exemplo até finalizar os passos.

**Tempo:** 12 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual regra confirma o bug?
- Severidade e prioridade são iguais?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Explorar é testar sem objetivo? | A missão e as notas orientam a exploração. |
| Preciso saber a causa? | A divergência reproduzível é suficiente; causa pode ser hipótese. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: plano de testes, oito casos ligados a RN01–RN08, registro de execução das duas versões, BUG01 e evidência de reteste. A próxima aula verifica correções e acompanhamento.

## Tarefa para casa

Revisar BUG01 com feedback de um colega que tentou reproduzi-lo.

**Tempo sugerido:** 30–45 minutos. Entregar `m04-aula-03-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro.
