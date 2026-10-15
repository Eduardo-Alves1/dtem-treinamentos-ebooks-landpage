# Script do Professor — Conceitos Básicos: Front-end, Back-end, APIs e Banco de Dados

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 1, Aula 3](../modulo-01-aula-03-conceitos-basicos-front-back-api-banco.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-01-fundamentos.md)  
**Caderno:** [prática do Módulo 1](../../atividades/modulo-01-caderno-de-pratica.md)  

## Alinhamento obrigatório

- **Objetivo:** Apresentar as principais camadas de uma aplicação para que o iniciante consiga distinguir interface, processamento, comunicação e armazenamento.
- **Demonstração central:** Cadastro de aluno atravessando as camadas.
- **Prática em grupo:** Separe as camadas.
- **Exercício individual:** desenhar o fluxo técnico de uma funcionalidade.
- **Tarefa:** analisar uma funcionalidade de um aplicativo e atualizar o mapa mental.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Preparar a tela de cadastro.
- [ ] Preparar um JSON simples sem dados sensíveis.
- [ ] Preparar uma tabela fictícia de usuários.
- [ ] Evitar demonstração de código profundo; o objetivo é conceitual.
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

> Vou mostrar uma tela de login. O que vocês conseguem ver? E o que vocês imaginam que acontece depois que clicamos em ‘Entrar’?

**Pergunta diagnóstica:** Onde o sistema verifica os dados e onde eles ficam armazenados?

Dê cerca de dois minutos para respostas curtas no chat, voz ou caderno. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** A resposta inicial pode ser incompleta; ao final o aluno deverá distinguir interface, back-end/API e banco.

**Transição:**

> Vamos desmontar uma funcionalidade em camadas para entender por onde a informação passa.

## 08–25 — Conceitos e exemplos

### 1. Front-end e back-end

**Fala sugerida:**

> Front-end é a parte com que o usuário interage. Back-end processa regras e operações que não precisam estar visíveis. Uma tela bonita não diz, sozinha, como a regra foi implementada.

**Mostrar/fazer:** use uma tela simples de login/cadastro.

**Perguntar:** O que vemos e o que precisa acontecer por trás quando clicamos em Entrar?

**Compreensão esperada:** o aluno separa interface observável de processamento interno.

### 2. API e requisição/resposta

**Fala sugerida:**

> A API funciona como um contrato de comunicação. Ela recebe uma requisição, encaminha uma operação e devolve uma resposta. Não é uma tela e não é o banco.

**Mostrar/fazer:** escreva POST /login com JSON simples.

**Perguntar:** Que informação entra e que resposta poderia voltar?

**Compreensão esperada:** o aluno identifica comunicação entre partes.

### 3. Banco de dados e persistência

**Fala sugerida:**

> Banco de dados é onde informações persistentes são organizadas. O back-end pode consultar ou alterar esses dados; a API não ‘vira’ o banco.

**Mostrar/fazer:** uma tabela simples de alunos.

**Perguntar:** Que dados uma plataforma de cursos precisa guardar?

**Compreensão esperada:** o aluno diferencia armazenamento de lógica e interface.

Evite transformar este bloco em leitura do E-book. Use o E-book como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Cadastro de aluno atravessando as camadas

### Passo 1 — Começar pela tela

**Fazer:** Desenhe campos e botão Criar conta.

**Fala sugerida:**

> Isso é o que o usuário observa. A partir daqui começam perguntas sobre validação e comportamento, mas ainda não vimos como a regra interna funciona.

**Checar com a turma:** Peça dois exemplos de validação visual.

### Passo 2 — Mostrar a comunicação

**Fazer:** Escreva uma requisição JSON simples e uma resposta.

**Fala sugerida:**

> A tela precisa conversar com outra parte do sistema. Vamos representar isso como uma chamada de API.

**Checar com a turma:** Pergunte se a API é o banco de dados e deixe a turma justificar.

### Passo 3 — Chegar ao armazenamento e voltar

**Fazer:** Mostre uma tabela de usuários e desenhe o retorno.

**Fala sugerida:**

