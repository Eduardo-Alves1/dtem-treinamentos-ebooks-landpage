# Roteiro de aula — Módulo 3, Aula 4

**Condução com falas prontas:** [script do professor](scripts/modulo-03-aula-04-github-e-colaboracao.md). Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.

## Tema e objetivo da aula

**Tema:** GitHub, revisão e publicação.

**Objetivo observável:** ao final, cada aluno produzirá e explicará: Publicar e verificar o primeiro projeto.; Revisar uma melhoria de documentação.. A explicação deve citar a regra, a entrada ou premissa e o resultado; o professor pode conferir o artefato sem depender de memória da apresentação.

**Leitura:** [E-book do módulo](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md), tópicos 4, 5. **Pré-requisito:** entrega ou revisão da aula anterior; retomar qualquer lacuna com um exemplo simples.

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

Apresente a situação Agenda Clara e pergunte: “Uma pessoa que nunca viu sua aula consegue executar o projeto?” Dê dois minutos para cada aluno escrever sua previsão. Recolha duas respostas distintas e identifique a evidência que seria necessária para decidir. Retome um conceito da aula anterior e explique a entrega de hoje em linguagem simples.

## Explicação teórica e exemplos práticos — 17 minutos

### GitHub e primeiro projeto publicado

**Conceito:** GitHub hospeda repositórios e oferece recursos de colaboração sobre históricos Git.

**Explicação simples para falar à turma:** Git organiza o histórico no seu computador; GitHub permite compartilhar uma cópia e receber contribuições.

**Aprofundamento necessário:** Crie um repositório vazio na conta escolhida, sem README automático quando estiver conectando um histórico local existente. Confira o endereço remoto antes de usar git remote add origin e envie a branch correta com git push -u origin main, após verificar seu nome com git branch --show-current. Se a branch local tiver outro nome, use esse nome ou renomeie conscientemente com git branch -M main. Autenticação deve seguir a documentação da plataforma; não incluir tokens no Markdown. Para iniciantes, a interface de upload pode ser uma alternativa, mas registre que ela não demonstra todas as operações locais de Git.

**Exemplo cotidiano:** Compartilhar uma pasta por mensagem não oferece a mesma discussão de mudanças que um repositório com histórico.

**Situação de empresa:** O aluno publica um laboratório fictício para que um colega consiga executar usando somente o README.

**Alerta didático:** Criar README remoto e ignorar históricos divergentes; compartilhar segredo; copiar URL sem verificar a conta. Oriente: Conferir visibilidade, arquivos e instruções; usar dados fictícios e revisar o conteúdo publicado.

### Branches, revisão e colaboração

**Conceito:** Uma mudança colaborativa precisa ser compreensível antes de ser integrada.

**Explicação simples para falar à turma:** Prepare uma proposta em separado, mostre o que mudou e explique como verificou.

**Aprofundamento necessário:** Crie uma branch de exercício com git switch -c docs/execucao, modifique uma instrução, registre o commit e envie a branch. Abra uma proposta de integração para a branch principal. O revisor lê o diff e verifica problema, resultado e evidência. Se duas pessoas mudarem a mesma região, pode haver conflito: preserve a intenção de ambas, edite a versão final e execute a verificação. Não resolva apenas escolhendo “tudo meu” ou “tudo do outro”. Uma proposta documental pode ser simples; alterações de comportamento exigem cenários relevantes.

**Exemplo cotidiano:** Editar um manual em grupo exige discutir qual instrução é correta, não somente qual arquivo é mais recente.

**Situação de empresa:** QA revisa exemplos de entrada enquanto Dev revisa o código; Produto verifica se a regra ficou clara.

**Alerta didático:** Aprovar sem ler; misturar muitas mudanças; tratar revisão como julgamento pessoal. Oriente: Propostas pequenas, descrição do problema e critério de aceitação observável.

Após cada conceito, peça ao aluno um exemplo com suas próprias palavras. Corrija uma generalização usando a regra do caso, sem antecipar todos os resultados.

## Demonstração guiada — 17 minutos

O professor modela a primeira atividade, pensando em voz alta. Se houver dois temas, faça uma passagem curta pelo segundo e deixe a resolução completa para a prática.

**Demonstração 1: Publicar e verificar o primeiro projeto.**

1. Crie o repositório e escolha a visibilidade conscientemente.
2. Envie o histórico ou use upload como alternativa declarada.
3. Confira README, código e commits na página.
4. Peça a um colega para localizar a instrução de execução.
5. Registre URL e uma captura sem dados sensíveis.

**Resultado de referência:** Entrega contém URL acessível ao avaliador, README com contexto fictício, instruções e limites, código e histórico. Repositório privado precisa ter acesso concedido ao avaliador; link sozinho não prova acessibilidade.

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

**Demonstração 2: Revisar uma melhoria de documentação.**

1. Crie a branch e melhore o comando de execução.
2. Abra a proposta de integração ou produza um diff local comentado.
3. Peça ao colega para identificar um risco ou dúvida.
4. Responda e integre somente após conferir a versão final.

**Resultado de referência:** Descrição de referência: “A instrução dependia da pasta atual. Agora indica executar a partir da raiz ou entrar na pasta do simulador. Verificação: o caminho resolve em ambos os casos documentados.”

