# Roteiro de aula — Módulo 2, Aula 2

## Tema e objetivo da aula

**Tema:** Variáveis, tipos e decisões.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Montar um dicionário de dados inicial do produto.; Criar uma tabela de decisão de validação.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-02-logica-de-programacao.md), tópicos 2, 3. **Pré-requisito:** entrega ou revisão da aula anterior; retomar qualquer lacuna com um exemplo simples.

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

Apresente a situação Agenda Clara e pergunte: “Qual informação se perde se H09 virar apenas 9?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 20 minutos

### Variáveis e tipos de dados

**Conceito:** Variáveis associam nomes a valores usados para representar informações durante a execução.

**Explicação simples para falar à turma:** Uma ficha “nome = Ana” guarda uma informação; outra ficha “reservas = 1” guarda uma quantidade. Não usamos as duas da mesma forma.

**Aprofundamento necessário:** Em Python, texto é str, inteiro é int, verdadeiro/falso é bool e uma sequência de elementos pode ser list. A atribuição usa =; comparação de igualdade usa ==. “2” é texto, enquanto 2 é inteiro: comparar ou somar esses valores exige decidir a conversão. Escolha nomes que expliquem o dado. Uma lista como ["H09", "H10"] preserva elementos separados; a string "H09,H10" ainda é um único texto. Valores mudam durante a execução, então uma tabela de rastreamento deve mostrar antes e depois. Evite ponto flutuante para dinheiro neste módulo; o caso não envolve pagamentos.

**Exemplo cotidiano:** Um formulário coleta uma quantidade, mas pode recebê-la como texto; o sistema precisa validar e converter antes de calcular.

**Situação de empresa:** Dados separa contagem de reservas de rótulos de horários. H09 é identificador textual, não o número nove.

**Alerta didático:** Somar textos esperando soma numérica; usar = como comparação; tratar nome como identificador único de cliente. Oriente: Escolher tipos a partir da operação necessária e mostrar dados inválidos separadamente.

### Condições e operadores

**Conceito:** Condições permitem selecionar um caminho conforme uma expressão verdadeira ou falsa.

**Explicação simples para falar à turma:** Se o nome estiver vazio, recuse. Caso contrário, continue verificando o horário.

**Aprofundamento necessário:** if executa um bloco quando sua condição é verdadeira; elif permite outra condição e else cobre o restante. and exige todas as condições; or aceita pelo menos uma; not inverte o valor lógico. Em Python, indentação delimita blocos. nome.strip() remove espaços das extremidades; bool(nome.strip()) é falso para vazio e espaços somente. Compare casos de fronteira e entradas diferentes. Não conclua que uma mensagem visual prova a aplicação correta de uma regra no servidor: aqui estamos estudando o algoritmo de validação, não a segurança de uma aplicação web.

**Exemplo cotidiano:** Um cupom pode exigir compra mínima e prazo válido simultaneamente; usar or nesse caso permitiria descontos indevidos.

**Situação de empresa:** QA constrói uma tabela de decisão para RN03 e RN08; Produto confirma qual erro deve ser comunicado quando há mais de uma entrada inválida.

**Alerta didático:** Trocar and por or; esquecer espaços; permitir alteração de estado no ramo de erro. Oriente: Usar tabela de decisão e um resultado explícito por ramo.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 15 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Montar um dicionário de dados inicial do produto.**

1. Liste nome, horário, quantidade de reservas e agenda disponível.
2. Defina tipo, exemplo e restrição para cada dado.
3. Compare 2 + 3 com "2" + "3".
4. Explique por que H09 deve permanecer como texto.

**Resultado de referência:** nome: texto não vazio após strip; horario: texto pertencente ao catálogo; quantidade: inteiro não negativo; disponíveis: lista de textos. 2 + 3 resulta em 5 e a concatenação dos textos resulta em "23".

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

**Demonstração 2: Criar uma tabela de decisão de validação.**

1. Combine nome válido/inválido com horário no/fora do catálogo.
2. Escreva as quatro combinações.
3. Escolha uma ordem de validação e registre-a.
4. Explique o resultado quando ambas as entradas são inválidas.

**Resultado de referência:** Nome válido + H09 pode continuar para verificar ocupação; nome válido + H12 retorna horario_invalido; vazio + H09 retorna nome_invalido; vazio + H12 também retorna nome_invalido se nome for a primeira validação. A ordem precisa ser documentada.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 25 minutos

**Nome:** Revisão cruzada — Variáveis, tipos e decisões.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 3 minutos, ler o enunciado de cada atividade e identificar a regra ou premissa.
2. Em 10 minutos, executar as etapas abaixo e registrar o resultado.
3. Em 7 minutos, revisar o colega: localizar uma evidência, uma lacuna e uma proposta de correção.
4. Em 5 minutos, apresentar uma decisão e sua justificativa; com muitas duplas, selecionar duas e recolher as demais por escrito.

**Atividade 1 — Montar um dicionário de dados inicial do produto.**

1. Liste nome, horário, quantidade de reservas e agenda disponível.
2. Defina tipo, exemplo e restrição para cada dado.
3. Compare 2 + 3 com "2" + "3".
4. Explique por que H09 deve permanecer como texto.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Qual informação se perde se H09 virar apenas 9?

**Atividade 2 — Criar uma tabela de decisão de validação.**

1. Combine nome válido/inválido com horário no/fora do catálogo.
2. Escreva as quatro combinações.
3. Escolha uma ordem de validação e registre-a.
4. Explique o resultado quando ambas as entradas são inválidas.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** A condição foi atendida ou o sistema apenas exibiu uma mensagem?

## Exercício individual — 20 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** Qual informação se perde se H09 virar apenas 9? A condição foi atendida ou o sistema apenas exibiu uma mensagem? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-02-logica-de-programacao.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 15 minutos

- Qual informação se perde se H09 virar apenas 9?
- A condição foi atendida ou o sistema apenas exibiu uma mensagem?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **Variáveis e tipos de dados:** nome: texto não vazio após strip; horario: texto pertencente ao catálogo; quantidade: inteiro não negativo; disponíveis: lista de textos. 2 + 3 resulta em 5 e a concatenação dos textos resulta em "23".
- **Condições e operadores:** Nome válido + H09 pode continuar para verificar ocupação; nome válido + H12 retorna horario_invalido; vazio + H09 retorna nome_invalido; vazio + H12 também retorna nome_invalido se nome for a primeira validação. A ordem precisa ser documentada.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Tipo é escolhido pelo formato que vejo? | Não apenas; considere o significado e as operações, pois um código numérico pode continuar sendo texto. |
| Preciso usar else sempre? | Não; um retorno antecipado pode encerrar o ramo de erro e simplificar a função. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: caderno de seis algoritmos com entradas, saídas e rastreamento, mais uma função de validação em Python ou pseudocódigo. A próxima aula amplia esse trabalho; mantenha as decisões e dúvidas registradas.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m02-aula-02-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Altere a política para permitir somente duas reservas por cliente. Descreva qual dado adicional falta; não invente uma solução que conte apenas horários.

O professor verifica a revisão no início do próximo encontro. 