> O back-end pode validar e persistir os dados. Depois devolve um resultado, que o front-end transforma em mensagem para a pessoa.

**Checar com a turma:** Peça três pontos em que um erro poderia ocorrer.

**Resultado de referência:** Fluxo conceitual: usuário → front-end → requisição/API → regra no back-end → banco de dados → resposta → front-end. A arquitetura real pode variar.

Antes de mostrar o resultado, peça uma previsão. Depois compare previsão, comportamento observado e explicação.

## 45–50 — Pausa

Informar claramente o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Separe as camadas

**Cenário:** A turma recebe itens misturados de uma aplicação: botão, regra de senha, tabela de usuários, endpoint /login, mensagem de erro, cálculo de frete, consulta SQL, resposta JSON e dashboard.

**Orientação para a turma:**

> Classificar é menos importante do que justificar. Se um item puder envolver mais de uma camada, expliquem qual aspecto vocês estão considerando.

1. Classificar os itens em Front-end, Back-end, API, Banco de dados ou Dados/BI.
2. Escolher três itens e justificar a classificação.
3. Apontar um item que possa gerar dúvida e explicar por quê.

**Tempo sugerido:** 2 min para organização, 8 min para produção, 3 min para revisão entre pares e 2 min para compartilhamento.

**Entrega esperada:** quadro de classificação com justificativas

**O professor observa:** diferenças conceituais corretas; justificativas claras; capacidade de reconhecer ambiguidade.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Escolha login, cadastro, compra, agendamento, certificado ou recuperação de senha. Desenhe front-end, API, back-end e banco; indique os dados enviados, uma resposta esperada e três possíveis erros.

**Entrega:** fluxo técnico simplificado da funcionalidade

**Critérios:** quatro camadas identificadas; entrada e resposta presentes; três erros plausíveis; sem afirmar arquitetura real de uma empresa específica.

**Se houver dificuldade:** use primeiro apenas as quatro caixas e peça ao aluno para colocar uma seta e uma informação em cada passagem.

## 77–85 — Correção, intervenções e dúvidas

Comece pedindo que o aluno explique como chegou à resposta antes de mostrar uma referência.

**Se aparecer:** “API guarda os dados.”

> A API pode acionar uma operação que lê ou grava dados, mas o armazenamento persistente é responsabilidade de outra camada, como um banco.

**Se aparecer:** “Back-end é o banco.”

> Back-end executa regras e processamento; banco é um mecanismo de armazenamento. Eles se relacionam, mas não são a mesma coisa.

**Se aparecer:** “Se a tela mostrou erro, o problema é no front-end.”

> A mensagem está no front, mas a causa pode estar na validação da interface, API, regra de back-end, integração ou dados. Precisamos de evidência.

### Perguntas de verificação

- **API e banco de dados são a mesma coisa?** — Não. API é interface/contrato de comunicação; banco armazena dados.
- **Front-end é apenas design?** — Não. Inclui interface, comportamento, estados e integração com APIs.
- **Por que QA e Produto precisam entender essas camadas?** — Para discutir requisitos, riscos, cenários, origem de erros e limitações com mais precisão.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Mesmo quem não vai começar como desenvolvedor ganha muito quando consegue explicar onde uma informação entra, quem processa, onde persiste e como volta para o usuário.

**Tarefa para casa:**

1. Escolher um aplicativo e uma funcionalidade.
2. Descrever o que seria front-end, back-end, API e dados armazenados.
3. Listar testes importantes.
4. Adicionar front-end, back-end, API, banco, JSON, requisição e resposta ao mapa mental.

**Entrega:** análise da funcionalidade + mapa mental atualizado

**Ponte para a próxima aula:**

> Na próxima aula vamos usar esses conceitos para aprender a quebrar problemas em partes menores e organizar um raciocínio antes de buscar uma solução.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se a atividade usada foi a mesma definida no roteiro.
- [ ] Anotar qualquer ajuste de tempo para a próxima turma.
- [ ] Não alterar critérios ou respostas de referência apenas na fala; se a regra mudar, atualizar roteiro e script juntos.
