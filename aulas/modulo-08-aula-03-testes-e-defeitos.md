# Roteiro — Módulo 8, Aula 3

## Tema e objetivo da aula

**Tema:** Testes e defeitos. **Objetivo observável:** executar oito casos e distinguir bugs executados e fornecidos.

**Leitura:** [E-book do módulo](../ebooks/modulo-08-projeto-final-hands-on.md), tópicos 3. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

## Duração sugerida

| Etapa | Minutos |
|---|---:|
| Abertura e diagnóstico | 10 |
| Teoria com exemplos | 20 |
| Demonstração | 15 |
| Pausa | 10 |
| Dinâmica em grupo | 25 |
| Exercício individual | 20 |
| Perguntas e fechamento | 15 |
| Orientação da tarefa de casa | 5 |
| Total | 120 |

## Materiais necessários

Python, duas classes e registro BUG02. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Mostre duas evidências de origem diferente e peça classificação. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Testes, bugs e evidências do projeto

**Conceito:** A execução deve sustentar o que o projeto afirma sobre comportamento e qualidade.

**Explicação simples:** Mostre a entrada, o esperado, o observado e a versão; o leitor não deve depender da sua memória.

**Aprofundamento:** Use oito casos do kit e acrescente uma sequência própria. Execute referência e variante, reiniciando estado quando previsto. BUG01 pode ser reproduzido; BUG02 é fornecido como um registro fictício de uma terceira versão inexistente no código. Documente esse tipo de evidência. Não afirmar execução de BUG02. Reteste de BUG01 usa referência; análise de BUG02 propõe passos e critério de correção sem tratar a proposta como executada. Distinga falha, dúvida e melhoria. Vincule regras, histórias e casos.

**Exemplo cotidiano:** Um print isolado não prova todo o caminho nem identifica a versão.

**Cenário empresarial:** QA apresenta BUG01 e explica por que a ocupação de H11 reforça a evidência.

**Erros a observar:** Misturar simulação e execução; aprovar sem estado; contar caso não executado como passado.

**Orientação:** Versões identificadas e registros honestos de cobertura.

Distribua os 20 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Execute BUG01 e leia BUG02 como incidente fornecido.

**Exemplo 1:** BUG01 viola RN03 na variante. BUG02 descreve RN06 violada em versão fictícia: cancelamento retorna sucesso, mas horário não reaparece. A referência fornecida não tem esse defeito; produzir plano de confirmação, não falso resultado.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Provar comportamento. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 3 minutos de leitura; 10 de execução; 7 de revisão cruzada; 5 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 3: Executar testes e produzir dois reportes**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Executar testes e produzir dois reportes, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Execute oito casos de referência e a divergência de espaços.
2. Registre entrada, retorno e estado.
3. Produza BUG01.
4. Analise registro fornecido de BUG02 e declare simulado.
5. Adicione uma sequência própria e parecer de qualidade.

**Entrega esperada:** testes.md e bugs.md com evidências identificadas Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m08-atividade-03.md`.

**Critérios específicos:** Oito casos; dois tipos de bug diferenciados; nenhuma execução inventada.

**Exemplo de resposta comentada:** BUG01 viola RN03 na variante. BUG02 descreve RN06 violada em versão fictícia: cancelamento retorna sucesso, mas horário não reaparece. A referência fornecida não tem esse defeito; produzir plano de confirmação, não falso resultado.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Que evidência adicional você pediria antes de confirmar BUG02 num produto real?


## Exercício individual

Execute uma sequência nova e emita parecer.

**Tempo:** 20 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual versão foi executada?
- Que confirmação falta para BUG02?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| BUG02 existe no código? | Não; é registro fictício fornecido para análise. |
| Copiar saída conta? | É preciso produzir ou declarar a origem da evidência. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: dossiê Agenda Clara com requisitos, três histórias, backlog, oito casos executados, dois reportes simulados, Sprint, SDLC, release e apresentação de cinco minutos. A entrega final conecta decisões e demonstração.

## Tarefa para casa

Consolidar testes, bugs e reteste.

**Tempo sugerido:** 30–45 minutos. Entregar `m08-aula-03-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. 

