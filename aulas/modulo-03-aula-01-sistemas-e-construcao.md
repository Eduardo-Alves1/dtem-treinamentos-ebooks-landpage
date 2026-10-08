# Roteiro de aula — Módulo 3, Aula 1

**Condução com falas prontas:** [script do professor](scripts/modulo-03-aula-01-sistemas-e-construcao.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Sistemas e construção de software.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Desenhar os componentes do laboratório.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md), tópicos 1. **Pré-requisito:** algoritmos e condições do Módulo 2; arquivo de texto salvo e localizado no computador.

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

Apresente a situação Agenda Clara e pergunte: “Qual componente falta para preservar reservas entre execuções?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 17 minutos

### O que é um sistema e como é construído

**Conceito:** Um sistema reúne componentes que recebem entradas, executam regras e produzem resultados para um objetivo.

**Explicação simples para falar à turma:** A tela é uma parte da solução. A reserva também depende de regras e de algum lugar onde o estado seja mantido.

**Aprofundamento necessário:** Separe interface, regra de negócio, integração e armazenamento. O simulador Agenda Clara implementa regras e estado em memória; não tem interface web nem banco persistente. Em um produto maior, requisitos orientam o desenho, código implementa o comportamento e testes verificam exemplos e riscos. Construção é iterativa: uma descoberta pode exigir voltar à regra. Um protótipo pode validar interação sem implementar toda a lógica, enquanto um programa de linha de comando pode executar regras sem uma tela gráfica.

**Exemplo cotidiano:** Em uma compra online, fechar o navegador não deveria apagar um pedido persistido; no simulador, encerrar o processo perde as reservas.

**Situação de empresa:** Produto e Dev combinam qual parte do MVP será executável e qual parte continuará ilustrada; QA registra essa limitação no plano.

**Alerta didático:** Confundir protótipo com produto pronto; chamar armazenamento em memória de banco persistente. Oriente: Descrever componentes existentes, ausentes e dependências antes de demonstrar.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 17 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Desenhar os componentes do laboratório.**

1. Leia o README do simulador.
2. Identifique entrada, regra e estado.
3. Desenhe uma possível interface futura sem afirmar que existe.
4. Registre o efeito de encerrar o processo.

**Resultado de referência:** Entrada por chamadas Python; regras na classe Agenda; estado em reservas; saída em dicionários. Uma interface futura chamaria a regra. Encerrar a execução perde o estado porque não há persistência.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 20 minutos

**Nome:** Revisão cruzada — Sistemas e construção de software.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 2 minutos, ler o recorte do enunciado no script e identificar a regra ou premissa.
2. Em 5 minutos, executar o recorte principal e registrar o resultado.
3. Em 5 minutos, trocar funções e revisar uma evidência, uma lacuna e uma correção.
4. Em 3 minutos, selecionar duas duplas para apresentar; recolher as demais por escrito.

**Atividade 1 — Desenhar os componentes do laboratório.**

1. Leia o README do simulador.
2. Identifique entrada, regra e estado.
3. Desenhe uma possível interface futura sem afirmar que existe.
4. Registre o efeito de encerrar o processo.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Qual componente falta para preservar reservas entre execuções?

## Exercício individual — 12 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** Qual componente falta para preservar reservas entre execuções? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 8 minutos

- Qual componente falta para preservar reservas entre execuções?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **O que é um sistema e como é construído:** Entrada por chamadas Python; regras na classe Agenda; estado em reservas; saída em dicionários. Uma interface futura chamaria a regra. Encerrar a execução perde o estado porque não há persistência.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Todo sistema tem tela? | Não; serviços e rotinas podem receber entradas por chamadas ou arquivos. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: repositório de portfólio com README, simulador, três commits com propósito e uma alteração revisada. A próxima aula amplia esse trabalho; mantenha as decisões e dúvidas registradas.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m03-aula-01-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Você alterou uma regra, mas o README continua descrevendo a versão anterior. Produza uma revisão que mantenha comportamento, documentação e evidência coerentes.

O professor verifica a revisão no início do próximo encontro.
