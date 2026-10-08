# Script do professor — Conceitos Básicos: Front-end, Back-end, APIs e Banco de Dados

**DTEM Treinamentos · encontro ao vivo de até 90 minutos, gravado para revisão.**

Este documento contém falas e ações de condução. Adaptar a linguagem ao próprio estilo, preservando conceitos,
exemplos e critérios. Os intervalos incluem escrita, espera, interação e prática; não são 90 minutos de leitura.
Não depende de vídeos prévios. O aluno pode consultar o E-book e rever a gravação depois.

**Roteiro:** [planejamento da aula](../modulo-01-aula-03-conceitos-basicos-front-back-api-banco.md).  
**Material de estudo:** [E-book correspondente](../../ebooks/modulo-01-fundamentos.md).  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md), empresa e dados fictícios.

## Objetivo e materiais

**Objetivo observável:** distinguir front-end, back-end, API e armazenamento e separar observação de hipótese.  
**Materiais:** desenho de tela, quadro e exemplo de entrada/saída; não exige serviço web.

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

> Ao clicar em confirmar, você vê a tela mudar. Isso revela qual banco foi usado? Hoje vamos separar a interface observada das possíveis partes que trabalham por trás dela.

**Condução:** dar dois minutos para uma previsão individual no chat ou caderno. Colher duas respostas,
sem exigir fala de todos. Esperar aproximadamente 30 segundos antes de completar a resposta.
Não confundir silêncio inicial com falta de capacidade; oferecer a situação concreta novamente.

**Pergunta de diagnóstico:** “API e banco são a mesma coisa?”

**Referência para o professor:** Não: contrato de comunicação e armazenamento cumprem papéis diferentes, ainda que se relacionem.

**Transição para a explicação:**

> Vamos transformar essa primeira resposta em um raciocínio que outra pessoa consiga conferir.
> A cada exemplo, anotem a decisão e a informação que a sustenta.

## 08–25 — Explicação teórica e exemplos

Dividir os 17 minutos entre as três explicações, a escrita e duas perguntas breves.
Usar as falas como apoio, sem acrescentar uma exposição inteira do E-book.

### Explicação 1 — Interface e regra

**Fala sugerida:**

> Front-end é a parte com que o usuário interage. Back-end pode aplicar regras e coordenar operações. Uma tela exibir sucesso não comprova que todas as regras foram respeitadas. Precisamos de resultados e estados verificáveis. Estamos estudando papéis de componentes, não uma arquitetura única para qualquer sistema.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.
### Explicação 2 — API e armazenamento

**Fala sugerida:**

> API é um contrato de interação entre componentes; banco de dados organiza armazenamento. Na proposta de uma aplicação web, a interface enviaria nome e horário a uma API e receberia uma resposta. O laboratório Agenda Clara recebe chamadas locais e guarda estado em memória: ainda não possui API HTTP nem banco persistente.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.
### Explicação 3 — Informação e limite

**Fala sugerida:**

> Um cadastro pode conter identificador, nome e estado de acesso. Senha não deve ser guardada em texto legível; sistemas de autenticação usam mecanismos próprios, como hash de senha. Hoje não implementaremos login. Ao desenhar uma solução futura, marquem explicitamente que se trata de proposta.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.

**Mostrar no quadro:** Usuário → Interface → API proposta → Regra → Armazenamento, destacando as partes não implementadas.

**Checagem de compreensão:** “API e banco são a mesma coisa?”  
**Resposta esperada:** Não: contrato de comunicação e armazenamento cumprem papéis diferentes, ainda que se relacionem.

**Transição:**

> Agora vou percorrer um exemplo pensando em voz alta. Antes de mostrar o resultado,
> vou pedir uma previsão. Observem onde uma regra ou evidência muda a decisão.

## 25–45 — Demonstração guiada

**Preparação:** abrir os dados, documento, código ou cartões indicados. Reservar aproximadamente cinco minutos
por passo e os minutos finais para uma previsão e uma dúvida. Em comandos, executar uma operação de cada vez
e conferir estado. Não substituir falha de ambiente por uma afirmação de execução bem-sucedida.

### Passo 1 — Mostrar tela proposta de reserva

**Fala durante a demonstração:**

> Vou desenhar nome, horário e botão. Isso é interface proposta, não prova de que existe um serviço.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.
### Passo 2 — Percorrer entrada e saída

