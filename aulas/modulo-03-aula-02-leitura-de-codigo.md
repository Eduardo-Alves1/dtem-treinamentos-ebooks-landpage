# Roteiro de aula — Módulo 3, Aula 2

**Condução com falas prontas:** [script do professor](scripts/modulo-03-aula-02-leitura-de-codigo.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** Leitura de código e comportamento.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Rastrear duas chamadas do simulador.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md), tópicos 2. **Pré-requisito:** entrega ou revisão da aula anterior; retomar qualquer lacuna com um exemplo simples.

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

Apresente a situação Agenda Clara e pergunte: “Em qual ponto a chamada deixa de poder criar uma reserva?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 17 minutos

### Noções básicas e leitura de código

**Conceito:** Ler código é reconstruir seu comportamento a partir de entradas, decisões e mudanças de estado.

**Explicação simples para falar à turma:** Não precisamos escrever tudo para investigar: podemos acompanhar o que cada linha faz com um exemplo.

**Aprofundamento necessário:** Na classe Agenda, self.reservas é um dicionário que associa identificador a dados da reserva. O método consultar monta um conjunto de horários ocupados e filtra o catálogo. return encerra a operação e devolve seu resultado. Em reservar, observe as três recusas antes da criação. super().reservar na classe com defeito chama a implementação de referência depois de transformar a entrada. Você não precisa dominar orientação a objetos aqui; a classe serve para agrupar estado e operações. Comece pelo contrato público e aprofunde uma linha por vez.

**Exemplo cotidiano:** Ler uma regra de cálculo ajuda a distinguir um requisito inesperado de um erro de implementação.

**Situação de empresa:** QA usa a leitura para explicar por que espaços passam na variante defeituosa, sem inventar detalhes de um servidor inexistente.

**Alerta didático:** Adivinhar pelo nome da função; ignorar retorno antecipado; ler sem entrada concreta. Oriente: Anotar entrada, linha relevante, saída e mudança de estado.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 17 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Rastrear duas chamadas do simulador.**

1. Leia reservar na classe Agenda.
2. Acompanhe Ana/H09 em agenda vazia.
3. Acompanhe Bruno/H09 na mesma agenda.
4. Localize a linha que impede a segunda reserva.

**Resultado de referência:** A primeira reserva recebe id 1. A segunda encontra H09 fora de consultar() e retorna conflito antes de adicionar dados. O dicionário conserva uma única reserva.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 20 minutos

**Nome:** Revisão cruzada — Leitura de código e comportamento.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 2 minutos, ler o recorte do enunciado no script e identificar a regra ou premissa.
2. Em 5 minutos, executar o recorte principal e registrar o resultado.
3. Em 5 minutos, trocar funções e revisar uma evidência, uma lacuna e uma correção.
4. Em 3 minutos, selecionar duas duplas para apresentar; recolher as demais por escrito.

**Atividade 1 — Rastrear duas chamadas do simulador.**

1. Leia reservar na classe Agenda.
2. Acompanhe Ana/H09 em agenda vazia.
3. Acompanhe Bruno/H09 na mesma agenda.
4. Localize a linha que impede a segunda reserva.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Em qual ponto a chamada deixa de poder criar uma reserva?

## Exercício individual — 12 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** Em qual ponto a chamada deixa de poder criar uma reserva? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 8 minutos

- Em qual ponto a chamada deixa de poder criar uma reserva?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **Noções básicas e leitura de código:** A primeira reserva recebe id 1. A segunda encontra H09 fora de consultar() e retorna conflito antes de adicionar dados. O dicionário conserva uma única reserva.

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Preciso entender classes para começar? | Entenda primeiro entradas, saídas e estado; aprofundamento de orientação a objetos fica para uma trilha de desenvolvimento. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: repositório de portfólio com README, simulador, três commits com propósito e uma alteração revisada. A próxima aula amplia esse trabalho; mantenha as decisões e dúvidas registradas.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m03-aula-02-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Você alterou uma regra, mas o README continua descrevendo a versão anterior. Produza uma revisão que mantenha comportamento, documentação e evidência coerentes.

O professor verifica a revisão no início do próximo encontro.
