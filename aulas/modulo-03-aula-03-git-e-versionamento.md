# Roteiro de aula — Módulo 3, Aula 3

## Tema e objetivo da aula

**Tema:** Git e histórico local.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Criar três commits locais com intenção clara.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md), tópicos 3. **Pré-requisito:** entrega ou revisão da aula anterior; retomar qualquer lacuna com um exemplo simples.

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

Apresente a situação Agenda Clara e pergunte: “O arquivo salvo já pertence a um commit?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 20 minutos

### Git e versionamento local

**Conceito:** Git mantém histórico de mudanças selecionadas em um repositório.

**Explicação simples para falar à turma:** Salvar um arquivo muda seu conteúdo. Criar um commit registra uma versão que podemos identificar e comparar.

**Aprofundamento necessário:** O diretório de trabalho contém seus arquivos; a área de preparação reúne o que entrará no próximo commit; o histórico guarda os commits. Execute git status para observar, git add para selecionar e git commit para registrar. git diff mostra mudanças ainda não preparadas; git diff --staged mostra as preparadas. git log --oneline ajuda a localizar versões. Um arquivo não rastreado ainda não pertence ao histórico. Faça tudo em uma pasta de exercício, sem usar operações destrutivas de limpeza. Configure identidade de autor conforme a preferência de privacidade da conta.

**Exemplo cotidiano:** Um texto sem histórico permite ver apenas a versão atual; com commits podemos explicar a evolução da regra.

**Situação de empresa:** Dev registra a correção de RN03 separadamente da reformatação do README, permitindo revisão focada.

**Alerta didático:** Usar git add . sem inspecionar; registrar credenciais; mensagens como “coisas”. Oriente: Verificar status e diff, selecionar arquivos explicitamente e escrever propósito no commit.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 15 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Criar três commits locais com intenção clara.**

1. Crie uma pasta de laboratório e copie README e agenda_clara.py.
2. Execute git init e git status.
3. Adicione README e faça o primeiro commit.
4. Adicione simulador em outro commit; melhore a instrução de execução no terceiro.
5. Leia git log --oneline e explique cada versão.

**Resultado de referência:** Histórico esperado: apresentar projeto; adicionar simulador de reservas; esclarecer execução. Os hashes variam. O importante é que cada commit tenha mudança verificável e mensagem coerente.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 25 minutos

**Nome:** Revisão cruzada — Git e histórico local.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 3 minutos, ler o enunciado de cada atividade e identificar a regra ou premissa.
2. Em 10 minutos, executar as etapas abaixo e registrar o resultado.
3. Em 7 minutos, revisar o colega: localizar uma evidência, uma lacuna e uma proposta de correção.
4. Em 5 minutos, apresentar uma decisão e sua justificativa; com muitas duplas, selecionar duas e recolher as demais por escrito.

**Atividade 1 — Criar três commits locais com intenção clara.**

1. Crie uma pasta de laboratório e copie README e agenda_clara.py.
2. Execute git init e git status.
3. Adicione README e faça o primeiro commit.
4. Adicione simulador em outro commit; melhore a instrução de execução no terceiro.
5. Leia git log --oneline e explique cada versão.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** O arquivo salvo já pertence a um commit?

## Exercício individual — 20 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** O arquivo salvo já pertence a um commit? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 15 minutos

- O arquivo salvo já pertence a um commit?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **Git e versionamento local:** Histórico esperado: apresentar projeto; adicionar simulador de reservas; esclarecer execução. Os hashes variam. O importante é que cada commit tenha mudança verificável e mensagem coerente.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Git exige GitHub? | Não; o histórico local é criado e consultado sem hospedagem. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: repositório de portfólio com README, simulador, três commits com propósito e uma alteração revisada. A próxima aula amplia esse trabalho; mantenha as decisões e dúvidas registradas.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m03-aula-03-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Você alterou uma regra, mas o README continua descrevendo a versão anterior. Produza uma revisão que mantenha comportamento, documentação e evidência coerentes.

O professor verifica a revisão no início do próximo encontro. 

