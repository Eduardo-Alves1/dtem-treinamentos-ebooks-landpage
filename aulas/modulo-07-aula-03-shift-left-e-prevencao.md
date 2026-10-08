# Roteiro — Módulo 7, Aula 3

## Tema e objetivo da aula

**Tema:** Shift Left e prevenção. **Objetivo observável:** refinar regra antes do código e manter plano de verificação.

**Leitura:** [E-book do módulo](../ebooks/modulo-07-ciclo-de-vida-do-software.md), tópicos 3. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

enunciado vago e exemplos. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Apresente “nome obrigatório” e peça interpretações. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Testes antecipados e Shift Left

**Conceito:** Shift left antecipa feedback e prevenção de defeitos para momentos anteriores da construção.

**Explicação simples:** Pergunte sobre nomes compostos por espaços antes de implementar a reserva.

**Aprofundamento:** Revisar requisitos, exemplos, protótipos e código gera informação antes do teste final. Antecipar não significa remover testes posteriores. No caso, uma conversa sobre nome útil revelaria a diferença entre não vazio e não composto por espaços. Testabilidade pede condição observável; requisito vago precisa de refinamento. Organize uma revisão em três perspectivas: valor, viabilidade e verificabilidade. Avalie o custo de detectar ambiguidade cedo, sem inventar percentuais universais de economia.

**Exemplo cotidiano:** Revisar uma instrução antes de imprimir evita repetir o erro em todos os exemplares.

**Cenário empresarial:** PO, Dev e QA alinham exemplos de RN03; depois verificam execução na versão entregue.

**Erros a observar:** Shift left como ferramenta específica; usar revisão para dispensar execução.

**Orientação:** Exemplos cedo, hipóteses explícitas e testes posteriores relevantes.

Distribua os 20 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Mostre vazio, espaços e nome válido; escreva critério.

**Exemplo 1:** Nome textual com conteúdo após strip. Exemplos: Ana aceita; vazio e espaços recusados. Rever antes do código e testar depois retorno e ausência de alteração de estado.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Três perspectivas. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 3 minutos de leitura; 10 de execução; 7 de revisão cruzada; 5 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 3: Realizar revisão antecipada de uma regra**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Realizar revisão antecipada de uma regra, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Leia “nome obrigatório” sem exemplos.
2. Liste ambiguidades de vazio, espaços e tipos.
3. Proponha critérios verificáveis.
4. Defina testes e quem precisa participar.
5. Registre o que ainda será conferido após implementar.

**Entrega esperada:** regra refinada, exemplos e plano de verificação Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m07-atividade-03.md`.

**Critérios específicos:** Ambiguidade identificada; exemplo verificável; execução posterior preservada.

**Exemplo de resposta comentada:** Nome textual com conteúdo após strip. Exemplos: Ana aceita; vazio e espaços recusados. Rever antes do código e testar depois retorno e ausência de alteração de estado.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Qual ambiguidade só seria descoberta ao observar a operação?


## Exercício individual

Revise “cancelamento simples” com dois critérios verificáveis.

**Tempo:** 20 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual ambiguidade foi removida?
- Qual teste posterior permanece?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Shift left é ferramenta? | É antecipação de feedback e prevenção. |
| Substitui teste final? | Não; complementa verificações posteriores. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: diagrama completo de SDLC, matriz de rastreabilidade, checklist de release simulada e plano de resposta a falha. Release exige critérios e resposta a falhas.

## Tarefa para casa

Revisar regra e registrar decisão.

**Tempo sugerido:** 30–45 minutos. Entregar `m07-aula-03-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. 