Antes de revelar o resultado, pare e peça uma previsão. Depois, marque no quadro qual passo sustenta a resposta. Se a saída diferir, registre e investigue a entrada ou estado em vez de ajustar a resposta verbalmente.

## Dinâmica em grupo — 20 minutos

**Nome:** Revisão cruzada — GitHub, revisão e publicação.

**Contexto profissional:** o time precisa verificar uma decisão antes de entregar uma versão. Em duplas, uma pessoa produz e outra revisa; na metade do tempo, troquem os papéis. Em aula remota, usar salas ou comentários no documento. Em grupo maior, designar também uma pessoa para registrar decisões.

1. Em 2 minutos, ler o recorte do enunciado no script e identificar a regra ou premissa.
2. Em 5 minutos, executar o recorte principal e registrar o resultado.
3. Em 5 minutos, trocar funções e revisar uma evidência, uma lacuna e uma correção.
4. Em 3 minutos, selecionar duas duplas para apresentar; recolher as demais por escrito.

**Atividade 1 — Publicar e verificar o primeiro projeto.**

1. Crie o repositório e escolha a visibilidade conscientemente.
2. Envie o histórico ou use upload como alternativa declarada.
3. Confira README, código e commits na página.
4. Peça a um colega para localizar a instrução de execução.
5. Registre URL e uma captura sem dados sensíveis.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** Uma pessoa que nunca viu sua aula consegue executar o projeto?

**Atividade 2 — Revisar uma melhoria de documentação.**

1. Crie a branch e melhore o comando de execução.
2. Abra a proposta de integração ou produza um diff local comentado.
3. Peça ao colega para identificar um risco ou dúvida.
4. Responda e integre somente após conferir a versão final.

**Entrega:** tabela, algoritmo, documento ou registro de execução conforme o enunciado, com regra, resultado e justificativa. **Critérios:** cumprir as etapas e permitir conferência por outra pessoa. **Dica:** faça uma previsão antes de consultar a resposta. **Variação mais difícil:** O que um revisor precisa para verificar sua afirmação?

## Exercício individual — 12 minutos

Cada aluno refaz a parte principal das atividades usando uma entrada nova ou uma decisão alternativa. Escreve o resultado esperado, a evidência e a razão. Não precisa reproduzir toda a entrega da dupla, mas deve demonstrar entendimento próprio.

**Enunciado de transferência:** Uma pessoa que nunca viu sua aula consegue executar o projeto? O que um revisor precisa para verificar sua afirmação? Use uma regra do caso para responder e inclua um contraexemplo ou uma limitação.

**Critérios:** correção, completude, evidência e justificativa. Aplicar a [rubrica do E-book](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md). Se o aluno não conseguir começar, forneça a primeira entrada e peça somente a decisão seguinte; depois amplie. Registre a ajuda recebida para distinguir execução assistida de autonomia.

## Perguntas para os alunos e correção — 8 minutos

- Uma pessoa que nunca viu sua aula consegue executar o projeto?
- O que um revisor precisa para verificar sua afirmação?
- Qual evidência permitiria a outra pessoa discordar ou confirmar sua resposta?
- Qual parte da sua primeira previsão você mudou, e por quê?

**Referências de correção:**

- **GitHub e primeiro projeto publicado:** Entrega contém URL acessível ao avaliador, README com contexto fictício, instruções e limites, código e histórico. Repositório privado precisa ter acesso concedido ao avaliador; link sozinho não prova acessibilidade.
- **Branches, revisão e colaboração:** Descrição de referência: “A instrução dependia da pasta atual. Agora indica executar a partir da raiz ou entrar na pasta do simulador. Verificação: o caminho resolve em ambos os casos documentados.”

Não exigir frase idêntica. Verificar se o aluno preserva o comportamento, explica o resultado e reconhece limites.

## Possíveis dúvidas e como responder

| Dúvida | Orientação |
|---|---|
| Preciso publicar em modo público? | Pode usar privado com acesso ao avaliador; o objetivo é revisar uma entrega compartilhável. |
| Revisão é apenas de código? | Não; requisitos, cenários e documentação também merecem revisão. |
| Minha resposta precisa ser igual ao exemplo? | Não. Precisa ser coerente com as regras e permitir conferência. |
| Não consegui usar a ferramenta. Como continuar? | Registre manualmente o raciocínio; complete a evidência de execução ou publicação com apoio depois. |

## Fechamento e resumo da aula

Peça que cada aluno complete: “Hoje usei ___ para decidir ___ e confirmei com ___”. Retome o objetivo e conecte o artefato à entrega final do módulo: repositório de portfólio com README, simulador, três commits com propósito e uma alteração revisada. Na próxima etapa, o aluno usará a entrega como evidência de base para o módulo seguinte.

## Tarefa para casa — orientação de 5 minutos

**Tempo de execução fora da aula:** 30–45 minutos. Revisar a atividade com o feedback recebido, acrescentar um exemplo próprio e registrar o que mudou. Entregar `m03-aula-04-revisao.md`, com contexto fictício, regra, resposta inicial, resposta revisada e evidência. Não incluir dados pessoais de clientes.

**Referência para comparação:** usar as respostas comentadas acima depois de tentar. **Desafio opcional:** Você alterou uma regra, mas o README continua descrevendo a versão anterior. Produza uma revisão que mantenha comportamento, documentação e evidência coerentes.

O professor verifica a revisão no início do próximo encontro. Solicitar também a organização da entrega final e a reflexão individual.
