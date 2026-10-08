# Script do professor — Módulo 2, Aula 1
## Algoritmos e rastreamento

**DTEM Treinamentos · duração máxima: 90 minutos · encontro ao vivo, gravado para revisão.**

Este é um texto de apoio às falas e à condução. O professor pode adaptá-lo ao próprio jeito de falar, mantendo conceitos, regras e momentos de prática. Os intervalos incluem fala, escrita no quadro, espera e interação; não representam 90 minutos de leitura contínua.

**Roteiro pedagógico:** [aula 1](../modulo-02-aula-01-algoritmos-e-rastreamento.md).  
**Leitura do aluno:** [E-book do Módulo 2](../../ebooks/modulo-02-logica-de-programacao.md), tópico 1.  
**Regras fornecidas:** [Agenda Clara](../../atividades/caso-agenda-clara.md).

## Objetivo e preparação

Ao final, cada aluno escreve passos de reserva, distingue entrada, processamento, saída e estado e rastreia uma tentativa válida e uma recusada. Não é necessário programar, instalar ferramentas ou dominar sintaxe.

Antes do encontro, preparar um quadro ou documento compartilhado com:

- Catálogo: H09, H10 e H11.
- Regra: um horário aceita no máximo uma reserva ativa.
- Nome obrigatório com conteúdo após remover espaços das extremidades.
- Reserva recusada não apaga nem altera uma reserva existente.
- Três espaços desenhados entre aspas: “   ”, para tornar a entrada visível.
- Tabela com tentativa, entrada, estado antes, resultado e estado depois.

H09 é um identificador do catálogo, não uma data real. Reserva e cancelamento não precisam ser demonstrados por código nesta aula; cancelamento será aprofundado depois. Usar nomes fictícios.

**Materiais:** quadro ou editor compartilhado, caderno do caso e folha ou editor de texto por aluno. Salas de dupla são opcionais; se não houver, usar troca de arquivos ou comentários no chat.

## Agenda de condução

| Intervalo | Bloco | Minutos |
|---|---|---:|
| 00–08 | Abertura e diagnóstico | 8 |
| 08–25 | Conceitos e exemplo cotidiano | 17 |
| 25–45 | Algoritmo e rastreamento demonstrados | 20 |
| 45–50 | Pausa | 5 |
| 50–65 | Prática em dupla | 15 |
| 65–77 | Exercício individual | 12 |
| 77–85 | Correção e perguntas | 8 |
| 85–90 | Fechamento e tarefa | 5 |
| Total | | 90 |

Se uma discussão ultrapassar o tempo, registrar a dúvida para retorno e transferir a variação opcional para casa. Preservar exercício individual e fechamento.

## 00–08 — Abertura e diagnóstico

**Mostrar:** “Hoje: transformar uma regra em passos e conferir o resultado.”

**Fala sugerida:**

> Na aula de hoje, vamos aprender a organizar uma solução antes de escrever código. Ao final, vocês vão conseguir explicar quais informações entram, quais verificações acontecem e qual resultado deve sair.
>
> Pensem em uma recepção que agenda atendimentos por mensagem. Ana pede um horário, a recepção confirma e, logo depois, Bruno pede o mesmo horário. O que precisa ser conferido antes de confirmar para Bruno?

**Perguntar:** “Qual seria o primeiro passo de vocês?”

**Esperar:** aproximadamente 30 segundos; depois colher duas respostas. Pedir uma previsão individual no chat ou caderno. Não anunciar a resposta completa ainda.

**Se alguém responder “olhar a agenda”:**

> Esse é um bom começo. Agora vamos tornar o passo mais preciso: olhar qual horário? O que fazemos se ele estiver ocupado? E o que respondemos para a pessoa?

**Se responder “avisar que não pode”:**

> Pode ser o resultado correto, mas ainda precisamos mostrar como chegamos a ele. Hoje vamos trabalhar justamente essa ligação entre informação, verificação e resposta.

**Transição:**

> A regra diz o que precisa ser respeitado. O algoritmo organiza os passos para respeitar essa regra. Vamos entender essa diferença com uma situação simples.

## 08–25 — Explicação teórica com falas

### 08–13 — O que é um algoritmo

**Escrever:** “Algoritmo = passos organizados para resolver um problema.”

