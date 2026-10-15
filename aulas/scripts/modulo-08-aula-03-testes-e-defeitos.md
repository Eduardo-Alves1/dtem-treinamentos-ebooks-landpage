# Script do Professor — Testes, Defeitos e Evidências

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar uma aula paralela.

**Roteiro:** [Módulo 8, Aula 3](../modulo-08-aula-03-testes-e-defeitos.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-08-projeto-final-hands-on.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Executar e organizar as evidências do projeto final, distinguindo teste executado, BUG01 reproduzível e BUG02 fornecido como incidente fictício que não deve ser apresentado como execução.
- **Demonstração central:** Executar BUG01 e analisar BUG02 corretamente.
- **Prática em grupo:** Provar comportamento.
- **Exercício individual:** executar um caso autoral e emitir parecer.
- **Tarefa:** consolidar oito casos, bugs, reteste e evidências.

## Antes da aula

- [ ] Resetar estado entre casos.
- [ ] Confirmar referência/variante.
- [ ] Separar BUG02 e deixar claro que não é executável no código fornecido.
- [ ] Deixar roteiro e script abertos.
- [ ] Conferir materiais, dados e exemplos.
- [ ] Separar a entrega esperada da aula.

## Agenda

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

> Hoje a qualidade da evidência vale mais que uma lista longa de testes marcados como ‘passou’. Vamos registrar apenas o que conseguimos realmente demonstrar.

**Pergunta diagnóstica:** Se recebemos um bug de uma versão que não possuímos, podemos afirmar que o reproduzimos?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** Não. Podemos analisar o relato e preparar um plano de reprodução, mas não inventar execução.

**Transição:**

> Vamos comparar um defeito que conseguimos executar com outro que existe apenas como registro fornecido.

## 08–25 — Conceitos e exemplos

### 1. Evidência de execução

**Fala sugerida:**

> No projeto final, dizer ‘testei’ exige informação que permita conferir. Precisamos saber em qual versão, com quais dados e o que foi observado.

**Mostrar/fazer:** registro de um caso executado.

**Perguntar:** Screenshot sozinho prova toda a sequência?

**Compreensão esperada:** não necessariamente; contexto e dados também importam.

### 2. BUG01 versus BUG02

**Fala sugerida:**

> BUG01 pode ser reproduzido no código fornecido. BUG02 descreve um incidente de uma versão que não existe no laboratório. O tratamento precisa ser diferente.

**Mostrar/fazer:** dois registros lado a lado.

**Perguntar:** O que podemos afirmar sobre BUG02?

**Compreensão esperada:** podemos analisar, propor reprodução e critérios; não afirmar que executamos.

### 3. Parecer proporcional

**Fala sugerida:**

> Parecer bom não transforma ausência de evidência em aprovação. Ele resume o que foi demonstrado, o que falhou e o que continua pendente.

**Mostrar/fazer:** verificado / não verificado / decisão.

**Perguntar:** O que fazer se um caso crítico não foi executado?

**Compreensão esperada:** registrar pendência e limitar decisão.

## 25–45 — Demonstração guiada — Executar BUG01 e analisar BUG02 corretamente

### Passo 1 — Controlar a execução

**Fazer:** Registre versão e estado antes do caso.

**Fala sugerida:**

> A evidência começa antes do clique/comando: preciso saber em que condições estou executando.

**Checar com a turma:** Peça versão e estado inicial.

### Passo 2 — Reproduzir BUG01

**Fazer:** Execute nome com espaços na variante.

**Fala sugerida:**

> Aqui temos código e comportamento observável. Posso afirmar reprodução porque consigo demonstrar a divergência.

**Checar com a turma:** Peça esperado, observado e estado.

### Passo 3 — Analisar BUG02

**Fazer:** Abra o relato fictício sem tentar ‘executá-lo’ na referência.

**Fala sugerida:**

> Este incidente é material de análise. A versão descrita não existe aqui. Vou escrever como confirmaria, mas não direi que confirmei.

**Checar com a turma:** Peça ao aluno para formular passos e critério de confirmação.

**Resultado de referência:** BUG01 é reproduzível na variante e pode ser retestado na referência. BUG02 deve permanecer identificado como incidente fictício fornecido; só cabe plano de investigação/critério, não resultado inventado.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Provar comportamento

**Cenário:** Cada dupla recebe um caso executável e um registro fornecido que precisa ser analisado.

> Se vocês não executaram, escrevam ‘não executado’. Honestidade da evidência vale mais que preencher todas as caixas.

1. Executar o caso com versão/estado registrados.
2. Separar observado de hipótese.
3. Analisar o registro fornecido.
4. Escrever o que seria necessário para reproduzi-lo.
5. Trocar evidências com outra dupla para conferência.

**Entrega:** registro de execução + plano de investigação

**Observar:** fonte da evidência clara; nenhuma execução inventada; estado/versão presentes; plano de confirmação reproduzível.

## 65–77 — Exercício individual

> Crie uma sequência nova de rejeição, execute na versão disponível e registre entrada, estado, esperado, observado e resultado. Depois escreva uma frase dizendo o que essa evidência permite — e não permite — concluir.

**Entrega:** caso autoral executado + conclusão limitada

**Critérios:** execução verificável; esperado independente; limite da conclusão; versão identificada.

**Ajuda graduada:** comece por uma regra já conhecida e altere apenas um dado de entrada.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** o aluno marca BUG02 como reproduzido porque o relato já descreve passos

> Você executou esses passos na mesma versão citada? Se não, mantenha como incidente fornecido e plano de confirmação.

**Se aparecer:** o aluno usa resultado da referência como prova sobre a versão fictícia

> Versões diferentes podem se comportar diferente. Evidência pertence à versão executada.

**Se aparecer:** o aluno escreve ‘sistema aprovado’ após poucos casos

> Qual escopo exato foi verificado? Restrinja o parecer aos casos e riscos cobertos.

### Perguntas de verificação

- **Posso dizer que reproduzi BUG02?** — Não, porque a versão defeituosa descrita não está disponível no laboratório.
- **Uma evidência de um caso prova todo o sistema?** — Não. Sustenta apenas o comportamento e condições investigadas.
- **Qual diferença entre ‘não encontrei falha’ e ‘não existe falha’?** — A primeira descreve a execução; a segunda é uma afirmação absoluta que testes não conseguem garantir.

## 85–90 — Fechamento e tarefa

> Portfólio técnico ganha credibilidade quando distingue claramente o que foi executado, simulado, fornecido e apenas proposto.

1. Executar/conferir os oito casos previstos.
2. Organizar BUG01 com reteste.
3. Manter BUG02 como incidente fornecido com plano de confirmação.
4. Atualizar matriz de rastreabilidade.
5. Entregar `m08-aula-03-revisao.md`.

**Entrega:** bloco de qualidade do dossiê

**Ponte:**

> Na próxima aula vamos transformar esses artefatos em uma história profissional verificável: problema, decisão, demonstração, contribuição e limites.

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
