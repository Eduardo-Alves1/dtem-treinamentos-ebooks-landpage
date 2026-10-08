# Script do professor — Variáveis, tipos e decisões

**DTEM Treinamentos · encontro ao vivo de até 90 minutos, gravado para revisão.**

Este documento contém falas e ações de condução. Adaptar a linguagem ao próprio estilo, preservando conceitos,
exemplos e critérios. Os intervalos incluem escrita, espera, interação e prática; não são 90 minutos de leitura.
Não depende de vídeos prévios. O aluno pode consultar o E-book e rever a gravação depois.

**Roteiro:** [planejamento da aula](../modulo-02-aula-02-variaveis-e-condicoes.md).  
**Material de estudo:** [E-book correspondente](../../ebooks/modulo-02-logica-de-programacao.md).  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md), empresa e dados fictícios.

## Objetivo e materiais

**Objetivo observável:** representar informações por tipos e conferir quatro combinações de validação.  
**Materiais:** tabela de dados, quadro e exemplos Python do E-book; papel é suficiente para previsão.

Antes do encontro, preparar o exemplo e conferir os recursos necessários. Em tarefas de ferramenta, preparar
conta e ambiente com antecedência. Se a execução estiver indisponível, percorrer manualmente e declarar o método;
publicação ou execução exigidas pela entrega devem ser concluídas depois com apoio. Não inventar evidência.

## Agenda de condução

| Intervalo | Etapa | Minutos |
|---|---|---:|
| 00–08 | Abertura e diagnóstico | 8 |
| 08–25 | Conceitos e exemplos | 17 |
| 25–45 | Demonstração guiada | 20 |
| 45–50 | Pausa | 5 |
| 50–65 | Dinâmica em dupla ou grupo | 15 |
| 65–77 | Exercício individual | 12 |
| 77–85 | Correção e dúvidas | 8 |
| 85–90 | Fechamento e tarefa | 5 |
| Total | | 90 |

O roteiro original contém o caderno completo de atividades. Nesta versão, os enunciados de grupo e individual
abaixo definem o recorte do encontro. A tarefa de casa conclui os itens restantes. Se precisar reduzir extensão,
preservar demonstração, tentativa individual, feedback e orientação da entrega.

## 00–08 — Abertura e diagnóstico

**Mostrar:** título da aula e objetivo. **Fala de abertura:**

> O valor 2 e o texto '2' representam a mesma coisa para uma operação? Vamos descobrir como dados e decisões mudam o comportamento de uma reserva.

**Condução:** dar dois minutos para uma previsão individual no chat ou caderno. Colher duas respostas,
sem exigir fala de todos. Esperar aproximadamente 30 segundos antes de completar a resposta.
Não confundir silêncio inicial com falta de capacidade; oferecer a situação concreta novamente.

**Pergunta de diagnóstico:** “Nome vazio e H12 inválido: qual recusa aparece na ordem escolhida?”

**Referência para o professor:** Nome inválido, porque essa verificação vem primeiro; a decisão não ocupa nenhum horário.

**Transição para a explicação:**

> Vamos transformar essa primeira resposta em um raciocínio que outra pessoa consiga conferir.
> A cada exemplo, anotem a decisão e a informação que a sustenta.

## 08–25 — Explicação teórica e exemplos

Dividir os 17 minutos entre as três explicações, a escrita e duas perguntas breves.
Usar as falas como apoio, sem acrescentar uma exposição inteira do E-book.

### Explicação 1 — Variáveis e tipos

**Fala sugerida:**

> Uma variável associa um nome a um valor. nome guarda texto; quantidade guarda número; horário H09 é identificador textual. O tipo depende do significado e da operação. Dois números podem ser somados; dois textos podem ser concatenados. Por isso, 2 mais 3 e os textos '2' mais '3' não dão a mesma saída.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.
### Explicação 2 — Atribuir e comparar

**Fala sugerida:**

> Em Python, um sinal de igual atribui e dois comparam igualdade. Hoje vocês podem acompanhar em tabela sem dominar sintaxe. Texto, inteiro, booleano e lista atendem usos diferentes. Uma lista de horários mantém itens separados; um texto contendo vírgulas continua sendo um texto.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.
### Explicação 3 — Condições e ordem

**Fala sugerida:**

> Uma decisão seleciona um caminho. Nosso exemplo verifica nome antes do catálogo e da ocupação. Nome formado por espaços fica vazio após remover as extremidades. Se nome e horário são inválidos ao mesmo tempo, a ordem define o primeiro motivo informado. Usar and exige ambas as condições; or exige ao menos uma.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.