**Fala:**

> Um algoritmo é uma sequência de passos que descreve uma solução. Podemos escrevê-lo em português, desenhar um fluxo ou, mais adiante, transformá-lo em código.
>
> Imaginem que eu dê a instrução “reserve o horário para o cliente”. Para quem já trabalha na recepção, isso pode parecer suficiente. Para uma pessoa que acabou de começar, faltam informações: o nome foi informado? O horário existe? Está disponível? Qual resposta damos se uma dessas condições não for atendida?
>
> Um algoritmo útil transforma essa instrução ampla em decisões e ações claras.

**Perguntar:** “Uma lista de passos pode estar errada mesmo quando parece organizada?”

**Resposta esperada:** sim, pode omitir uma verificação ou executar passos na ordem errada.

**Intervenção:**

> Exatamente. Organização ajuda, mas precisamos conferir se os passos atendem às regras. Uma lista que confirma a reserva e só depois verifica se o horário está ocupado pode causar problema.

### 13–19 — Entrada, processamento e saída

**Mostrar:**

| Parte | Pergunta | Exemplo |
|---|---|---|
| Entrada | O que recebemos? | Nome e horário |
| Processamento | O que verificamos e fazemos? | Validar e conferir ocupação |
| Saída | Qual resultado devolvemos? | Sucesso ou motivo de recusa |

**Fala:**

> A entrada é a informação que recebemos para iniciar a operação. Aqui, nome e horário.
>
> O processamento reúne as verificações e ações. Primeiro avaliamos os dados e a disponibilidade; só depois criamos a reserva.
>
> A saída informa o resultado da tentativa. Pode ser sucesso, nome inválido, horário inválido ou conflito de horário.
>
> Essas partes ajudam a explicar um sistema mesmo antes de conhecer uma linguagem de programação.

**Exemplo cotidiano:**

> Ao tentar comprar um ingresso, escolher o assento é uma entrada. Conferir se ele ainda está disponível faz parte do processamento. A confirmação ou a recusa é uma saída. Apenas clicar no assento não garante que a compra foi concluída.

**Perguntar:** “Na reserva, o nome do cliente é entrada ou saída?”

**Se houver confusão:**

> Perguntem de onde veio a informação. O cliente informou o nome, então ele é uma entrada. A confirmação foi produzida depois da análise, então é uma saída.

### 19–25 — Estado e rastreamento

**Escrever:** “Estado = como a agenda está em determinado momento.”

**Fala:**

> Além da resposta, precisamos acompanhar o estado. Antes de reservar, H09 está livre. Depois de uma reserva válida, ele está ocupado.
>
> Quando uma tentativa é recusada, a resposta muda para conflito, mas a reserva anterior deve continuar existindo.
>
> Rastrear um algoritmo significa percorrer os passos com uma entrada concreta e anotar o que acontece. Assim, conseguimos conferir a resposta e as mudanças na agenda.

**Perguntar:** “Se o sistema disser conflito, mas apagar a reserva da Ana, a operação está correta?”

**Resposta esperada:** não, porque a recusa precisa preservar o estado anterior.

**Conexão com o trabalho:**

> Produto precisa esclarecer a regra. Desenvolvimento precisa implementá-la. QA pode testar a resposta e verificar se a reserva anterior foi preservada. O mesmo raciocínio ajuda essas especialidades a conversar.

**Transição:**

> Agora vamos acompanhar duas tentativas. Na primeira, o horário está livre. Na segunda, vamos usar a agenda que ficou depois da primeira tentativa.

## 25–45 — Demonstração guiada

### 25–31 — Construir os passos no quadro

**Mostrar e ler as regras necessárias:** RN01–RN05 e RN08. Explicar que RN08 define a recusa de horário fora do catálogo.

**Fala:**

> Nosso catálogo tem H09, H10 e H11. O nome deve ter conteúdo depois de remover espaços das extremidades. Um horário aceita somente uma reserva ativa.
>
> Vou escrever o algoritmo pensando em voz alta. Não vou ocupar o horário antes de terminar as verificações.

**Escrever uma linha por vez:**

