# Roteiro — Módulo 5, Aula 3

## Tema e objetivo da aula

**Tema:** Histórias e critérios. **Objetivo observável:** escrever três histórias e critérios positivos e negativos.

**Leitura:** [E-book do módulo](../ebooks/modulo-05-product-owner-e-produto.md), tópicos 3, 4. **Pré-requisito:** atividade da aula anterior, com retomada da lacuna identificada no feedback.

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

modelo de história e casos do módulo 4. Usar [caderno do caso](../atividades/caso-agenda-clara.md), editor de Markdown ou papel e [laboratório](../portfolio/agenda-clara/README.md). Testar o ambiente antes da aula. Contas de ferramentas são opcionais quando houver alternativa documental; evidência de execução continua necessária quando o enunciado a solicitar.

## Abertura da aula

Compare um benefício circular com benefício concreto. Dê dois minutos para registrar uma previsão individual, recolha duas respostas e pergunte qual evidência seria necessária. Retome um conceito anterior e anuncie a entrega de hoje.

## Explicação teórica e exemplos práticos

### User Stories

**Conceito:** Uma história expressa necessidade e benefício sob a perspectiva de quem recebe valor.

**Explicação simples:** Quem quer fazer o quê, e para qual benefício?

**Aprofundamento:** O formato Como/quero/para ajuda a iniciar conversa, mas não garante qualidade. Uma história precisa de exemplos e tamanho adequado. Não force toda tarefa técnica nesse formato. Divida por recortes úteis, respeitando dependências. Evite benefícios circulares, como “quero reservar para reservar”. Consultar, reservar e cancelar têm propósitos distintos. “Adicionar banco” descreve solução técnica; manter reserva após encerrar aplicativo descreve necessidade de persistência, ainda fora do laboratório.

**Exemplo cotidiano:** Um cliente precisa recuperar uma compra; o banco de dados é um meio para atender essa necessidade.

**Cenário empresarial:** PO escreve US02, Dev discute integridade e QA deriva cenários.

**Erros a observar:** História enorme; usuário genérico; benefício circular.

**Orientação:** Perfil, propósito, exemplos e dependências claros.

### Critérios de aceite

**Conceito:** Critérios de aceite descrevem condições verificáveis de uma necessidade específica.

**Explicação simples:** Dizem o que deve acontecer no sucesso e na recusa.

**Aprofundamento:** Dado/Quando/Então separa contexto, ação e resultado; não é sintaxe obrigatória. Critérios de história são específicos; Definition of Done é padrão comum do incremento. Para US02, cubra sucesso, conflito, espaços e horário fora do catálogo. Confira estado, não só mensagem. Critérios ajudam a derivar testes, sem limitar toda exploração. Não inclua desempenho vago nem detalhe de implementação sem necessidade.

**Exemplo cotidiano:** “Compra concluída” fica ambíguo sem definir cobrança e criação do pedido.

**Cenário empresarial:** QA transforma critério de conflito em caso; Dev garante preservação da reserva.

**Erros a observar:** Somente fluxo positivo; “ser intuitivo” sem condição; confundir aceite e DoD.

**Orientação:** Contexto, ação, resultado e estado definidos.

Distribua os 20 minutos entre os tópicos. Peça um exemplo com palavras do aluno antes de avançar; se houver uma contradição, retome a regra do caso.

## Demonstração guiada

Escreva US03 e derive critérios de cancelamento e id inexistente.

**Exemplo 1:** US03: Como recepcionista, quero cancelar uma reserva ativa para oferecer o horário a outra pessoa. RN06/RN07. Depende de identificar reserva. Autorização de cancelamento é questão futura, pois login não existe.

**Exemplo 2:** Dado H09 ocupado por Ana, quando Bruno solicita H09, então retornar conflito e preservar Ana. O teste confere saída e estado usando RN05.

Interrompa antes do resultado para pedir uma previsão. Revele uma etapa de cada vez, marque a regra e compare a resposta com a evidência. Não concluir correção apenas pela aparência do arquivo.

## Dinâmica em grupo