**Mostrar no quadro:** dicionário de dados e tabela Nome válido? / Horário no catálogo? / Decisão.

**Checagem de compreensão:** “Nome vazio e H12 inválido: qual recusa aparece na ordem escolhida?”  
**Resposta esperada:** Nome inválido, porque essa verificação vem primeiro; a decisão não ocupa nenhum horário.

**Transição:**

> Agora vou percorrer um exemplo pensando em voz alta. Antes de mostrar o resultado,
> vou pedir uma previsão. Observem onde uma regra ou evidência muda a decisão.

## 25–45 — Demonstração guiada

**Preparação:** abrir os dados, documento, código ou cartões indicados. Reservar aproximadamente cinco minutos
por passo e os minutos finais para uma previsão e uma dúvida. Em comandos, executar uma operação de cada vez
e conferir estado. Não substituir falha de ambiente por uma afirmação de execução bem-sucedida.

### Passo 1 — Comparar entradas

**Fala durante a demonstração:**

> Vou escrever 2 + 3 e '2' + '3'. Prevejam as saídas: 5 na soma; '23' na concatenação. A operação precisa considerar os tipos.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.
### Passo 2 — Completar quatro combinações

**Fala durante a demonstração:**

> Nome válido/H09 segue para ocupação. Nome válido/H12 é horário inválido. Nome vazio/H09 é nome inválido. Nome vazio/H12 também é nome inválido quando validamos nome primeiro.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.
### Passo 3 — Relacionar regra e estado

**Fala durante a demonstração:**

> Não confundir 'pode continuar' com reserva concluída. A disponibilidade ainda será verificada; entradas recusadas não devem ocupar horário.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.

**Pergunta após a demonstração:** “Qual decisão vocês conseguem explicar sem copiar a frase que usei?”

**Referência:** a resposta precisa relacionar situação, decisão e fundamento.
As falas de cada passo indicam o comportamento ou a interpretação que deve ser conferido.

**Transição:**

> Na prática, vocês vão alternar quem conduz e quem revisa. O objetivo é produzir algo
> que o colega consiga conferir, e não somente repetir minha demonstração.

## 45–50 — Pausa

Deixar horário de retorno visível e não apresentar conteúdo obrigatório durante os cinco minutos.
Na gravação, indicar o ponto em que a atividade seguinte começa.

## 50–65 — Dinâmica em dupla ou grupo

**Nome:** Revisão com explicação — Variáveis, tipos e decisões.  
**Contexto profissional:** uma equipe precisa revisar seu trabalho antes de avançar.
**Objetivo:** aplicar os conceitos e produzir um registro conferível no recorte da aula.

**Fala de orientação:**

> Uma pessoa começa conduzindo e a outra confere as decisões. Na metade, troquem funções.
> Registrem o que fizeram e qual informação justifica o resultado.
> Se discordarem, expliquem a diferença usando regra ou evidência, em vez de escolher pela maioria.

**Enunciado e passo a passo:**

1. Criar quatro linhas de dicionário: nome, horário, quantidade, disponíveis.
2. Preencher quatro combinações de validação e trocar papéis.
3. Indicar o que não muda na agenda quando a entrada é recusada.

**Tempo:** 2 minutos para ler e organizar; 5 para produzir; 5 para trocar revisão; 3 para compartilhar.
Selecionar duas duplas para falar e recolher as demais por escrito. Em aulas de entrevista ou apresentação,
usar o mesmo tempo para a primeira participação, troca e feedback.

**Entrega esperada:** registro da atividade com contexto, decisão, fundamento e uma revisão.
**Critérios:** cumprir as etapas, preservar as regras e permitir que o colega confira.
**Referência de correção:** usar os exemplos da demonstração e verificar o que mudou no novo caso,
sem exigir palavras idênticas.

**Perguntas ao circular:** “Qual passo está sendo executado?”, “Qual evidência sustenta isso?”
e “O que precisaria mudar para sua conclusão ser diferente?”

**Dica para a dupla:** separar o que observou do que está supondo.
**Variação difícil:** formular um contraexemplo ou limite; transferir para casa se não couber.

## 65–77 — Exercício individual

**Fala do professor — enunciado:**

> Escreva o tipo e uso de um identificador de reserva e de uma contagem. Depois explique espaços/H11 e Ana/H12, com esperado e estado.

**Tempo:** 2 minutos de leitura, 7 de resolução e 3 de revisão/entrega.
Cada aluno entrega uma resposta própria, mesmo quando a atividade anterior foi em grupo.

