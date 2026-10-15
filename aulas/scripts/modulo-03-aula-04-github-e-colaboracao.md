# Script do Professor — GitHub, Revisão e Publicação

**DTEM Treinamentos · encontro ao vivo de até 90 minutos.**

> **Papel deste documento:** orientar a condução da aula. O conteúdo e as atividades abaixo devem permanecer coerentes com o roteiro; o script não cria uma aula paralela.

**Roteiro:** [Módulo 3, Aula 4](../modulo-03-aula-04-github-e-colaboracao.md)  
**Material do aluno:** [E-book correspondente](../../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)  
**Laboratório:** [Agenda Clara](../../portfolio/agenda-clara/README.md)  

## Alinhamento obrigatório

- **Objetivo:** Publicar o primeiro projeto no GitHub e compreender como branch, proposta de mudança e revisão apoiam colaboração.
- **Demonstração central:** Publicar e revisar uma melhoria de documentação.
- **Prática em grupo:** Revisão de README.
- **Exercício individual:** publicar/verificar projeto e descrever uma proposta.
- **Tarefa:** finalizar publicação e revisar README.

Não substituir esses elementos por um exemplo genérico sem revisar também o roteiro.

## Antes da aula

- [ ] Confirmar conta GitHub e autenticação sem expor tokens.
- [ ] Preparar repositório de demonstração descartável.
- [ ] Testar fluxo de branch e push.
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

> Um colega recebeu o link do seu projeto. Ele consegue descobrir o que é, como executar e por que uma mudança foi feita? Hoje vamos transformar um repositório em algo colaborativo.

**Pergunta diagnóstica:** Alterar o arquivo no computador atualiza o GitHub automaticamente?

Dê cerca de dois minutos para respostas curtas. Escute pelo menos duas respostas antes de completar.

**Resposta de referência para o professor:** Não. Mudança precisa ser registrada em commit e enviada ao remoto.

**Transição:**

> Vamos ligar o histórico local que já conhecemos a um remoto e depois isolar uma melhoria para revisão.

## 08–25 — Conceitos e exemplos

### 1. Local e remoto

**Fala sugerida:**

> O repositório local existe no seu computador. GitHub pode hospedar uma cópia remota para compartilhamento e colaboração.

**Mostrar/fazer:** `git remote -v` e página do repositório.

**Perguntar:** Alterar um arquivo local muda o GitHub imediatamente?

**Compreensão esperada:** não; é preciso commit e envio/sincronização.

### 2. Branch e proposta

**Fala sugerida:**

> Branch permite desenvolver uma mudança sem alterar imediatamente a linha principal. Uma proposta de revisão explica problema, mudança e verificação.

**Mostrar/fazer:** fluxo main → branch → PR → revisão.

**Perguntar:** Por que não trabalhar sempre direto na main?

**Compreensão esperada:** para isolar mudanças, revisar e reduzir risco.

### 3. README e acessibilidade

**Fala sugerida:**

> Um link não é portfólio suficiente se ninguém entende o projeto. README precisa explicar o que é, como executar e o que não está implementado.

**Mostrar/fazer:** README do laboratório.

**Perguntar:** Uma pessoa que não assistiu à aula consegue executar?

**Compreensão esperada:** deve conseguir com instruções claras e acesso.

Evite ler o E-book. Use-o como base e mantenha a explicação oral no recorte previsto pelo roteiro.

## 25–45 — Demonstração guiada — Publicar e revisar uma melhoria de documentação

### Passo 1 — Conferir remoto

**Fazer:** Mostre `git remote -v` e página vazia/atual.

**Fala sugerida:**

> Antes de enviar, precisamos saber para onde estamos enviando. Credenciais e URL fazem parte da segurança do processo.

**Checar com a turma:** Pergunte o que fazer se a URL remota estiver errada.

### Passo 2 — Enviar e verificar

**Fazer:** Faça push normal e confira no GitHub.

**Fala sugerida:**

> Não basta comando retornar sem erro. Vamos verificar se o histórico que esperamos realmente apareceu no remoto.

**Checar com a turma:** Peça ao aluno para localizar commits e README.

### Passo 3 — Criar proposta revisável

