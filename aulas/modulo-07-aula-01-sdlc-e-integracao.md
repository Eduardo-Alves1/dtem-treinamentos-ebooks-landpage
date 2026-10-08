# Roteiro — Módulo 7, Aula 1

## Tema e objetivo da aula

**Tema:** SDLC e integração. **Objetivo observável:** desenhar ciclo com feedback e papéis.

**Leitura:** [E-book do módulo](../ebooks/modulo-07-ciclo-de-vida-do-software.md), tópicos 1. **Pré-requisito:** entregas de QA, Produto e Gestão dos módulos 4–6.

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

artefatos dos módulos anteriores e quadro. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Pergunte o que ocorre antes do primeiro código e depois da entrega. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### SDLC e integração entre áreas

**Conceito:** SDLC reúne atividades necessárias para criar, entregar, operar e evoluir software.

**Explicação simples:** A vida do sistema começa antes do código e continua depois que ele é entregue.

**Aprofundamento:** Descoberta identifica necessidade; requisitos tornam comportamento explícito; planejamento define recorte; construção implementa; testes geram evidências; entrega disponibiliza; operação observa e aprende. Não são departamentos que passam uma caixa sem conversar. Métodos iterativos repetem essas atividades em recortes; algumas acontecem em paralelo. Produto, Dev, QA, Dados e Infra contribuem conforme contexto. O laboratório cobre regras e verificação local; operação e infraestrutura são discutidas e simuladas.

**Exemplo cotidiano:** Um app continua sendo corrigido e melhorado depois de instalado pelos primeiros usuários.

**Cenário empresarial:** Uma reclamação na recepção retorna a Produto e QA para revisar o fluxo de cancelamento.

**Erros a observar:** Tratar etapas como sequência rígida universal; achar que depois do deploy acabou.

**Orientação:** Mostrar retorno de feedback e participação compartilhada.

Distribua os 20 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Construa fluxo e marque participação de QA antes dos testes.

**Exemplo 1:** Feedback da recepção retorna a requisitos. QA contribui em exemplos e execução; Dados define medida; Infra discute observação futura. No laboratório, deploy real e monitoramento não existem.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Conectar áreas. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 3 minutos de leitura; 10 de execução; 7 de revisão cruzada; 5 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 1: Desenhar fluxo completo do sistema**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Desenhar fluxo completo do sistema, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Liste necessidade, requisitos, planejamento, código, teste, entrega e operação.
2. Ligue etapas e inclua retorno de feedback.
3. Indique contribuição de cinco áreas.
4. Marque o que é executado e o que é simulado.

**Entrega esperada:** diagrama com papéis, retornos e limites Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m07-atividade-01.md`.

**Critérios específicos:** Cobertura do ciclo; feedback; distinção de execução e simulação.

**Exemplo de resposta comentada:** Feedback da recepção retorna a requisitos. QA contribui em exemplos e execução; Dados define medida; Infra discute observação futura. No laboratório, deploy real e monitoramento não existem.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Que retorno falta em um fluxo que termina nos testes?


## Exercício individual

Adicione retorno de uma reclamação a uma regra.

**Tempo:** 20 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Onde entra feedback?
- Quais partes são simuladas?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| É sempre sequencial? | Atividades podem se repetir e sobrepor. |
| Deploy encerra trabalho? | Operação e evolução continuam. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: diagrama completo de SDLC, matriz de rastreabilidade, checklist de release simulada e plano de resposta a falha. Rastreabilidade conecta decisões a evidências.

## Tarefa para casa

Revisar diagrama com limites.

**Tempo sugerido:** 30–45 minutos. Entregar `m07-aula-01-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. 

