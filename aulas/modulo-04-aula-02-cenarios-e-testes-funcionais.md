# Roteiro — Módulo 4, Aula 2

**Condução com falas prontas:** [script do professor](scripts/modulo-04-aula-02-cenarios-e-testes-funcionais.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Cenários e testes funcionais. **Objetivo observável:** escrever oito casos com regra, dados e resultado.

**Leitura:** [E-book do módulo](../ebooks/modulo-04-qualidade-de-software.md), tópicos 2. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

Python 3, simulador e tabela de casos. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Compare “testar reserva” com uma entrada e estado explícitos. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Cenários e testes funcionais

**Conceito:** Cenário resume uma situação; caso de teste define como executá-la e conferir seu resultado.

**Explicação simples:** “Testar reserva” é amplo. “Reservar H09 livre para Ana e confirmar que ele fica ocupado” permite conferência.

**Aprofundamento:** Um caso contém ID, regra, pré-condição, dados, passos, esperado e estado final. A execução acrescenta versão, observado, status e evidência. O esperado vem da regra, não do código atual. Reinicie a agenda nos casos independentes; preserve o estado explicitamente nas sequências. Texto vazio e espaços somente são entradas distintas para RN03. Uma recusa não deve alterar reserva anterior. Não use “funcionou” como esperado nem aprove apenas porque nenhuma exceção ocorreu.

**Exemplo cotidiano:** Uma compra sem mensagem de erro ainda pode gerar pedido duplicado.

**Cenário empresarial:** QA vincula TC02 a RN05 e verifica conflito e preservação da reserva de Ana.

**Erros a observar:** Ausência de pré-condição; esperado vago; copiar observado para esperado.

**Orientação:** Definir resultado antes de executar e conferir estado final.

Distribua os 17 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Execute Ana/H09 e depois Bruno/H09; confira a preservação da primeira reserva.

**Exemplo 1:** TC03/RN03: agenda vazia; reservar espaços em H11; esperado nome_invalido e H11 livre. Referência rejeita; variante aceita e ocupa H11. Essa diferença é um defeito simulado, não incidente real.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Do requisito à evidência. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 2: Escrever e executar oito casos de teste**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Escrever e executar oito casos de teste, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Crie pelo menos um caso por regra RN01–RN08.
2. Inclua sucesso, conflito, espaços, horário inválido e cancelamento.
3. Registre quando a agenda será reiniciada.
4. Execute na referência e anote observado.
5. Compare o caso de espaços nas duas versões.

**Entrega esperada:** tabela com oito casos e registro de execução Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m04-atividade-02.md`.

**Critérios específicos:** Cobrir oito regras; especificar dados e estado; registrar versão e resultado.

**Exemplo de resposta comentada:** TC03/RN03: agenda vazia; reservar espaços em H11; esperado nome_invalido e H11 livre. Referência rejeita; variante aceita e ocupa H11. Essa diferença é um defeito simulado, não incidente real.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Crie um caso que valide preservação do estado após uma recusa.


## Exercício individual

Escreva o caso RN07 de cancelamento inexistente preservando outra reserva.

**Tempo:** 12 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- De onde vem o esperado?
- Quando reiniciar o estado?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Caso negativo é erro do teste? | Não; verifica uma recusa prevista. |
| Sem exceção significa aprovado? | Não; saída e estado precisam atender à regra. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: plano de testes, oito casos ligados a RN01–RN08, registro de execução das duas versões, BUG01 e evidência de reteste. A próxima aula amplia investigação e comunicação.

## Tarefa para casa

Revisar casos e executar nas versões disponíveis, identificando a evidência.

**Tempo sugerido:** 30–45 minutos. Entregar `m04-aula-02-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro.
