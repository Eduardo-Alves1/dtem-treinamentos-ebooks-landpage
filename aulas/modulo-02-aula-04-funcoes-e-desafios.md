# Roteiro de aula — Módulo 2, Aula 4

## Tema e objetivo da aula

**Tema:** Funções e resolução de problemas.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Implementar e validar uma função de nome.; Investigar uma validação que aceita espaços.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-02-logica-de-programacao.md), tópicos 5, 6. **Pré-requisito:** entrega ou revisão da aula anterior; retomar qualquer lacuna com um exemplo simples.

## Duração sugerida

| Etapa | Minutos |
|---|---:|
| Abertura e diagnóstico | 10 |
| Explicação teórica com exemplos | 20 |
| Demonstração guiada | 15 |
| Pausa | 10 |
| Dinâmica em dupla ou grupo | 25 |
| Exercício individual | 20 |
| Perguntas, correção e fechamento | 15 |
| Orientação da tarefa de casa | 5 |
| Total | 120 |

Se a turma precisar de mais tempo, reduza a extensão da variação, preserve a prática individual e conclua a revisão na aula seguinte.

## Materiais necessários

E-book, [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou folha com tabela, quadro e acesso ao [simulador](../portfolio/agenda-clara/README.md). Para código: Python 3. Para versionamento: Git e, quando houver publicação, conta GitHub. Jira/Azure DevOps são opcionais e podem ser representados por cartões. Teste os recursos antes da aula e prepare uma cópia de saída para discussão se houver indisponibilidade.

## Abertura da aula — 10 minutos

Apresente a situação Agenda Clara e pergunte: “Quem deve decidir reservar um horário: validar_nome ou a operação de reserva?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 20 minutos

### Funções e responsabilidade

**Conceito:** Uma função encapsula uma operação que recebe parâmetros e pode retornar um resultado.

**Explicação simples para falar à turma:** Em vez de copiar a verificação do nome em vários lugares, damos a ela um nome e a reutilizamos.

**Aprofundamento necessário:** def define a função; parâmetros representam entradas; return entrega o resultado. print exibe texto e não substitui return. A função validar_nome deve apenas decidir se o texto é aceito, sem reservar horário ou mudar a agenda. Separar responsabilidades facilita testar. Para simplificar, considere entradas de texto; se aceitar outros tipos, valide-os explicitamente. Uma função sem return explícito retorna None em Python. Observe a diferença entre argumento passado na chamada e parâmetro declarado na definição.

**Exemplo cotidiano:** Um cálculo de frete reutilizável pode ser chamado tanto pelo carrinho quanto pela finalização da compra.

**Situação de empresa:** QA testa validar_nome sem precisar executar todo o processo de reserva; Dev evita copiar a mesma lógica.

**Alerta didático:** Usar print e tentar comparar o resultado; modificar dados sem anunciar; criar uma função que resolve tarefas desconexas. Oriente: Nomear pela responsabilidade, manter entradas e saídas claras e usar exemplos pequenos.

### Resolução de problemas e depuração inicial

**Conceito:** Depurar é investigar por que o comportamento observado difere do esperado.

**Explicação simples para falar à turma:** Em vez de mudar linhas ao acaso, descubra qual passo fez o resultado desviar.

**Aprofundamento necessário:** Defina uma regra, construa uma entrada que a exercita e compare saída e estado. Use uma tabela com passo, variável e resultado. Reproduza o problema antes de propor correção. Primeiro classifique: erro de sintaxe impede interpretar o programa; erro de execução interrompe uma operação; erro lógico pode produzir uma saída válida na forma, porém errada pela regra. Python e Portugol usam sintaxes diferentes: escolha uma linguagem para executar e trate a outra como alternativa didática, sem misturar comandos.

**Exemplo cotidiano:** Uma calculadora que apresenta um número incorreto pode ter executado sem travar; ausência de erro visível não prova correção.

**Situação de empresa:** Na AgendaComDefeito, espaços geram uma reserva. O problema é lógico, pois viola RN03 sem interromper a execução.

**Alerta didático:** Mudar várias regras de uma vez; comparar sem registrar entrada; usar apenas um exemplo positivo. Oriente: Reproduzir, reduzir o caso, formular hipótese, corrigir uma causa e repetir casos anteriores.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 15 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Implementar e validar uma função de nome.**

1. Defina validar_nome(nome).
2. Retorne bool(nome.strip()) para entrada textual.
3. Teste "Ana", "" e "   ".
4. Registre entrada e retorno e explique a diferença para print.

**Resultado de referência:** def validar_nome(nome): return bool(nome.strip()). Os resultados para as três entradas são True, False e False. A função pressupõe str; a classe de referência também protege contra outros tipos.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

**Demonstração 2: Investigar uma validação que aceita espaços.**

1. Compare nome != "" com bool(nome.strip()).
2. Rastreie ambas para "   ".
3. Formule uma hipótese do erro.
4. Escreva a correção e repita as três entradas da função anterior.

**Resultado de referência:** "   " != "" é True; bool("   ".strip()) é False. A primeira expressão confunde texto não vazio com conteúdo útil. A correção rejeita vazio e espaços e preserva nome válido.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 25 minutos

**Nome:** Revisão cruzada — Funções e resolução de problemas.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 3 minutos, ler o enunciado de cada atividade e identificar a regra ou premissa.
2. Em 10 minutos, executar as etapas abaixo e registrar o resultado.
3. Em 7 minutos, revisar o colega: localizar uma evidência, uma lacuna e uma proposta de correção.
4. Em 5 minutos, apresentar uma decisão e sua justificativa; com muitas duplas, selecionar duas e recolher as demais por escrito.

**Atividade 1 — Implementar e validar uma função de nome.**

1. Defina validar_nome(nome).
2. Retorne bool(nome.strip()) para entrada textual.
3. Teste "Ana", "" e "   ".
4. Registre entrada e retorno e explique a diferença para print.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Quem deve decidir reservar um horário: validar_nome ou a operação de reserva?

**Atividade 2 — Investigar uma validação que aceita espaços.**

1. Compare nome != "" com bool(nome.strip()).
2. Rastreie ambas para "   ".
3. Formule uma hipótese do erro.
4. Escreva a correção e repita as três entradas da função anterior.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Qual evidência confirma sua hipótese?

## Exercício individual — 20 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** Quem deve decidir reservar um horário: validar_nome ou a operação de reserva? Qual evidência confirma sua hipótese? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-02-logica-de-programacao.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 15 minutos

- Quem deve decidir reservar um horário: validar_nome ou a operação de reserva?
- Qual evidência confirma sua hipótese?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **Funções e responsabilidade:** def validar_nome(nome): return bool(nome.strip()). Os resultados para as três entradas são True, False e False. A função pressupõe str; a classe de referência também protege contra outros tipos.
- **Resolução de problemas e depuração inicial:** "   " != "" é True; bool("   ".strip()) é False. A primeira expressão confunde texto não vazio com conteúdo útil. A correção rejeita vazio e espaços e preserva nome válido.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Uma função precisa ser grande para ter utilidade? | Não; uma responsabilidade pequena costuma ser mais fácil de testar e reutilizar. |
| Posso concluir que corrigi após um caso? | Confira o caso que falhava e os casos que já funcionavam para avaliar efeitos colaterais. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: caderno de seis algoritmos com entradas, saídas e rastreamento, mais uma função de validação em Python ou pseudocódigo. Na próxima etapa, o aluno usará a entrega como evidência de base para o módulo seguinte.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m02-aula-04-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Altere a política para permitir somente duas reservas por cliente. Descreva qual dado adicional falta; não invente uma solução que conte apenas horários.

O professor verifica a revisão no início do próximo encontro. Solicitar também a organização da entrega final e a reflexão individual.