```text
1. Receber nome e horário.
2. Verificar se o nome tem conteúdo após remover espaços das extremidades.
   Se não tiver, responder nome inválido e encerrar a tentativa.
3. Verificar se o horário pertence ao catálogo.
   Se não pertencer, responder horário inválido e encerrar.
4. Verificar se o horário já está ocupado.
   Se estiver, responder conflito e preservar a reserva existente.
5. Registrar a nova reserva no horário.
6. Responder sucesso e encerrar.
```

**Fala:**

> “Encerrar” significa que essa tentativa terminou. Depois de recusar um nome inválido, não continuamos até a etapa que cria a reserva.
>
> Antes de registrar qualquer mudança, passamos pelas verificações. Essa ordem será importante quando transformarmos os passos em código.

**Perguntar:** “Qual passo altera a agenda?”

**Resposta:** passo 5. As recusas terminam sem criar reserva.

### 31–37 — Primeira tentativa: Ana/H09

**Estado inicial:** todos os horários livres.

**Fala:**

> Ana informa seu nome e pede H09. Primeiro: o nome tem conteúdo? Sim. Segundo: H09 está no catálogo? Sim. Terceiro: ele está ocupado? Ainda não.
>
> Portanto, podemos registrar a reserva. A resposta é sucesso e o estado de H09 passa a ser ocupado por Ana.

**Preencher:**

| Tentativa | Entrada | Estado antes | Resultado | Estado depois |
|---|---|---|---|---|
| 1 | Ana/H09 | H09 livre | Sucesso | H09 ocupado por Ana |

**Pedir:** um aluno explica o passo que justifica sucesso; outro explica a mudança de estado.

**Se disser apenas “porque funcionou”:**

> Vamos apontar a razão: qual verificação permitiu registrar? Precisamos explicar por que o resultado era esperado, não apenas repetir a resposta.

### 37–42 — Segunda tentativa: Bruno/H09

**Fala antes de revelar:**

> Agora Bruno pede H09. A agenda não foi reiniciada: a reserva de Ana continua existindo. Qual resposta vocês preveem? E como H09 deve ficar depois?

**Esperar:** um minuto para resposta individual.

**Percorrer os passos:**

> Bruno tem um nome válido e H09 pertence ao catálogo. Mas, quando verificamos a ocupação, encontramos a reserva de Ana. A tentativa de Bruno termina com conflito.
>
> Não criamos outra reserva e não removemos a anterior. H09 continua ocupado por Ana.

| Tentativa | Entrada | Estado antes | Resultado | Estado depois |
|---|---|---|---|---|
| 2 | Bruno/H09 | H09 ocupado por Ana | Conflito | H09 ocupado por Ana |

**Perguntar:** “A resposta de erro significa que algo foi feito errado pelo sistema?”

**Explicar:**

> Nem sempre. Aqui, recusar é o comportamento correto. Uma regra pode exigir que o sistema impeça uma ação. O teste precisa conferir essa recusa e a preservação da agenda.

### 42–45 — Antecipar uma entrada inválida

**Mostrar:** nome “   ”, horário H11 livre.

**Fala:**

> Temos um nome formado apenas por espaços. Depois de remover esses espaços, sobra conteúdo? Não. Então a tentativa termina no passo 2. H11 permanece livre.
>
> Na prática de vocês, anotem também o estado final. Essa informação mostra se a tentativa recusada alterou algo que deveria permanecer igual.

**Transição para pausa:**

> Vamos fazer cinco minutos de pausa. Na volta, vocês vão usar os mesmos passos com outras entradas, alternando quem conduz e quem confere.

## 45–50 — Pausa

**Ação do professor:** deixar o horário de retorno visível. Não acrescentar conteúdo obrigatório durante a pausa. Na gravação, o aluno pode avançar até o próximo bloco.

## 50–65 — Dinâmica em dupla

**Nome:** Uma pessoa conduz, outra confere.  
**Contexto:** revisar uma regra antes de apresentar a solução ao time.  
**Objetivo:** escrever algoritmo e rastrear entradas, incluindo recusa.  
**Entrega:** passos e tabela de três tentativas.  
**Critérios:** ordem correta, resultado justificado e preservação do estado nas recusas.

**Fala de orientação:**

