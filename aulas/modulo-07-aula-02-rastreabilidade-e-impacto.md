# Roteiro — Módulo 7, Aula 2

## Tema e objetivo da aula

**Tema:** Rastreabilidade e impacto. **Objetivo observável:** ligar regras, histórias, testes e versões.

**Leitura:** [E-book do módulo](../ebooks/modulo-07-ciclo-de-vida-do-software.md), tópicos 2. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

RN, US, TC e BUG dos módulos 4 e 5. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Mude a regra do nome e pergunte o que precisa ser revisto. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Requisitos, desenvolvimento e rastreabilidade

**Conceito:** Rastreabilidade permite seguir uma necessidade até as evidências que sustentam sua implementação.

**Explicação simples:** Se a regra mudar, você precisa saber quais histórias, testes e documentos serão afetados.

**Aprofundamento:** Use IDs estáveis e relações úteis. RN03 está ligada a US02, TC03, BUG01 e versão corrigida. A matriz não precisa relacionar tudo com tudo; deve apoiar análise de cobertura e impacto. Link quebrado ou versão indefinida enfraquece evidência. Desenvolvimento deve preservar regra, documentação e histórico. Uma mudança de critério exige investigar código e casos derivados. Não conclua cobertura só por ter uma linha: conferir se o teste realmente verifica a regra e o estado.

**Exemplo cotidiano:** Um manual e o programa podem divergir após alteração de política.

**Cenário empresarial:** Time localiza rapidamente todos os artefatos afetados pela validação de espaços.

**Erros a observar:** IDs inconsistentes; matriz decorativa; evidência de versão errada.

**Orientação:** Poucos vínculos claros e revisão quando a regra muda.

Distribua os 20 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Monte cadeia RN03–US02–TC03–BUG01–versão.

**Exemplo 1:** RN03 → US02 → TC03 → BUG01 → referência para reteste. Se RN03 passar a exigir tamanho mínimo, casos e código atuais precisam revisão, sem afirmar que a regra nova já está coberta.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Seguir a mudança. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 3 minutos de leitura; 10 de execução; 7 de revisão cruzada; 5 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 2: Construir matriz de rastreabilidade**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Construir matriz de rastreabilidade, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Liste RN02, RN03 e RN06.
2. Ligue a histórias, testes e bugs aplicáveis.
3. Indique versão ou estado de verificação.
4. Escolha uma mudança e identifique impactos.

**Entrega esperada:** matriz com três regras e análise de mudança Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m07-atividade-02.md`.

**Critérios específicos:** Vínculos coerentes; evidência identificada; impacto explicado.

**Exemplo de resposta comentada:** RN03 → US02 → TC03 → BUG01 → referência para reteste. Se RN03 passar a exigir tamanho mínimo, casos e código atuais precisam revisão, sem afirmar que a regra nova já está coberta.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Como identificar uma regra sem teste e um teste sem regra?


## Exercício individual

Analise impacto de novo catálogo H12 e registre o que deixa de ser válido.

**Tempo:** 20 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual regra não tem teste?
- Qual versão sustenta a evidência?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Matriz garante cobertura? | Não; é preciso revisar o conteúdo do teste. |
| Preciso ligar tudo a tudo? | Não; use relações úteis e conferíveis. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: diagrama completo de SDLC, matriz de rastreabilidade, checklist de release simulada e plano de resposta a falha. Antecipar revisão reduz ambiguidades.

## Tarefa para casa

Revisar matriz e uma análise de impacto.

**Tempo sugerido:** 30–45 minutos. Entregar `m07-aula-02-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. 