**Entrega:** artefato pedido no enunciado, acompanhado de uma explicação breve da decisão.
**Critérios:** correção, completude do recorte, evidência e justificativa. Aplicar a
[rubrica formativa](../../planejamento/analise-pedagogica.md), de 0 a 2 por critério. Referência proposta: 6/8, sem zero em correção ou evidência.

**Ajuda graduada:** pedir que identifique primeiro a entrada, regra ou exigência; depois que escolha o próximo
passo. Não resolver todas as etapas. Registrar qual parte foi assistida e conferir transferência em uma tentativa nova.

**Gabarito comentado — revelar depois da tentativa:**

> Id no simulador é inteiro usado para identificar, não contar clientes; contagem é inteiro para quantidade. Espaços/H11 retorna nome_invalido; Ana/H12 retorna horario_invalido; agenda preservada. H09 continua texto do catálogo.

## 77–85 — Correção, intervenções e dúvidas

**Fala para iniciar a correção:**

> Se sua resposta foi diferente, mantenha a primeira versão. Vamos descobrir em qual decisão
> o raciocínio mudou. Corrigir e explicar a mudança faz parte da aprendizagem.

**Se o aluno somar textos como números:**

> Mostre os valores com aspas e explique qual operação acontece.

**Se o aluno reservar antes de validar:**

> Em que passo uma entrada recusada deve encerrar a tentativa?

**Dúvida central da aula:** “Nome vazio e H12 inválido: qual recusa aparece na ordem escolhida?”

**Como responder:**

> Nome inválido, porque essa verificação vem primeiro; a decisão não ocupa nenhum horário.

**Se perguntarem se a resposta precisa ser igual:**

> Não precisa repetir minha frase. Precisa respeitar as regras e permitir que outra pessoa
> confira como você chegou à decisão.

**Se perguntarem como usar a gravação:**

> Localize o trecho em que surgiu a dúvida, reveja o exemplo e depois tente uma entrada ou situação nova.
> Assistir de novo ajuda; explicar sua própria decisão é o que vamos avaliar.

**Modelo de devolutiva:**

> Você acertou ao identificar a decisão principal. Falta mostrar a informação que a sustenta.
> Acrescente essa evidência e explique o que mudou na sua revisão.

Selecionar duas dúvidas para os oito minutos. Registrar as demais para resposta após a aula ou retomada.
Não ampliar silenciosamente a duração do encontro.

## 85–90 — Fechamento e tarefa para casa

**Fala de fechamento:**

> Hoje trabalhamos como representar informações por tipos e conferir quatro combinações de validação.
> Para revisar, procure uma decisão, a evidência que a sustenta e uma limitação que ainda precisa de atenção.
> Guardem a primeira versão e a correção; isso ajuda a explicar a evolução no portfólio.

**Pergunta de saída:** “O que você mudou na sua primeira previsão, e por quê?”

**Tarefa de casa — falar à turma:**

> Concluir dicionário e tabela de decisão. Executar os exemplos se houver Python ou registrar rastreamento manual identificado, e explicar uma previsão revista.

**Tempo-base:** 30–45 minutos para revisão. Se o enunciado exigir concluir vários artefatos, execução pendente
ou preparação da entrega final, combinar prazo e tempo adicional explicitamente; não prometer que tudo cabe
nesse intervalo.

**Entrega:** `modulo-02-aula-02-variaveis-e-condicoes-revisao.md`, ou arquivos específicos pedidos, contendo resposta inicial, feedback,
versão revisada e explicação. O professor verifica a revisão no início do encontro seguinte.

**Dica:** usar E-book e gravação como apoio; identificar empresa fictícia e origem da evidência.
**Variação difícil:** acrescentar uma situação nova ou uma dúvida de aplicação, com proposta de investigação.

## Checklist do professor e uso da gravação

- [ ] Preparar recursos e exemplo antes do encontro.
- [ ] Pedir previsão antes de revelar referência.
- [ ] Conferir compreensão por exemplo, não por memorização.
- [ ] Alternar condução e revisão na dupla.
- [ ] Preservar exercício individual.
- [ ] Declarar execução, simulação e limites corretamente.
- [ ] Registrar feedback, tarefa e dúvidas pendentes.
- [ ] Disponibilizar gravação para revisão e indicar os blocos de demonstração e correção.

Percentual de vídeo assistido é sinal de utilização, não prova de domínio.
Usar artefato e explicação para avaliar aprendizagem; não penalizar o aluno por uma falha de registro de reprodução.