**Nome:** Conversa e confirmação. **Contexto:** a equipe precisa revisar uma decisão antes de avançar o MVP. Em duplas, uma pessoa produz e outra confere; trocar funções na metade do tempo. Em grupos maiores, adicionar um papel de registro.

**Distribuição:** 3 minutos de leitura; 10 de execução; 7 de revisão cruzada; 5 de compartilhamento. Se houver mais de duas duplas, recolher as demais conclusões por escrito para caber no tempo.

**Atividade 3: Criar três histórias do MVP**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Criar três histórias do MVP, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Escreva US01 consultar, US02 reservar e US03 cancelar.
2. Use perfil e benefício concreto.
3. Vincule às RN correspondentes.
4. Registre uma dependência e uma pendência.

**Entrega esperada:** três histórias com vínculos e propósito Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m05-atividade-03.md`.

**Critérios específicos:** Perfil e valor claros; cobertura do MVP; regras identificadas.

**Exemplo de resposta comentada:** US03: Como recepcionista, quero cancelar uma reserva ativa para oferecer o horário a outra pessoa. RN06/RN07. Depende de identificar reserva. Autorização de cancelamento é questão futura, pois login não existe.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Divida uma história grande sem perder o benefício do recorte.

**Atividade 4: Escrever critérios positivos e negativos**

**Contexto profissional:** o time da empresa fictícia Agenda Clara precisa revisar esta decisão antes de entregar o MVP. Dados e regras no [caderno do caso](../atividades/caso-agenda-clara.md).

**Objetivo:** Escrever critérios positivos e negativos, com registro que permita conferência por outra pessoa.

**Passo a passo:**

1. Descreva sucesso e conflito de US02.
2. Inclua espaços e H12 inválido.
3. Descreva cancelamento ativo e inexistente.
4. Converta um critério em caso de teste.

**Entrega esperada:** critérios para três histórias e caso derivado Identificar nome, versão ou premissas, regra utilizada e justificativa. Nome sugerido: `m05-atividade-04.md`.

**Critérios específicos:** Testabilidade; positivos e negativos; estado final explícito.

**Exemplo de resposta comentada:** Dado H09 ocupado por Ana, quando Bruno solicita H09, então retornar conflito e preservar Ana. O teste confere saída e estado usando RN05.

**Dica:** faça sua tentativa antes de ler a resposta e explique qualquer revisão.

**Variação mais difícil:** Qual comportamento indevido passaria se você conferisse só a mensagem?


## Exercício individual

Crie critério para conflito e um caso de teste derivado.

**Tempo:** 20 minutos. **Entrega:** uma versão própria do artefato, incluindo regra, decisão e evidência. **Avaliação:** critérios específicos acima e rubrica do E-book. O professor verifica se houve transferência para o novo caso. Se houver ajuda, registrar qual etapa foi assistida.

## Perguntas para os alunos

- Quem recebe valor?
- Qual estado precisa ser conferido?
- Qual parte da sua previsão você reviu e qual evidência motivou a mudança?

## Possíveis dúvidas e como responder

| Dúvida | Resposta |
|---|---|
| Formato garante qualidade? | Não; exemplos e conversa são necessários. |
| Aceite é DoD? | Aceite é específico; DoD é padrão comum de qualidade. |
| Preciso copiar a resposta de referência? | Não; preserve as regras e explique sua decisão com evidência. |

## Correção e fechamento

As respostas de referência estão na demonstração. Não exigir frases idênticas; conferir critérios e raciocínio. Cada aluno completa: “Usei ___ para decidir ___ e confirmei com ___”. Relacionar à entrega do módulo: brief do problema, roteiro de entrevista, três histórias completas, backlog com seis itens e ata de refinamento. A priorização define a ordem de trabalho.

## Tarefa para casa

Revisar histórias e critérios com QA e Dev simulados.

**Tempo sugerido:** 30–45 minutos. Entregar `m05-aula-03-revisao.md` com resposta inicial, feedback, versão revisada e explicação da mudança. O professor verifica a revisão no próximo encontro. 

