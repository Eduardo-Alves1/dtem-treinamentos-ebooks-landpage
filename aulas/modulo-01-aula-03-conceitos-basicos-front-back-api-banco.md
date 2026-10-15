# Roteiro de Aula — Módulo 1, Aula 3

# Conceitos Básicos: Front-end, Back-end, APIs e Banco de Dados

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-01-aula-03-conceitos-basicos-front-back-api-banco.md).

## Objetivo da aula

Apresentar as principais camadas de uma aplicação para que o iniciante consiga distinguir interface, processamento, comunicação e armazenamento.

Ao final, o aluno deverá conseguir:

- diferenciar front-end e back-end
- explicar API de forma simples
- explicar o papel de banco de dados
- desenhar um fluxo front-end → API/back-end → banco → resposta
- relacionar as camadas a QA, Produto e Desenvolvimento

## Conteúdos e conceitos

### Front-end e back-end
- interface e interação
- regras e processamento
- as duas partes se complementam

### API e requisição/resposta
- interface de comunicação
- entrada, método e resposta
- JSON como formato comum

### Banco de dados e persistência
- armazenamento estruturado
- consulta e alteração de dados
- integridade e segurança

## Duração e blocos

| Bloco | Tempo previsto |
|---|---:|
| Abertura e diagnóstico | 8 min |
| Conceitos e exemplos | 17 min |
| Demonstração guiada | 20 min |
| Pausa | 5 min |
| Dinâmica em dupla ou grupo | 15 min |
| Exercício individual | 12 min |
| Correção e dúvidas | 8 min |
| Fechamento e tarefa | 5 min |
| **Total** | **90 min** |

## Materiais necessários

- [E-book do Módulo 1](../ebooks/modulo-01-fundamentos.md)
- [Caderno de prática do Módulo 1](../atividades/modulo-01-caderno-de-pratica.md)
- quadro branco ou ferramenta visual
- navegador
- exemplo de tela de cadastro
- exemplo de JSON
- tabela simples simulando banco de dados

## Exemplos planejados

### Exemplo 1
Cadastro de aluno na DTEM.

### Exemplo 2
Compra em e-commerce.

### Exemplo 3
Solicitação de corrida em aplicativo de transporte.

## Demonstração planejada — Cadastro de aluno atravessando as camadas

1. Desenhar uma tela de cadastro com nome, e-mail e senha.
2. Mostrar a coleta dos dados no front-end.
3. Representar uma requisição JSON para uma API.
4. Explicar a regra no back-end e o registro no banco.
5. Retornar sucesso ou erro para a tela.

**Resultado pedagógico esperado:** o aluno enxerga o caminho completo sem confundir camada com ferramenta.

## Dinâmica em grupo — Separe as camadas

**Cenário:** A turma recebe itens misturados de uma aplicação: botão, regra de senha, tabela de usuários, endpoint /login, mensagem de erro, cálculo de frete, consulta SQL, resposta JSON e dashboard.

1. Classificar os itens em Front-end, Back-end, API, Banco de dados ou Dados/BI.
2. Escolher três itens e justificar a classificação.
3. Apontar um item que possa gerar dúvida e explicar por quê.

**Entrega esperada:** quadro de classificação com justificativas

**Critérios:** diferenças conceituais corretas; justificativas claras; capacidade de reconhecer ambiguidade.

## Exercício individual

Escolha login, cadastro, compra, agendamento, certificado ou recuperação de senha. Desenhe front-end, API, back-end e banco; indique os dados enviados, uma resposta esperada e três possíveis erros.

**Entrega:** fluxo técnico simplificado da funcionalidade

**Critérios:** quatro camadas identificadas; entrada e resposta presentes; três erros plausíveis; sem afirmar arquitetura real de uma empresa específica.

## Perguntas de verificação

- API e banco de dados são a mesma coisa?
- Front-end é apenas design?
- Por que QA e Produto precisam entender essas camadas?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Escolher um aplicativo e uma funcionalidade.
2. Descrever o que seria front-end, back-end, API e dados armazenados.
3. Listar testes importantes.
4. Adicionar front-end, back-end, API, banco, JSON, requisição e resposta ao mapa mental.

**Entrega:** análise da funcionalidade + mapa mental atualizado

## Conexão com a trilha

A Aula 4 usa pensamento computacional para organizar problemas e fecha o Módulo 1 com o mapa mental final.

## Referências

- [E-book correspondente](../ebooks/modulo-01-fundamentos.md)
- [Caderno de prática](../atividades/modulo-01-caderno-de-pratica.md)
- [Script do professor](scripts/modulo-01-aula-03-conceitos-basicos-front-back-api-banco.md)