> Cada dupla começa com uma agenda nova, com H09, H10 e H11 livres. Uma pessoa percorre os passos e a outra pergunta qual regra sustenta cada decisão.
>
> Primeiro, Lia pede H10. Depois, Rui pede H10 na mesma agenda. Por fim, uma pessoa com nome composto por espaços pede H11.
>
> Vocês vão entregar o algoritmo e a tabela de antes e depois. Não precisam escrever código nem fazer um desenho bonito. Precisam permitir que outra pessoa acompanhe o raciocínio.

**Distribuição dos 15 minutos:**

1. **2 minutos:** ler regras, escolher quem conduz e preparar a tabela.
2. **5 minutos:** percorrer Lia/H10 e Rui/H10.
3. **5 minutos:** trocar funções, conferir espaços/H11 e revisar passos.
4. **3 minutos:** colher uma conclusão de duas duplas; as demais entregam por escrito.

**Perguntas do professor ao acompanhar:**

- Em qual passo vocês estão?
- De onde veio o resultado esperado?
- A agenda foi reiniciada ou é a mesma?
- O que mudou depois dessa tentativa?
- O que precisa continuar igual?

**Se o grupo aceitar Rui/H10:**

> Antes dessa tentativa, quem já estava em H10? A regra permite duas reservas ativas? Voltem ao passo de ocupação e revisem o resultado.

**Se ocupar H11 para o nome inválido:**

> Em que etapa essa tentativa deveria terminar? Ela pode chegar ao registro da reserva depois de ser recusada?

**Referência para correção:**

| Entrada | Resultado | Estado final relevante |
|---|---|---|
| Lia/H10 | Sucesso | H10 ocupado por Lia |
| Rui/H10 | Conflito | H10 continua com Lia |
| Espaços/H11 | Nome inválido | H11 continua livre |

**Dica para o aluno:** prever antes de percorrer; conferir resposta e estado.  
**Variação difícil, somente se sobrar tempo:** incluir H12 e explicar por que o catálogo impede a reserva.

## 65–77 — Exercício individual

**Mostrar o enunciado; não mostrar a referência ainda.**

**Fala:**

> Agora quero conferir como cada pessoa aplica a lógica. Considerem outra agenda: H10 está ocupado por Carla; H09 e H11 estão livres.
>
> Percorram três tentativas nessa ordem: Rui pede H10; um nome composto por espaços pede H09; Dani pede H11. Anotem a etapa que decide a resposta e o estado final.
>
> Depois escolham uma das tentativas e expliquem, em duas frases, por que o resultado respeita a regra.

**Passo a passo para o aluno:**

1. Registrar estado inicial.
2. Aplicar os passos às três entradas, mantendo o estado entre elas.
3. Preencher resultado e estado depois.
4. Explicar uma decisão e uma recusa.
5. Entregar a tabela com seu nome ou identificador de aluno.

**Tempo:** 2 minutos de leitura, 7 de resolução e 3 de revisão/entrega.

**Ajuda graduada para quem não inicia:**

> Comece pela primeira entrada. O nome tem conteúdo? O horário existe? Quem já está nele?

Depois da primeira tentativa assistida, pedir que faça a segunda sozinho. Registrar a ajuda para orientar recuperação.

**Gabarito — referência reservada ao professor:**

| Entrada | Passo decisivo | Resultado | Estado relevante |
|---|---|---|---|
| Rui/H10 | 4: ocupação | Conflito | Carla permanece em H10 |
| Espaços/H09 | 2: nome | Nome inválido | H09 permanece livre |
| Dani/H11 | 5: registro após validações | Sucesso | Dani ocupa H11 |

**Rubrica:** correção, completude, evidência e justificativa, de 0 a 2. Referência completa no E-book. Para esta aula, evidência é a tabela de rastreamento; não é necessário executar Python.

## 77–85 — Correção dialogada e dúvidas

**Fala:**

> Vamos comparar os resultados. Se sua resposta foi diferente, não apague imediatamente. Primeiro identifique em qual passo seu raciocínio mudou. Depois registre a correção e a razão.
>
> Na primeira tentativa, Carla continua em H10. Na segunda, H09 permanece livre. Na terceira, H11 passa a ser ocupado por Dani. As duas primeiras são recusadas corretamente; a última altera a agenda porque passou pelas verificações.

**Selecionar duas perguntas para caber no tempo:**

- Qual a diferença entre saída e estado?
- Em que passo a tentativa com nome inválido termina?
- Por que a recusa de Rui não pode apagar Carla?
- Como você explicaria o algoritmo para alguém que não assistiu à aula?

