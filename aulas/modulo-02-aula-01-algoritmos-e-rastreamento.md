# Roteiro de aula — Módulo 2, Aula 1

**Condução com falas prontas:** [script do professor para até 90 minutos](scripts/modulo-02-aula-01-algoritmos-e-rastreamento.md). O script detalha o que falar, mostrar, perguntar e corrigir. Esta aula foi adaptada ao encontro semanal de 90 minutos; o professor usa a gravação para revisão posterior, sem exigir vídeos prévios.

## Tema e objetivo da aula

**Tema:** Algoritmos e rastreamento.

**Objetivo observável:** ao final, cada aluno escreverá um algoritmo de reserva e rastreará tentativas válidas e recusadas, sem código. A explicação deve distinguir entrada, processamento, saída e estado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-02-logica-de-programacao.md), tópicos 1. **Pré-requisito:** mapa mental do Módulo 1 e capacidade de explicar entrada, processamento e saída.

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

E-book, [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou folha com tabela e quadro compartilhado. Esta aula usa rastreamento manual: não exige Python, Git, GitHub ou ferramenta de gestão. O [simulador](../portfolio/agenda-clara/README.md) é referência opcional para o professor, sem antecipar a leitura de código.

## Abertura da aula — 8 minutos

Apresente a situação Agenda Clara e pergunte: “Se a segunda tentativa falhar, por que o estado anterior deve permanecer?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 17 minutos

### Algoritmos e lógica básica

**Conceito:** Um algoritmo descreve uma sequência de passos com entradas, decisões e resultados definidos.

**Explicação simples para falar à turma:** Uma receita pode orientar um iniciante, mas “faça uma reserva” é amplo demais. Precisamos dizer o que verificar e o que fazer quando a verificação falha.

**Aprofundamento necessário:** Defina entrada (nome e horário), pré-condição (catálogo disponível), processamento (validar e verificar ocupação) e saída (sucesso ou motivo de recusa). A ordem interfere no resultado: não ocupe um horário antes de validar o nome. Um algoritmo pode estar em linguagem natural, fluxograma ou pseudocódigo; nenhum deles exige conhecer sintaxe de Python. Rastrear significa executar os passos manualmente, anotando o estado após cada mudança. Terminação e clareza são importantes: um procedimento que manda “tentar de novo” sem uma condição de parada precisa ser revisto.

**Exemplo cotidiano:** Ao comprar um ingresso, selecionar uma sessão não significa que o assento já esteja reservado.

**Situação de empresa:** Produto explicita RN02 e QA verifica o que acontece na segunda tentativa de reservar H09. Dev transforma a decisão em comportamento executável.

**Alerta didático:** Pular o caso de erro; confundir um desejo de negócio com passos executáveis; escrever “verificar” sem informar como reagir. Oriente: Escrever verbos concretos, registrar entradas e testar manualmente uma situação positiva e uma negativa.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 20 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Desenhar o algoritmo de reserva sem escrever código.**

1. Leia RN01 a RN05 e RN08 no caderno do caso.
2. Escreva entradas, três verificações e saídas possíveis.
3. Percorra Ana/H09 e depois Bruno/H09 mantendo a primeira reserva.
4. Anote o estado do horário depois de cada tentativa.

**Resultado de referência:** Ana/H09 valida nome e catálogo, encontra horário livre e ocupa H09. Bruno/H09 valida as mesmas entradas, encontra H09 ocupado e retorna conflito. H09 continua reservado para Ana; a recusa não pode apagar a primeira reserva.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 15 minutos

**Nome:** Revisão cruzada — Algoritmos e rastreamento.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 2 minutos, ler as regras e preparar a tabela.
2. Em 5 minutos, rastrear Lia/H10 e Rui/H10 na mesma agenda, inicialmente vazia.
3. Em 5 minutos, trocar os papéis, conferir nome somente com espaços/H11 e revisar.
4. Em 3 minutos, recolher conclusões de duas duplas e receber as demais por escrito.

**Atividade 1 — Desenhar o algoritmo de reserva sem escrever código.**

1. Leia RN01 a RN05 e RN08 no caderno do caso.
2. Escreva entradas, três verificações e saídas possíveis.
3. Percorra Lia/H10 e depois Rui/H10 mantendo a primeira reserva; depois avalie nome somente com espaços/H11.
4. Anote o estado do horário depois de cada tentativa.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Se a segunda tentativa falhar, por que o estado anterior deve permanecer?

## Exercício individual — 12 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** em uma nova agenda, H10 está ocupado por Carla; H09 e H11 estão livres. Rastrear Rui/H10, nome somente com espaços/H09 e Dani/H11, nessa ordem. Registrar o passo decisivo, a saída e o estado depois. Explicar uma decisão e uma recusa. A referência detalhada está no script do professor.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-02-logica-de-programacao.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 8 minutos

- Se a segunda tentativa falhar, por que o estado anterior deve permanecer?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **Algoritmos e lógica básica:** Ana/H09 valida nome e catálogo, encontra horário livre e ocupa H09. Bruno/H09 valida as mesmas entradas, encontra H09 ocupado e retorna conflito. H09 continua reservado para Ana; a recusa não pode apagar a primeira reserva.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Posso começar pelo fluxograma? | Sim; depois confira se cada decisão tem caminhos e resultados definidos. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: caderno de seis algoritmos com entradas, saídas e rastreamento, mais uma função de validação em Python ou pseudocódigo. A próxima aula amplia esse trabalho; mantenha as decisões e dúvidas registradas.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m02-aula-01-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Altere a política para permitir somente duas reservas por cliente. Descreva qual dado adicional falta; não invente uma solução que conte apenas horários.

O professor verifica a revisão no início do próximo encontro.
