# Script do Professor — Funções e Resolução de Problemas

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 2, Aula 4](../modulo-02-aula-04-funcoes-e-desafios.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-02-logica-de-programacao.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  

## Alinhamento obrigatório

- **Objetivo:** Usar funções para encapsular responsabilidades e aplicar depuração orientada por hipótese em uma validação simples.
- **Demonstração central:** Implementar, reproduzir e corrigir `validar_nome`.
- **Prática em grupo:** Função sob revisão.
- **Exercício individual:** escrever a função e explicar o limite de responsabilidade.
- **Tarefa:** consolidar as atividades de lógica e revisar a entrega do módulo.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Confirmar Python disponível.
- [ ] Preparar as três entradas de teste.
- [ ] Separar exemplo curto de `print` versus `return`.
- [ ] Deixar o roteiro e este script abertos.
- [ ] Testar qualquer ferramenta, arquivo ou demonstração antes da turma entrar.
- [ ] Separar o material que o aluno deverá entregar ao final.

## Agenda de condução

| Intervalo | Etapa |
|---|---|
| 00–08 | Abertura e diagnóstico |
| 08–25 | Conceitos e exemplos |
| 25–45 | Demonstração guiada |
| 45–50 | Pausa |
| 50–65 | Dinâmica |
| 65–77 | Exercício individual |
| 77–85 | Correção e dúvidas |
| 85–90 | Fechamento e tarefa |

## 00–08 — Abertura e diagnóstico

**Fala de abertura:**

> Se copiarmos a mesma validação em vários lugares, o que acontece quando uma cópia muda e outra não? Hoje vamos dar uma responsabilidade clara a uma função e investigar um erro lógico.

**Pergunta diagnóstica:** Uma função que imprime `True` necessariamente devolve `True` para quem a chamou?

Dê cerca de dois minutos para respostas curtas no chat, voz ou caderno. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Não. Exibição e retorno são operações diferentes.

**Transição:**

> Vamos definir primeiro o contrato da função e depois usar entradas concretas para investigar um comportamento incorreto.

## 08–25 — Conceitos e exemplos

### 1. Funções e responsabilidade

**Fala sugerida:**

> Uma função recebe informações, executa uma responsabilidade e pode devolver um resultado. `validar_nome` não deveria reservar horário; ela deveria responder sobre o nome.

**Mostrar/fazer:** assinatura `def validar_nome(nome):`.

**Perguntar:** Que informação entra e qual resultado deve sair?

**Compreensão esperada:** texto entra; um booleano de validade sai.

### 2. `print` versus `return`

**Fala sugerida:**

> Mostrar algo na tela e devolver um valor para quem chamou a função são coisas diferentes.

**Mostrar/fazer:** uma função que apenas imprime e outra que retorna.

**Perguntar:** Qual delas permite usar o resultado em uma condição?

**Compreensão esperada:** a que retorna valor.

### 3. Depuração por hipótese

**Fala sugerida:**

> Depurar não é alterar linhas aleatoriamente. Primeiro reproduzimos, depois formulamos uma hipótese e verificamos se a mudança explica o comportamento.

**Mostrar/fazer:** `nome != ''` versus `bool(nome.strip())`.

**Perguntar:** Por que `'   '` passa na primeira expressão?

**Compreensão esperada:** porque é uma string não vazia, apesar de conter apenas espaços.

Evite transformar este bloco em leitura do E-book. Use o E-book como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Implementar, reproduzir e corrigir `validar_nome`

### Passo 1 — Definir contrato da função

**Fazer:** Escreva nome, entrada e saída esperada.

**Fala sugerida:**

> Antes do corpo, vamos definir a responsabilidade. Isso evita colocar regra de reserva dentro de uma validação de nome.

**Checar com a turma:** Pergunte se a função deveria alterar a agenda.

### Passo 2 — Comparar duas validações

**Fazer:** Execute `'   ' != ''` e `bool('   '.strip())`.

**Fala sugerida:**

> O programa não travou; mesmo assim a primeira regra está errada para o nosso negócio. Esse é um erro lógico.

**Checar com a turma:** Peça que a turma formule a hipótese antes de mostrar `strip`.

### Passo 3 — Retestar após correção

**Fazer:** Repita Ana, vazio e espaços.

**Fala sugerida:**

> Corrigir um caso não encerra a investigação. Precisamos confirmar que o comportamento válido continua válido.

**Checar com a turma:** Pergunte por que testar Ana novamente é importante.

**Resultado de referência:** `validar_nome('Ana')` → True; `validar_nome('')` e `validar_nome('   ')` → False. `return` devolve valor; `print` apenas exibe.

Antes de mostrar o resultado, peça uma previsão. Depois compare previsão, comportamento observado e explicação.

## 45–50 — Pausa

Informar claramente o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Função sob revisão

**Cenário:** Uma dupla recebe uma função de validação e três entradas; uma pessoa explica e a outra tenta encontrar um contraexemplo.

**Orientação para a turma:**

> Quem revisa não precisa ‘achar defeito’ a qualquer custo; precisa tentar confirmar ou refutar a regra.

1. Definir responsabilidade da função.
2. Executar/prever três entradas.
3. Comparar validação defeituosa e corrigida.
4. Trocar papéis e propor um novo caso.

**Tempo sugerido:** 2 min para organização, 8 min para produção, 3 min para revisão entre pares e 2 min para compartilhamento.

**Entrega esperada:** função + tabela entrada/esperado/observado

**O professor observa:** responsabilidade delimitada; retornos corretos; hipótese do bug explicada; reteste após correção.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Escreva `validar_nome` em Python ou pseudocódigo e registre os retornos para Ana, vazio e espaços. Depois responda: quem deve decidir se um horário pode ser reservado — `validar_nome` ou a operação de reserva? Justifique.

**Entrega:** função + três resultados + justificativa

**Critérios:** função correta; retorno em vez de apenas impressão; responsabilidade separada; justificativa coerente.

**Se houver dificuldade:** permita primeiro escrever a regra em português e depois converter para código.

## 77–85 — Correção, intervenções e dúvidas

Comece pedindo que o aluno explique como chegou à resposta antes de mostrar uma referência.

**Se aparecer:** a função valida nome e já cria a reserva

> Qual responsabilidade conseguimos isolar para testar separadamente? `validar_nome` deve apenas responder sobre o nome.

**Se aparecer:** o aluno muda várias linhas de uma vez

> Qual hipótese estamos testando? Mude uma coisa que responda à hipótese e repita os mesmos casos.

**Se aparecer:** o aluno usa `print` onde precisa de retorno

> Quem chama essa função consegue usar o valor exibido em uma condição? O que precisa ser devolvido?

### Perguntas de verificação

- **Mostrar um resultado com `print` significa que a função o retornou?** — Não. `print` exibe; `return` entrega o valor ao chamador.
- **Por que espaços passam em `nome != ''`?** — Porque a string contém caracteres de espaço e, portanto, não é vazia.
- **Depois de corrigir o bug, por que testar novamente um nome válido?** — Para confirmar que a correção não quebrou o comportamento que já funcionava.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> O ponto principal não é decorar `def` ou `strip`. É aprender a separar responsabilidades, reproduzir um problema e confirmar a correção com casos controlados.

**Tarefa para casa:**

1. Revisar a função e a investigação do bug.
2. Organizar as atividades do módulo.
3. Resolver um mini desafio próprio de validação ou repetição.
4. Registrar uma reflexão sobre o que mudou no seu raciocínio.

**Entrega:** entrega final do Módulo 2 organizada e revisada

**Ponte para a próxima aula:**

> No próximo módulo vocês vão começar a enxergar como essa lógica aparece dentro de um projeto real e como mudanças são registradas com Git e GitHub.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se a atividade usada foi a mesma definida no roteiro.
- [ ] Anotar qualquer ajuste de tempo para a próxima turma.
- [ ] Não alterar critérios ou respostas de referência apenas na fala; se a regra mudar, atualizar roteiro e script juntos.
