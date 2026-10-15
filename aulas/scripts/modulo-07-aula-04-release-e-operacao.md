# Script do Professor — Release, Operação e Resposta a Falhas

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O script operacionaliza o roteiro correspondente; não deve criar uma aula paralela.

**Roteiro:** [Módulo 7, Aula 4](../modulo-07-aula-04-release-e-operacao.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-07-ciclo-de-vida-do-software.md)  
**Caso:** [Agenda Clara](../../atividades/caso-agenda-clara.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Ensinar decisão de release baseada em evidências, diferenciar deploy de release e praticar resposta a falha dentro dos limites do laboratório educacional.
- **Demonstração central:** Executar checklist e tomar decisão de liberação.
- **Prática em grupo:** Liberar ou interromper.
- **Exercício individual:** definir gatilho de parada para RN02.
- **Tarefa:** consolidar SDLC, matriz e checklist.

## Antes da aula

- [ ] Preparar checklist.
- [ ] Selecionar falha crítica simulada.
- [ ] Reforçar limites do laboratório versus produção.
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

> Hoje vamos tomar uma decisão que junta todo o módulo: temos evidência suficiente para liberar o que prometemos demonstrar, e sabemos como reagir se algo crítico falhar?

**Pergunta diagnóstica:** Se o teste de conflito falhar, o que precisa acontecer antes de liberar o fluxo de reserva?

Ouça pelo menos duas respostas antes de completar.

**Referência para o professor:** interromper o escopo afetado, registrar, corrigir e retestar; não mascarar a falha.

**Transição:**

> Vamos transformar evidências em uma decisão de release explícita e, de propósito, introduzir uma falha para praticar resposta.

## 08–25 — Conceitos e exemplos

### 1. Deploy versus release

**Fala sugerida:**

> Deploy e release podem acontecer juntos ou separados. O importante é distinguir colocar uma versão no ambiente de decidir disponibilizá-la para uso.

**Mostrar/fazer:** fluxo build/deploy/release conceitual.

**Perguntar:** Podemos fazer deploy sem liberar para todos?

**Compreensão esperada:** em muitas estratégias, sim; depende da arquitetura/processo.

### 2. Critérios de liberação

**Fala sugerida:**

> Release não é ‘está verde’. É uma decisão com contexto: o que foi verificado, que riscos restam e qual uso estamos autorizando.

**Mostrar/fazer:** checklist da demonstração do laboratório.

**Perguntar:** Se RN02 falha, podemos demonstrar reserva como se estivesse íntegra?

**Compreensão esperada:** não; é risco crítico para o objetivo.

### 3. Operação e resposta a falhas

**Fala sugerida:**

> Em produção real existiriam monitoramento, rollback, dados persistentes e procedimentos operacionais. Nosso laboratório não comprova isso; vamos simular apenas o raciocínio.

**Mostrar/fazer:** falha crítica durante pré-release.

**Perguntar:** Que ação é segura no laboratório?

**Compreensão esperada:** interromper demonstração, registrar, corrigir e repetir; não alegar rollback de produção.

## 25–45 — Demonstração guiada — Executar checklist e tomar decisão de liberação

### Passo 1 — Revisar checklist

**Fazer:** Marque versão, casos críticos e limites.

**Fala sugerida:**

> Checklist não substitui julgamento; ele evita que esqueçamos condições necessárias para decidir.

**Checar com a turma:** Peça um critério que bloquearia a liberação.

### Passo 2 — Simular falha crítica

**Fazer:** Considere RN02 falhando.

**Fala sugerida:**

> Agora precisamos decidir antes de pensar em ‘como deixar verde’. O comportamento central não está confiável.

**Checar com a turma:** Peça decisão e impacto.

### Passo 3 — Explicar resposta e limite

**Fazer:** Registre interrupção/correção/reteste.

**Fala sugerida:**

> Reiniciar o programa local não é rollback de produção. Vamos nomear corretamente a simulação e dizer o que faltaria num ambiente real.

**Checar com a turma:** Pergunte o que seria necessário para um plano operacional real.

**Resultado de referência:** Liberar apenas a demonstração/escopo cujos casos críticos passaram. Falha em conflito deve interromper a liberação do escopo afetado. Laboratório não comprova rollback, persistência ou monitoramento de produção.

Peça previsão antes de revelar decisões ou resultados.

## 45–50 — Pausa

Informar horário de retorno e não inserir conteúdo obrigatório.

## 50–65 — Dinâmica — Liberar ou interromper

**Cenário:** A equipe está a dez minutos de uma demonstração e um teste crítico de conflito falha.

> O objetivo não é ser ‘o QA que bloqueia’. É tomar uma decisão explicável com base no risco e na evidência.

1. Identificar requisito/risco afetado.
2. Classificar impacto.
3. Decidir release/demonstração.
4. Registrar justificativa e próxima ação.
5. Indicar claramente o que não será demonstrado.

**Entrega:** decisão de release + mini plano de resposta

**Observar:** evidência citada; escopo afetado claro; sem mascarar falha; limite da simulação declarado.

## 65–77 — Exercício individual

> Escreva um gatilho de parada para falha de RN02 e uma resposta de quatro passos. Diferencie o que é possível no laboratório do que exigiria ambiente de produção real.

**Entrega:** gatilho + resposta

**Critérios:** gatilho observável; ação coerente; reteste previsto; limites reais declarados.

**Ajuda graduada:** use ‘se [evidência], então [interromper], registrar, corrigir e retestar’.

## 77–85 — Correção e intervenções

Peça que a pessoa explique sua decisão antes da resposta de referência.

**Se aparecer:** o aluno chama reinício de rollback

> Que versão e dados foram restaurados? Se isso não existe, descreva corretamente como reinício local.

**Se aparecer:** o aluno libera mesmo com RN02 falhando porque ‘é só demo’

> Se o objetivo da demo inclui reserva íntegra, o comportamento crítico precisa ser confiável ou explicitamente removido do escopo.

**Se aparecer:** o aluno escreve ‘não liberar’ sem explicar

> Qual requisito, evidência e impacto sustentam a decisão? Registre a razão.

### Perguntas de verificação

- **Deploy e release são sempre a mesma coisa?** — Não necessariamente. Deploy instala/coloca versão; release é decisão de disponibilização.
- **Reiniciar o laboratório é rollback?** — Não. É apenas reiniciar estado local; rollback real envolve versão, dados, infraestrutura e estratégia.
- **Uma falha crítica precisa bloquear todo o produto?** — Depende do escopo/impacto. Deve bloquear pelo menos o uso afetado quando a evidência torna a decisão insegura.

## 85–90 — Fechamento e tarefa

> Decisão profissional de release não é otimismo nem pessimismo: é escopo, evidência, risco e limite nomeados de forma clara.

1. Revisar o diagrama SDLC.
2. Concluir matriz de rastreabilidade.
3. Finalizar checklist de release.
4. Registrar plano de resposta a falha.
5. Entregar `m07-aula-04-revisao.md` e organizar a entrega do módulo.

**Entrega:** pacote final do Módulo 7

**Ponte:**

> No próximo módulo vocês deixam de praticar peças separadas e passam a montar um dossiê completo do Agenda Clara, do problema à apresentação.

## Pós-aula

- [ ] Disponibilizar gravação.
- [ ] Registrar dúvidas e lacunas recorrentes.
- [ ] Conferir se demonstração, prática e tarefa seguiram o roteiro.
- [ ] Atualizar roteiro e script juntos se alguma regra mudar.
