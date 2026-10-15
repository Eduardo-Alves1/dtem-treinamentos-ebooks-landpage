# Script do Professor — Cenários e Testes Funcionais

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 4, Aula 2](../modulo-04-aula-02-cenarios-e-testes-funcionais.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-04-qualidade-de-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Transformar regras em cenários e casos funcionais reproduzíveis, separando resultado esperado de resultado observado.
- **Demonstração central:** Escrever e executar casos funcionais.
- **Prática em grupo:** Do requisito à evidência.
- **Exercício individual:** escrever caso de cancelamento inexistente.
- **Tarefa:** revisar casos e executar nas versões disponíveis.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Zerar estado antes das execuções.
- [ ] Preparar modelo de caso.
- [ ] Confirmar as duas versões do laboratório.
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

> Quando alguém diz ‘eu testei a reserva’, o que exatamente foi feito? Se outra pessoa não consegue repetir, ainda falta transformar intenção em caso de teste.

**Pergunta diagnóstica:** Que informações mínimas outra pessoa precisa para reproduzir um teste?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** pré-condição/estado, dados, ação/passos e resultado esperado; versão/ambiente quando relevante.

**Transição:**

> Vamos derivar o esperado da regra e só depois olhar para o comportamento da implementação.

## 08–25 — Conceitos e exemplos

### 1. Cenário versus caso

**Fala sugerida:**

> ‘Testar reserva’ é amplo. Um caso reproduzível precisa dizer em que estado começamos, o que fazemos e o que esperamos.

**Mostrar/fazer:** RN03 transformada em caso.

**Perguntar:** Que informação falta para outra pessoa repetir?

**Compreensão esperada:** dados, estado inicial, passos e esperado.

### 2. Esperado antes do observado

**Fala sugerida:**

> Escrevemos o esperado antes de olhar o resultado para evitar racionalizar um comportamento incorreto depois.

**Mostrar/fazer:** nome com espaços.

**Perguntar:** Qual esperado vem da RN03?

**Compreensão esperada:** nome_invalido e estado preservado.

### 3. Cobertura funcional

**Fala sugerida:**

> Cobertura não é quantidade aleatória de casos. Ela representa situações relevantes da regra e do risco.

**Mostrar/fazer:** sucesso, conflito, entrada inválida e cancelamento.

**Perguntar:** Qual caso negativo protege a reserva já existente?

**Compreensão esperada:** tentativa de reservar horário ocupado deve retornar conflito e preservar reserva.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Escrever e executar casos funcionais

### Passo 1 — Escrever antes de executar

**Fazer:** Monte TC03 completo.

**Fala sugerida:**

> A regra vem antes da execução. O esperado não deve ser reescrito só porque o programa fez outra coisa.

**Checar com a turma:** Peça o esperado para espaços e H11.

### Passo 2 — Comparar versões

**Fazer:** Execute referência e variante.

**Fala sugerida:**

> Mesma entrada, versões diferentes. Vamos registrar exatamente o que mudou, inclusive o estado da agenda.

**Checar com a turma:** Pergunte qual versão viola a regra.

### Passo 3 — Testar conflito

**Fazer:** Reserve H09 e tente novamente.

**Fala sugerida:**

> Não basta receber conflito. Precisamos confirmar que a reserva original permaneceu.

**Checar com a turma:** Peça evidência de estado após a recusa.

**Resultado de referência:** RN03: espaços → `nome_invalido`, sem ocupar H11. RN05: segunda tentativa em H09 → conflito e reserva original preservada.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Do requisito à evidência

**Cenário:** Cada dupla recebe uma regra diferente de RN01–RN08.

**Orientação para a turma:**

> A revisão deve responder: eu conseguiria repetir este caso sem perguntar nada ao autor?

1. Escrever um caso com dados e estado inicial.
2. Definir esperado antes de executar.
3. Executar ou simular declaradamente.
4. Registrar observado e estado final.
5. Trocar caso com outra dupla para verificar reproduzibilidade.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** caso funcional revisado por outra dupla

**O professor observa:** vínculo com regra; esperado explícito; dados suficientes; estado final observado.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Escreva o caso de RN07 para cancelar um ID inexistente enquanto existe outra reserva válida. Inclua estado inicial, ação, esperado e o que deve permanecer inalterado.

**Entrega:** caso funcional individual

**Critérios:** RN07 ligada; estado preservado; dados claros; resultado verificável.

**Se houver dificuldade:** comece pelo ‘antes’ e pelo ‘depois’ desejado antes de escrever os passos.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** o aluno escreve esperado igual ao que a variante fez

> Volte à regra. O que deveria acontecer independentemente da implementação atual?

**Se aparecer:** o caso não tem estado inicial

> Se outra pessoa começar com uma agenda diferente, o resultado pode mudar. O que precisa estar verdadeiro antes do teste?

**Se aparecer:** o aluno confunde quantidade de casos com cobertura

> Quais riscos/regras esses casos representam? Mais casos sem propósito não significam melhor cobertura.

### Perguntas de verificação

- **O esperado pode ser definido depois de executar?** — O ideal é derivá-lo da regra antes, para evitar ajustar a expectativa ao comportamento observado.
- **Caso de teste é só uma lista de cliques?** — Não. Precisa representar regra, dados, estado e resultado observável.
- **Por que registrar estado depois de uma recusa?** — Porque uma operação pode retornar erro e ainda assim alterar dados indevidamente.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Um bom caso não serve apenas para marcar aprovado ou reprovado; ele torna o comportamento discutível e reproduzível.

**Tarefa para casa:**

1. Revisar os casos com feedback.
2. Executar nas versões disponíveis.
3. Registrar versão, esperado, observado e evidência.
4. Entregar `m04-aula-02-revisao.md`.

**Entrega:** casos revisados + registros de execução

**Ponte para a próxima aula:**

> Na próxima aula vamos sair do roteiro totalmente previsto, explorar comportamentos e aprender a comunicar um bug que outra pessoa consiga reproduzir.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
