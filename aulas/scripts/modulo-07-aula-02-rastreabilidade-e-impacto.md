# Script do professor — Rastreabilidade e impacto

**DTEM Treinamentos · encontro ao vivo de até 90 minutos, gravado para revisão.**

Este documento contém falas e ações de condução. Adaptar a linguagem ao próprio estilo, preservando conceitos,
exemplos e critérios. Os intervalos incluem escrita, espera, interação e prática; não são 90 minutos de leitura.
Não depende de vídeos prévios. O aluno pode consultar o E-book e rever a gravação depois.

**Roteiro:** [planejamento da aula](../modulo-07-aula-02-rastreabilidade-e-impacto.md).  
**Material de estudo:** [E-book correspondente](../../ebooks/modulo-07-ciclo-de-vida-do-software.md).  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md), empresa e dados fictícios.

## Objetivo e materiais

**Objetivo observável:** rastrear uma mudança entre regra, história, teste e defeito.  
**Materiais:** RN03, RN02, RN06; US02, TC03 e BUG01; hipótese de novo H12.

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

> Quando uma regra muda, como saber o que revisar? Hoje construiremos vínculos que permitem responder sem depender da memória de uma pessoa.

**Condução:** dar dois minutos para uma previsão individual no chat ou caderno. Colher duas respostas,
sem exigir fala de todos. Esperar aproximadamente 30 segundos antes de completar a resposta.
Não confundir silêncio inicial com falta de capacidade; oferecer a situação concreta novamente.

**Pergunta de diagnóstico:** “Pode existir um teste correto para uma versão e desatualizado para outra?”

**Referência para o professor:** Sim. Registre a versão da regra e atualize dados e expectativas quando houver mudança.

**Transição para a explicação:**

> Vamos transformar essa primeira resposta em um raciocínio que outra pessoa consiga conferir.
> A cada exemplo, anotem a decisão e a informação que a sustenta.

## 08–25 — Explicação teórica e exemplos

Dividir os 17 minutos entre as três explicações, a escrita e duas perguntas breves.
Usar as falas como apoio, sem acrescentar uma exposição inteira do E-book.

### Explicação 1 — Rastreabilidade

**Fala sugerida:**

> Rastrear é relacionar uma necessidade às decisões, à construção e à verificação correspondentes. Não basta criar códigos: é preciso explicar o vínculo e manter a versão dos artefatos.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.
### Explicação 2 — Impacto

**Fala sugerida:**

> Adicionar H12 ao catálogo afeta a regra de horários, a consulta, dados de teste e casos que antes tratavam H12 como inválido. Um teste antigo pode reprovar corretamente a versão antiga e ficar desatualizado na nova.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.
### Explicação 3 — Defeito e reteste

**Fala sugerida:**

> Um defeito deve apontar comportamento esperado e observado, ambiente e evidência. Depois da correção, reteste verifica o problema original; regressão avalia comportamentos relacionados que poderiam ter sido afetados.

**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.

**Mostrar no quadro:** Regra → História → Caso de teste → Resultado → Defeito → Reteste; coluna versão.

**Checagem de compreensão:** “Pode existir um teste correto para uma versão e desatualizado para outra?”  
**Resposta esperada:** Sim. Registre a versão da regra e atualize dados e expectativas quando houver mudança.

**Transição:**

> Agora vou percorrer um exemplo pensando em voz alta. Antes de mostrar o resultado,
> vou pedir uma previsão. Observem onde uma regra ou evidência muda a decisão.

## 25–45 — Demonstração guiada

**Preparação:** abrir os dados, documento, código ou cartões indicados. Reservar aproximadamente cinco minutos
por passo e os minutos finais para uma previsão e uma dúvida. Em comandos, executar uma operação de cada vez
e conferir estado. Não substituir falha de ambiente por uma afirmação de execução bem-sucedida.

### Passo 1 — Vincular conflito

**Fala durante a demonstração:**

> RN02 diz que não pode haver duas reservas ativas no mesmo horário. US02 contém esse comportamento. Vou localizar o caso de conflito no kit, sem confundi-lo com TC03, que verifica nome com espaços. Cada vínculo precisa corresponder à regra realmente avaliada.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.
### Passo 2 — Vincular nome