**Fala durante a demonstração:**

> Ana/H09 entra na operação. A regra confere nome, catálogo e ocupação. Sucesso é uma resposta possível; conflito é outra. O banco, quando existir, guardará o estado que precisamos preservar.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.
### Passo 3 — Separar laboratório e futuro

**Fala durante a demonstração:**

> No simulador, um dicionário com status é saída de uma chamada Python. Não vou chamá-lo de resposta HTTP. Encerrar o programa perde dados em memória.

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

**Nome:** Revisão com explicação — Conceitos Básicos: Front-end, Back-end, APIs e Banco de Dados.  
**Contexto profissional:** uma equipe precisa revisar seu trabalho antes de avançar.
**Objetivo:** aplicar os conceitos e produzir um registro conferível no recorte da aula.

**Fala de orientação:**

> Uma pessoa começa conduzindo e a outra confere as decisões. Na metade, troquem funções.
> Registrem o que fizeram e qual informação justifica o resultado.
> Se discordarem, expliquem a diferença usando regra ou evidência, em vez de escolher pela maioria.

**Enunciado e passo a passo:**

1. Desenhar os componentes de uma reserva web futura.
2. Escrever papel de cada componente e exemplo de entrada/saída.
3. Marcar o que é proposta e o que existe no laboratório.

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

> Explique onde localizar interface, regra e estado em um cadastro hipotético. Escreva uma conclusão que não pode ser obtida somente observando a tela.

**Tempo:** 2 minutos de leitura, 7 de resolução e 3 de revisão/entrega.
Cada aluno entrega uma resposta própria, mesmo quando a atividade anterior foi em grupo.

**Entrega:** artefato pedido no enunciado, acompanhado de uma explicação breve da decisão.
**Critérios:** correção, completude do recorte, evidência e justificativa. Aplicar a
[rubrica formativa](../../planejamento/analise-pedagogica.md), de 0 a 2 por critério. Referência proposta: 6/8, sem zero em correção ou evidência.

**Ajuda graduada:** pedir que identifique primeiro a entrada, regra ou exigência; depois que escolha o próximo
passo. Não resolver todas as etapas. Registrar qual parte foi assistida e conferir transferência em uma tentativa nova.

**Gabarito comentado — revelar depois da tentativa:**

> Interface coleta; regra valida; estado precisa ser mantido. A tela não revela qual banco foi usado nem comprova unicidade. No laboratório, há regras e memória, sem API HTTP. Aceitar desenhos coerentes que distingam implementação de hipótese.

## 77–85 — Correção, intervenções e dúvidas

**Fala para iniciar a correção:**

> Se sua resposta foi diferente, mantenha a primeira versão. Vamos descobrir em qual decisão
> o raciocínio mudou. Corrigir e explicar a mudança faz parte da aprendizagem.

**Se o aluno dizer que api guarda dados:**

> O contrato pode encaminhar uma operação; onde a informação permanece depois da chamada?

**Se o aluno afirmar arquitetura de app real pela aparência:**

> Qual evidência você observou e qual parte está supondo?

**Dúvida central da aula:** “API e banco são a mesma coisa?”

**Como responder:**

> Não: contrato de comunicação e armazenamento cumprem papéis diferentes, ainda que se relacionem.

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

> Hoje trabalhamos como distinguir front-end, back-end, API e armazenamento e separar observação de hipótese.
> Para revisar, procure uma decisão, a evidência que a sustenta e uma limitação que ainda precisa de atenção.
> Guardem a primeira versão e a correção; isso ajuda a explicar a evolução no portfólio.

**Pergunta de saída:** “O que você mudou na sua primeira previsão, e por quê?”

**Tarefa de casa — falar à turma:**

> Revisar diagrama e explicar persistência versus memória. Completar a atividade 3 do caderno e incluir conceitos no mapa.

**Tempo-base:** 30–45 minutos para revisão. Se o enunciado exigir concluir vários artefatos, execução pendente
ou preparação da entrega final, combinar prazo e tempo adicional explicitamente; não prometer que tudo cabe
nesse intervalo.

**Entrega:** `modulo-01-aula-03-conceitos-basicos-front-back-api-banco-revisao.md`, ou arquivos específicos pedidos, contendo resposta inicial, feedback,
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