### Respostas prontas para dúvidas recorrentes

| Pergunta do aluno | Fala sugerida do professor |
|---|---|
| Algoritmo é código? | “Algoritmo descreve a solução. Código é uma forma de implementar essa solução em uma linguagem. Hoje estamos trabalhando os passos.” |
| Tenho que decorar os passos? | “Você precisa compreender as regras e conseguir reconstruir uma sequência coerente. Usar o caderno como apoio faz parte da prática.” |
| Posso começar pelo fluxograma? | “Pode. Confira se cada decisão tem caminhos claros e se uma recusa termina sem alterar a agenda.” |
| Conflito é um bug? | “Neste caso, conflito é a resposta prevista quando o horário está ocupado. Aceitar uma segunda reserva é que violaria a regra.” |
| O horário escolhido já fica ocupado? | “Neste algoritmo, não. Ele fica ocupado somente após todas as verificações e o registro da reserva.” |
| Posso conferir disponibilidade antes do nome? | “Existem outras ordens possíveis, mas elas podem mudar qual motivo de recusa aparece quando mais de um dado é inválido. Hoje usamos nome, catálogo e ocupação, alinhados à referência do curso.” |
| E se duas pessoas tentarem ao mesmo tempo? | “Hoje estamos percorrendo tentativas em sequência. Garantir reserva única com chamadas simultâneas exige controles e testes adicionais; nossa simulação não comprova isso.” |

**Feedback de exemplo:**

> Você identificou corretamente o conflito. Falta registrar quem continua no horário depois da recusa. Acrescente essa informação para que outra pessoa consiga conferir a preservação da reserva.

## 85–90 — Fechamento e tarefa para casa

**Fala de fechamento:**

> Hoje vocês transformaram uma regra de negócio em passos e conferiram esses passos com entradas diferentes. Aprenderam a distinguir o que recebemos, o que verificamos, o que respondemos e como a agenda fica depois.
>
> Guardem essa ideia: para conferir uma solução, precisamos de uma regra, de uma entrada concreta e de um resultado que possa ser explicado.
>
> Na próxima aula, vamos representar informações com variáveis e tipos de dados e aprofundar decisões. O raciocínio de hoje será a base.

**Pedir uma resposta curta no chat ou caderno:**

> Complete: “A tentativa foi recusada porque ___, e a agenda ficou ___.”

**Tarefa — entrega para a próxima aula, 30–45 minutos:**

1. Revisar algoritmo e tabela com o feedback.
2. Criar uma tentativa nova que não repita exatamente as entradas da aula.
3. Registrar estado inicial, entrada, resultado esperado, passo decisivo e estado final.
4. Explicar uma mudança entre a primeira versão e a revisada.
5. Salvar como `m02-aula-01-revisao.md`.

**Fala de orientação:**

> Usem a gravação para rever o trecho em que tiveram dúvida. Depois tentem resolver sem acompanhar a resposta pronta. Entreguem a primeira versão e a revisão; assim conseguimos observar o que vocês compreenderam e o que ainda precisa de apoio.

**Exemplo para conferir depois da tentativa:** H12 não pertence ao catálogo; com nome válido, deve ser recusado por horário inválido, sem alterar a agenda.  
**Desafio opcional:** explicar quais dados faltam para limitar reservas por cliente; nomes podem se repetir, então não assumir nome como identificador único.

## Checklist final do professor

- [ ] Alunos distinguiram entrada, processamento, saída e estado.
- [ ] Demonstração mostrou sucesso e recusa na mesma agenda.
- [ ] Prática em dupla alternou condução e revisão.
- [ ] Exercício individual usou entradas diferentes.
- [ ] Correção conferiu estado e resultado, sem exigir frase idêntica.
- [ ] Ficou claro que esta aula não exige execução de código.
- [ ] Tarefa e formato de entrega foram explicados.
- [ ] Dúvidas pendentes foram registradas para retorno.

**Após o encontro:** disponibilizar a gravação e indicar os trechos de conceitos, demonstração e correção. Usar o início da próxima aula para retomar a lacuna mais frequente nas entregas. A plataforma registra visualização; a tabela e a explicação demonstram a compreensão.
