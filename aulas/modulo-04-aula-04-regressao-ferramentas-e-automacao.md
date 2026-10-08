# Roteiro — Módulo 4, Aula 4

**Condução com falas prontas:** [script do professor](scripts/modulo-04-aula-04-regressao-ferramentas-e-automacao.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Regressão, ferramentas e automação. **Objetivo observável:** executar regressão e organizar um fluxo de defeito.

**Leitura:** [E-book do módulo](../ebooks/modulo-04-qualidade-de-software.md), tópicos 5, 6. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

referência, tabela de execução e cartões ou ferramenta. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Pergunte como provar que corrigir um nome não prejudicou cancelamento. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### Reteste, regressão e decisão de liberação

**Conceito:** Reteste confere a correção específica; regressão investiga efeitos adversos em comportamentos existentes.

**Explicação simples:** Depois de corrigir espaços, confira também se reserva e cancelamento continuam funcionando.

**Aprofundamento:** Selecione regressão por impacto e risco. Reteste de BUG01 repete os dados originais na versão corrigida; regressão cobre nome válido, conflito, cancelamento e horário fora do catálogo. Status não executado e bloqueado não equivalem a aprovado. Evidência de uma versão anterior não sustenta a versão atual. A referência serve como versão sem o defeito plantado, sem afirmar que é um produto pronto. Um parecer deve dizer decisão, base, limites e riscos residuais.

**Exemplo cotidiano:** Corrigir um desconto pode alterar cálculo de reembolso.

**Cenário empresarial:** Time usa RN02, RN03 e RN06 para decidir uma release apenas do escopo sequencial simulado.

**Erros a observar:** Chamar reteste de regressão completa; reutilizar evidência antiga.

**Orientação:** Identificar versão, áreas afetadas e riscos ainda abertos.

### Jira, Azure DevOps e conceito de automação

**Conceito:** Ferramentas organizam registros; automação repete verificações por instruções programadas.

**Explicação simples:** Um cartão acompanha o bug. Um script repete uma comparação. Pessoas ainda decidem o que importa.

**Aprofundamento:** Represente título, descrição, responsável, estado e vínculos. Tipos e campos de Jira e Azure DevOps variam por configuração; use documentação oficial, sem depender de uma tela específica. Em Markdown, simule o mesmo fluxo. Automação envolve preparar estado, chamar operação, comparar saída e reiniciar. Uma asserção como assert agenda.reservar("", "H09")["status"] == "nome_invalido" demonstra a comparação. Use agenda nova. Esta aula introduz a ideia, sem exigir domínio de framework. Fechar um bug precisa de reteste e evidência, não apenas mudança de coluna.

**Exemplo cotidiano:** Uma conferência automática pode repetir valores enquanto a pessoa investiga uma experiência nova.

**Cenário empresarial:** O time relaciona BUG01, RN03 e TC03 e confere transições com evidências.

**Erros a observar:** Automatizar regra indefinida; achar que ferramenta define o processo.

**Orientação:** IDs estáveis, vínculos e transições explícitas; automatizar verificações repetitivas.

Distribua os 17 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Reteste espaços, rode reserva/cancelamento e apresente a comparação automática.

**Exemplo 1:** Se os quatro passam, pode liberar a demonstração sequencial das regras cobertas. Não autoriza uso real: concorrência, segurança e persistência permanecem sem validação.

**Exemplo 2:** Criar Agenda; reservar espaços; comparar status com nome_invalido. Na variante a comparação falha. BUG01 passa para validado apenas após reteste na versão indicada.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Da correção à decisão. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 5: Executar suíte mínima e emitir parecer**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Executar suíte mínima e emitir parecer, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Selecione reteste de espaços, reserva válida, conflito e cancelar/re-reservar.
2. Justifique cada escolha.
3. Execute na referência e registre resultados.
4. Declare liberar, bloquear ou condicionar.
5. Indique duas limitações da decisão.

**Entrega esperada:** registro de quatro sequências e parecer de qualidade Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m04-atividade-05.md`.

**Critérios específicos:** Distinguir reteste e regressão; decisão sustentada por versão e resultados.

**Exemplo de resposta comentada:** Se os quatro passam, pode liberar a demonstração sequencial das regras cobertas. Não autoriza uso real: concorrência, segurança e persistência permanecem sem validação.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Um caso crítico ficou bloqueado. Como isso muda seu parecer?

**Atividade 6: Organizar BUG01 e uma verificação automática conceitual**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Organizar BUG01 e uma verificação automática conceitual, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Crie estados aberto, em análise, corrigido e validado.
2. Defina o que permite cada transição.
3. Vincule BUG01 a RN03 e TC03.
4. Escreva preparar, executar e comparar em Python ou pseudocódigo.

**Entrega esperada:** fluxo de cartões e verificação com esperado explícito Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m04-atividade-06.md`.

**Critérios específicos:** Bug validado somente após evidência; automação tem estado e comparação.

**Exemplo de resposta comentada:** Criar Agenda; reservar espaços; comparar status com nome_invalido. Na variante a comparação falha. BUG01 passa para validado apenas após reteste na versão indicada.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Qual informação não pode ser perdida ao migrar um cartão entre ferramentas?


## Exercício individual

Emita parecer para uma versão com caso crítico bloqueado e explique sua decisão.

**Tempo:** 12 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Qual evidência fecha o bug?
- O que o script não decide?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Reteste basta? | Não para analisar efeitos adversos; selecione regressão por risco. |
| Preciso de Jira pago? | Não; reproduza o fluxo com cartões ou Markdown. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: plano de testes, oito casos ligados a RN01–RN08, registro de execução das duas versões, BUG01 e evidência de reteste. O módulo de Produto aprofunda a origem das regras.

## Tarefa para casa

Consolidar plano, oito casos, BUG01, reteste e parecer.

**Tempo sugerido:** 30–45 minutos. Entregar `m04-aula-04-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. Organizar também a entrega final e a reflexão individual.
