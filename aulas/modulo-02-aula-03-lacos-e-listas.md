# Roteiro de aula — Módulo 2, Aula 3

**Condução com falas prontas:** [script do professor](scripts/modulo-02-aula-03-lacos-e-listas.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Laços e listas.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Rastrear o filtro de horários livres.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-02-logica-de-programacao.md), tópicos 4. **Pré-requisito:** entrega ou revisão da aula anterior; retomar qualquer lacuna com um exemplo simples.

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

Se a turma precisar de mais tempo, reduza a extensão da variação, preserve a prática individual e conclua a revisão na aula seguinte.

## Materiais necessários

E-book, [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou folha com tabela, quadro e acesso ao [simulador](../portfolio/agenda-clara/README.md). Para código: Python 3. Para versionamento: Git e, quando houver publicação, conta GitHub. Jira/Azure DevOps são opcionais e podem ser representados por cartões. Teste os recursos antes da aula e prepare uma cópia de saída para discussão se houver indisponibilidade.

## Abertura da aula — 8 minutos

Apresente a situação Agenda Clara e pergunte: “O que deve acontecer quando a lista está vazia?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 17 minutos

### Laços for e while

**Conceito:** Laços repetem instruções sobre uma coleção ou enquanto uma condição permanece verdadeira.

**Explicação simples para falar à turma:** Para mostrar cada horário, passe por todos os itens. Para repetir uma tentativa, verifique quando deve parar.

**Aprofundamento necessário:** for percorre os elementos de uma coleção; while verifica uma condição a cada repetição. Um while precisa de progresso em direção à parada. Em Python, range(3) produz 0, 1 e 2; o limite superior não é incluído. Percorrer uma lista vazia com for executa zero iterações, o que pode ser correto. Registre contador e resultado em cada passo. Não altere a coleção percorrida sem entender os efeitos. Para filtrar horários, percorra o catálogo e adicione ao resultado apenas os que não estão ocupados.

**Exemplo cotidiano:** Uma lista de pedidos exige examinar cada pedido, inclusive quando nenhum existe.

**Situação de empresa:** Dev filtra a agenda; QA testa catálogo completo, um horário ocupado e todos ocupados.

**Alerta didático:** Laço infinito; esquecer atualização do contador; supor que sempre haverá um elemento. Oriente: Definir estado inicial, condição de parada e comportamento para lista vazia.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 17 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Rastrear o filtro de horários livres.**

1. Use catálogo H09, H10, H11 e ocupados H10.
2. Percorra cada item e anote se será adicionado.
3. Repita com todos ocupados.
4. Escreva um while de três tentativas e indique a atualização.

**Resultado de referência:** Resultado com H10 ocupado: [H09, H11]; com todos ocupados: []. Um contador iniciado em 0, condição tentativas < 3 e incremento de 1 realiza três iterações; sem incremento, não há parada.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 20 minutos

**Nome:** Revisão cruzada — Laços e listas.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 2 minutos, ler o recorte do enunciado no script e identificar a regra ou premissa.
2. Em 5 minutos, executar o recorte principal e registrar o resultado.
3. Em 5 minutos, trocar funções e revisar uma evidência, uma lacuna e uma correção.
4. Em 3 minutos, selecionar duas duplas para apresentar; recolher as demais por escrito.

**Atividade 1 — Rastrear o filtro de horários livres.**

1. Use catálogo H09, H10, H11 e ocupados H10.
2. Percorra cada item e anote se será adicionado.
3. Repita com todos ocupados.
4. Escreva um while de três tentativas e indique a atualização.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** O que deve acontecer quando a lista está vazia?

## Exercício individual — 12 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** O que deve acontecer quando a lista está vazia? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-02-logica-de-programacao.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 8 minutos

- O que deve acontecer quando a lista está vazia?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **Laços for e while:** Resultado com H10 ocupado: [H09, H11]; com todos ocupados: []. Um contador iniciado em 0, condição tentativas < 3 e incremento de 1 realiza três iterações; sem incremento, não há parada.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| for e while são equivalentes? | Muitos problemas podem usar ambos, mas for é mais direto para coleções e while para condições de continuidade. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: caderno de seis algoritmos com entradas, saídas e rastreamento, mais uma função de validação em Python ou pseudocódigo. A próxima aula amplia esse trabalho; mantenha as decisões e dúvidas registradas.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m02-aula-03-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Altere a política para permitir somente duas reservas por cliente. Descreva qual dado adicional falta; não invente uma solução que conte apenas horários.

O professor verifica a revisão no início do próximo encontro.