**Fazer:** Use branch e alteração de README.

**Fala sugerida:**

> Uma boa proposta explica o problema, o que mudou e como confirmar. Isso é colaboração, não apenas ‘mandar código’.

**Checar com a turma:** Peça uma frase de problema e uma de verificação.

**Resultado de referência:** O projeto remoto deve conter histórico acessível, README coerente e uma mudança isolada/revisável. Repositório privado exige acesso apropriado ao avaliador.

Peça previsão antes de executar ou revelar a resposta. Depois compare previsão, evidência e explicação.

## 45–50 — Pausa

Informar o horário de retorno. Não usar a pausa para conteúdo obrigatório.

## 50–65 — Dinâmica — Revisão de README

**Cenário:** Uma pessoa publica instruções que funcionam apenas se o usuário já souber em qual pasta executar.

**Orientação para a turma:**

> Revisar não é reescrever o trabalho do colega. É apontar se a proposta está clara, verificável e segura.

1. Identificar o problema de documentação.
2. Propor mudança em branch.
3. Escrever descrição com problema, mudança e verificação.
4. Outra dupla revisa sem editar diretamente.

**Tempo sugerido:** 2 min organização, 8 min produção, 3 min revisão entre pares e 2 min compartilhamento.

**Entrega esperada:** proposta de mudança revisável

**O professor observa:** problema claro; mudança focada; verificação possível; limites honestos.

## 65–77 — Exercício individual

**Enunciado para falar à turma:**

> Verifique se outra pessoa consegue entender e executar seu projeto. Registre a URL ou pendência de acesso e escreva uma descrição curta de uma melhoria: problema, mudança e como verificar.

**Entrega:** link/verificação do repositório + descrição de proposta

**Critérios:** acesso conferido; README suficiente; proposta clara; sem inventar execução.

**Se houver dificuldade:** se publicação estiver bloqueada, documente o bloqueio e conclua a parte local; não use força para ‘resolver’ histórico sem entender.

## 77–85 — Correção, intervenções e dúvidas

Peça primeiro que o aluno explique o caminho usado. Só depois mostre referência ou correção.

**Se aparecer:** o aluno pensa que push é backup automático de qualquer arquivo

> Somente commits enviados chegam ao remoto. Arquivos não rastreados ou mudanças sem commit não aparecem.

**Se aparecer:** o aluno sugere `--force` para qualquer rejeição

> Pare e entenda por que o histórico divergiu. Forçar pode sobrescrever trabalho; não é solução padrão.

**Se aparecer:** o aluno considera link privado inacessível como evidência suficiente

> Quem avalia consegue abrir? A evidência precisa ser acessível ao público definido.

### Perguntas de verificação

- **Git e GitHub são a mesma coisa?** — Não. Git é versionamento; GitHub é uma plataforma de hospedagem/colaboração.
- **O que uma boa descrição de PR precisa explicar?** — Problema/contexto, mudança e forma de verificar, além de riscos quando relevantes.
- **Por que README faz parte do projeto?** — Porque permite compreender propósito, execução, limites e evidências sem depender do autor.

## 85–90 — Fechamento e tarefa

**Fala de fechamento:**

> Publicar é só o começo. Um projeto profissional precisa ser compreensível, verificável e seguro para outras pessoas colaborarem.

**Tarefa para casa:**

1. Conferir acesso ao repositório.
2. Revisar instruções do README.
3. Registrar uma melhoria em branch/PR ou simulação documentada.
4. Entregar `m03-aula-04-revisao.md` e organizar a entrega do módulo.

**Entrega:** repositório verificável + revisão documentada

**Ponte para a próxima aula:**

> No próximo módulo vamos olhar para esse software com a lente de qualidade: o que pode dar errado, como priorizar testes e como comunicar defeitos.

## Checklist pós-aula

- [ ] Disponibilizar a gravação.
- [ ] Registrar dúvidas que precisam ser retomadas.
- [ ] Conferir se atividade, demonstração e tarefa foram as mesmas do roteiro.
- [ ] Anotar ajustes de tempo para a próxima turma.
- [ ] Se uma regra ou resposta de referência mudar, atualizar roteiro e script juntos.
