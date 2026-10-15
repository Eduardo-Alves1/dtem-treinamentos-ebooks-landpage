# Script do Professor — Git e Histórico Local

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 3, Aula 3](../modulo-03-aula-03-git-e-versionamento.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Ensinar versionamento local com Git, distinguindo diretório de trabalho, área de preparação e histórico de commits.
- **Demonstração central:** Criar três commits locais com intenção clara.
- **Prática em grupo:** Organize o histórico.
- **Exercício individual:** produzir um commit e explicar seu propósito.
- **Tarefa:** consolidar três commits e explicar o histórico.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Confirmar Git instalado.
- [ ] Preparar pasta de laboratório separada.
- [ ] Não usar repositório importante do aluno para demonstrações destrutivas.
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

> Salvar um arquivo cria automaticamente um histórico que explica o que mudou e por quê? Hoje vamos separar arquivo atual, mudanças preparadas e versão registrada.

**Pergunta diagnóstica:** Qual diferença entre salvar um arquivo e fazer um commit?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Salvar muda o arquivo; commit registra uma versão selecionada no histórico.

**Transição:**

> Vamos transformar mudanças soltas em uma história que outra pessoa consiga revisar.

## 08–25 — Conceitos e exemplos

### 1. Estados do Git

**Fala sugerida:**

> Salvar muda o arquivo; versionar exige escolher o que entra em uma versão e registrar essa versão no histórico.

**Mostrar/fazer:** `git status` em três momentos.

**Perguntar:** Um arquivo salvo já pertence a um commit?

**Compreensão esperada:** não; depende de ter sido adicionado e commitado.

### 2. Diff e intenção

**Fala sugerida:**

> Um bom commit reúne mudanças que contam uma ideia coerente. Misturar correção de regra e reformatação dificulta revisão.

**Mostrar/fazer:** `git diff` e `git diff --staged`.

**Perguntar:** Por que separar duas intenções em commits diferentes?

**Compreensão esperada:** facilita revisão, histórico e reversão.

### 3. Histórico

**Fala sugerida:**

> O histórico permite investigar como o projeto evoluiu. A mensagem ajuda, mas a evidência está na mudança registrada.

**Mostrar/fazer:** `git log --oneline`.

**Perguntar:** O hash precisa ser decorado?

**Compreensão esperada:** não; é identificador, não conhecimento a memorizar.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Criar três commits locais com intenção clara

### Passo 1 — Inicializar e observar

**Fazer:** Execute `git init` e `git status`.

**Fala sugerida:**

> O Git começa nos dizendo o que ele conhece e o que ainda não está rastreado. Vamos usar o status como nosso painel.

**Checar com a turma:** Pergunte qual arquivo está fora do histórico.

### Passo 2 — Preparar e comparar

**Fazer:** Use `git diff`, `git add` e `git diff --staged`.

**Fala sugerida:**

> Antes de gravar uma versão, eu quero saber exatamente o que estou colocando nela.

**Checar com a turma:** Peça a diferença entre diff normal e staged.

### Passo 3 — Criar histórico legível

**Fazer:** Faça commits pequenos e mostre `git log --oneline`.

**Fala sugerida:**

> A meta não é ter muitos commits; é permitir que outra pessoa entenda a evolução.

**Checar com a turma:** Mostre duas mudanças distintas e pergunte se deveriam estar no mesmo commit.

**Resultado de referência:** Histórico esperado com pelo menos três intenções separadas. Hashes variam; a coerência entre mudança e mensagem é o critério.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Organize o histórico

**Cenário:** A dupla recebe um conjunto de mudanças misturadas em README e código.

**Orientação para a turma:**

> Não tentem criar um commit por arquivo. Criem um commit por intenção compreensível.

1. Separar as mudanças por intenção.
2. Escolher o que seria preparado primeiro.
3. Propor mensagens de commit.
4. Revisar se cada commit conta uma ideia.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** plano de commits + evidência de status/diff

**O professor observa:** intenção clara; mudanças coerentes por commit; uso correto de status/diff.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Faça ou simule um terceiro commit de melhoria de documentação. Mostre o estado antes, o que foi preparado e a mensagem final. Explique a diferença entre `git diff` e `git diff --staged`.

**Entrega:** registro do commit ou evidência equivalente

**Critérios:** estado conferido; mudança preparada conscientemente; mensagem coerente; diferença entre diffs explicada.

**Se houver dificuldade:** se Git estiver indisponível, use uma tabela ‘arquivo atual → alteração → versão planejada’, mas conclua a execução depois.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** o aluno usa `git add .` sem conferir nada

> Pode funcionar, mas qual evidência mostra que você sabe o que está preparando? Confira status e diff antes.

**Se aparecer:** mensagem ‘ajustes’

> Que intenção alguém deveria entender meses depois? Escreva a mudança em termos de propósito.

**Se aparecer:** o aluno confunde Git e GitHub

> Git é o sistema de versionamento local; GitHub é uma plataforma que pode hospedar e colaborar sobre repositórios Git.

### Perguntas de verificação

- **Salvar um arquivo cria uma versão no Git?** — Não. Salvar altera o diretório de trabalho; commit registra uma versão.
- **Para que serve a staging area?** — Selecionar quais mudanças farão parte do próximo commit.
- **Um commit deve ser grande ou pequeno?** — Deve ser coerente; pequeno o suficiente para explicar uma intenção, sem regra numérica universal.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Git não serve apenas para ‘subir código’. Ele registra decisões técnicas e permite comparar versões com muito mais segurança.

**Tarefa para casa:**

1. Revisar os commits.
2. Corrigir mensagens se necessário em um laboratório descartável.
3. Registrar `git log --oneline`.
4. Entregar `m03-aula-03-revisao.md`.

**Entrega:** histórico local com explicação das intenções

**Ponte para a próxima aula:**

> Na próxima aula vamos compartilhar esse histórico e aprender como outra pessoa pode revisar uma mudança sem sobrescrever o trabalho principal.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