**Fala durante a demonstração:**

> BUG01 da variante com defeito aceita espaços. A relação central é RN03, a validação de nome; vou manter o vínculo com o caso que testa esse cenário.

**Ação:** mostrar o registro correspondente antes de avançar; pedir uma previsão e conferir a resposta com a evidência.
### Passo 3 — Revisar mudança

**Fala durante a demonstração:**

> Com H12 válido, o teste de horário inválido precisa usar outro valor fora do catálogo, e o cenário de consulta deve incluir o novo horário.

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

**Nome:** Revisão com explicação — Rastreabilidade e impacto.  
**Contexto profissional:** uma equipe precisa revisar seu trabalho antes de avançar.
**Objetivo:** aplicar os conceitos e produzir um registro conferível no recorte da aula.

**Fala de orientação:**

> Uma pessoa começa conduzindo e a outra confere as decisões. Na metade, troquem funções.
> Registrem o que fizeram e qual informação justifica o resultado.
> Se discordarem, expliquem a diferença usando regra ou evidência, em vez de escolher pela maioria.

**Enunciado e passo a passo:**

1. Construir uma linha de rastreabilidade para nome inválido.
2. Mapear três impactos de adicionar H12.
3. Escolher um reteste e uma regressão para a mudança.

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

> Associe o defeito de cancelamento que não devolve H10 à regra aplicável e ao comportamento esperado.

**Tempo:** 2 minutos de leitura, 7 de resolução e 3 de revisão/entrega.
Cada aluno entrega uma resposta própria, mesmo quando a atividade anterior foi em grupo.

**Entrega:** artefato pedido no enunciado, acompanhado de uma explicação breve da decisão.
**Critérios:** correção, completude do recorte, evidência e justificativa. Aplicar a
[rubrica formativa](../../planejamento/analise-pedagogica.md), de 0 a 2 por critério. Referência proposta: 6/8, sem zero em correção ou evidência.

**Ajuda graduada:** pedir que identifique primeiro a entrada, regra ou exigência; depois que escolha o próximo
passo. Não resolver todas as etapas. Registrar qual parte foi assistida e conferir transferência em uma tentativa nova.

**Gabarito comentado — revelar depois da tentativa:**

> RN06: cancelar reserva ativa deve liberar o horário. O teste deve reservar H10, cancelar o identificador e consultar H10 disponível. BUG02 é um registro fictício fornecido; não afirmar execução dele no código de referência.

## 77–85 — Correção, intervenções e dúvidas

**Fala para iniciar a correção:**

> Se sua resposta foi diferente, mantenha a primeira versão. Vamos descobrir em qual decisão
> o raciocínio mudou. Corrigir e explicar a mudança faz parte da aprendizagem.

**Se o aluno ids substituem explicação:**

> Conte em uma frase qual comportamento conecta esses dois artefatos.

**Se o aluno tudo exige retestar tudo sempre:**

> Priorize pelo impacto e risco; justifique os cenários escolhidos.

**Dúvida central da aula:** “Pode existir um teste correto para uma versão e desatualizado para outra?”

**Como responder:**

> Sim. Registre a versão da regra e atualize dados e expectativas quando houver mudança.

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

> Hoje trabalhamos como rastrear uma mudança entre regra, história, teste e defeito.
> Para revisar, procure uma decisão, a evidência que a sustenta e uma limitação que ainda precisa de atenção.
> Guardem a primeira versão e a correção; isso ajuda a explicar a evolução no portfólio.

**Pergunta de saída:** “O que você mudou na sua primeira previsão, e por quê?”

**Tarefa de casa — falar à turma:**

> Concluir a matriz de rastreabilidade da aula, incluindo versões, evidências e análise da alteração de catálogo.

**Tempo-base:** 30–45 minutos para revisão. Se o enunciado exigir concluir vários artefatos, execução pendente
ou preparação da entrega final, combinar prazo e tempo adicional explicitamente; não prometer que tudo cabe
nesse intervalo.

**Entrega:** `modulo-07-aula-02-rastreabilidade-e-impacto-revisao.md`, ou arquivos específicos pedidos, contendo resposta inicial, feedback,
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
