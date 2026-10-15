# Auditoria Pedagógica — Roteiros × Scripts

**DTEM Treinamentos · revisão estrutural de outubro de 2026**

## Objetivo

Garantir que cada Script do Professor seja a transformação operacional do Roteiro correspondente, e não um texto genérico reutilizado com nomes diferentes.

A auditoria verificou os **34 pares** da formação:

- 32 aulas nos oito módulos;
- 2 aulas do bônus de carreira.

## Critérios avaliados

Para cada par foram comparados:

1. tema;
2. objetivo observável;
3. conceitos;
4. exemplo/demonstração central;
5. dinâmica em grupo;
6. exercício individual;
7. perguntas;
8. critérios de avaliação;
9. tarefa;
10. entrega;
11. pré-requisitos;
12. ponte para a aula seguinte;
13. adequação ao nível do aluno;
14. distinção entre material do aluno e material interno do professor.

## Problema encontrado

O padrão anterior usava uma estrutura pedagógica comum, mas em várias aulas a camada operacional havia se tornado excessivamente genérica.

O caso mais evidente era **Módulo 1 — Aula 1**:

- o Roteiro ensinava mercado tech e áreas de TI;
- o Script abria com reserva duplicada, caso de teste e linguagem de evidência;
- conceitos que deveriam ser aprendidos durante a aula apareciam como pré-requisito;
- a dinâmica do Roteiro (“Monte o time tech”) tinha sido substituída por análise do Agenda Clara.

Isso confirmou a necessidade de auditar a trilha inteira, não apenas corrigir um arquivo.

## Estratégia aplicada

Todos os 34 pares foram reestruturados para que:

- o Roteiro declare o contrato pedagógico;
- o Script repita esse contrato em “Alinhamento obrigatório”;
- demonstração, dinâmica, exercício e tarefa sejam equivalentes;
- falas e gabaritos existam apenas no Script;
- cada aula tenha prática própria do tema;
- exemplos do Agenda Clara cresçam em complexidade conforme a trilha;
- o projeto final reutilize conhecimentos anteriores sem fingir experiência profissional.

## Resultado por encontro

| Encontro | Foco após auditoria | Status |
|---|---|---|
| M1 A1 | Mercado, seis áreas, “Monte o time tech”, mapa inicial | ✅ Alinhado |
| M1 A2 | Fluxo de empresa tech da necessidade ao feedback | ✅ Alinhado |
| M1 A3 | Front, back, API e banco por cadastro de aluno | ✅ Alinhado |
| M1 A4 | Quatro pilares + mapa mental final | ✅ Alinhado |
| M2 A1 | Algoritmo e rastreamento antes do código | ✅ Alinhado |
| M2 A2 | Variáveis, tipos e decisões com Python introdutório | ✅ Alinhado |
| M2 A3 | Listas, for, while e condição de parada | ✅ Alinhado |
| M2 A4 | Funções, return e depuração orientada por hipótese | ✅ Alinhado |
| M3 A1 | Componentes reais do laboratório e limites | ✅ Alinhado |
| M3 A2 | Leitura de código + comparação controlada Python/JS/TS | ✅ Alinhado |
| M3 A3 | Git local, staging, diff e commits por intenção | ✅ Alinhado |
| M3 A4 | GitHub, branch, README e revisão | ✅ Alinhado |
| M4 A1 | Qualidade, risco e plano de testes | ✅ Alinhado |
| M4 A2 | Casos funcionais reproduzíveis | ✅ Alinhado |
| M4 A3 | Exploração e bug report | ✅ Alinhado |
| M4 A4 | Reteste, regressão e ponte para automação JS/TS | ✅ Alinhado |
| M5 A1 | Problema, output/outcome, hipótese e PO | ✅ Alinhado |
| M5 A2 | Descoberta e classificação de requisitos | ✅ Alinhado |
| M5 A3 | User Stories e critérios verificáveis | ✅ Alinhado |
| M5 A4 | Backlog, prioridade, dependência e trade-off | ✅ Alinhado |
| M6 A1 | Restrições, capacidade e replanejamento | ✅ Alinhado |
| M6 A2 | Scrum, Planning e Daily orientados à meta | ✅ Alinhado |
| M6 A3 | Review, Retro e Definition of Done | ✅ Alinhado |
| M6 A4 | Kanban, WIP, fluxo e comunicação | ✅ Alinhado |
| M7 A1 | SDLC integrado e feedback | ✅ Alinhado |
| M7 A2 | Rastreabilidade e impacto | ✅ Alinhado |
| M7 A3 | Shift Left e prevenção | ✅ Alinhado |
| M7 A4 | Release, operação e resposta a falha | ✅ Alinhado |
| M8 A1 | Kickoff, escopo e requisitos do projeto final | ✅ Alinhado |
| M8 A2 | Sprint simulada, execução e bloqueio | ✅ Alinhado |
| M8 A3 | Evidência, BUG01 executável e BUG02 fornecido | ✅ Alinhado |
| M8 A4 | Dossiê, release e pitch honesto | ✅ Alinhado |
| Bônus A1 | Vaga → evidência → currículo/LinkedIn/portfólio | ✅ Alinhado |
| Bônus A2 | Entrevista com evidência + plano de evolução | ✅ Alinhado |

## Decisões pedagógicas preservadas

### Linguagens

- Python permanece principal no Módulo 2.
- JavaScript entra como comparação no Módulo 3.
- TypeScript aparece como evolução da comparação e contexto de automação.
- O aluno não recebe três linguagens concorrentes no início.

### Agenda Clara

A complexidade do caso é progressiva:

- Módulo 1: exemplos cotidianos e visão geral;
- Módulo 2: regras simples para lógica;
- Módulo 3: leitura de sistema/código e versionamento;
- Módulo 4: QA;
- Módulos 5–7: Produto, Gestão e SDLC;
- Módulo 8: integração completa.

### Simulação versus experiência real

Todos os materiais devem distinguir:

- execução real no laboratório;
- simulação educacional;
- hipótese;
- incidente fornecido;
- experiência profissional.

Em especial, BUG02 do projeto final não pode ser marcado como reproduzido na versão disponível.

## Regra para futuras alterações

Uma mudança em objetivo, demonstração, atividade, exercício, critério, tarefa ou entrega exige revisão **do Roteiro e do Script no mesmo PR**.

Alterar apenas as falas ou uma intervenção interna pode ocorrer somente no Script, desde que o contrato pedagógico do Roteiro permaneça intacto.
