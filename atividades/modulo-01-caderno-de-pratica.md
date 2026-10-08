# Módulo 1 — Caderno de prática e avaliação

Este caderno complementa o [E-book existente](../ebooks/modulo-01-fundamentos.md) e suas quatro aulas. Ele define entregas verificáveis e recuperação. Nas tarefas, use dados fictícios e diferencie o que observou de sua hipótese sobre o funcionamento interno.

## Atividade 1 — Áreas, responsabilidades e evidências

**Contexto profissional:** escolher uma área de estudo exige entender atividades, não apenas nomes de cargos. **Cenário:** Agenda Clara precisa resolver conflitos de agenda. **Objetivo:** relacionar seis áreas a contribuições concretas.

1. Criar tabela com Desenvolvimento, QA, Produto, Dados, Infraestrutura e Gestão.
2. Para cada área, escrever uma responsabilidade e um artefato.
3. Relacionar duas áreas no tratamento de uma reserva duplicada.
4. Indicar um interesse pessoal e uma dúvida; interesse não vale como prova de domínio.
5. Comparar três descrições reais de vagas com link e data. Se não houver acesso, usar exemplos identificados como simulação.

**Entrega:** tabela de seis áreas, relação entre duas, mapa inicial e reflexão. **Critérios:** seis contribuições coerentes; artefatos concretos; fonte ou simulação identificada; distinção entre interesse e competência.

**Resposta de referência:**

| Área | Contribuição na Agenda Clara | Artefato |
|---|---|---|
| Desenvolvimento | Implementar regra de ocupação | Código |
| QA | Investigar duplicidade | Caso com entrada e esperado |
| Produto | Definir necessidade e prioridade | Requisito |
| Dados | Definir taxa de conflitos | Métrica com denominador |
| Infraestrutura | Discutir ambiente e observação | Plano de disponibilização |
| Gestão | Coordenar recorte e dependências | Plano de trabalho |

QA não garante sozinho qualidade; todos contribuem. “Banco de dados” é componente, não sinônimo de área de Dados. **Dica:** pergunte o que a pessoa entrega. **Variação difícil:** explicar uma empresa pequena onde a mesma pessoa reúne especialidades, sem concluir que as responsabilidades desaparecem.

## Atividade 2 — Do problema à entrega

**Contexto:** equipe precisa comunicar como uma ideia vira solução. **Cenário:** cliente não consegue cancelar reserva. **Objetivo:** mapear contribuições e feedback, sem colocar qualidade somente no fim.

1. Descrever problema e usuário.
2. Desenhar necessidade, critérios, construção, verificação, disponibilização e feedback.
3. Marcar participação de Produto, Dev e QA em mais de um momento.
4. Propor um critério de cancelamento e um resultado esperado.
5. Registrar uma pergunta que precisa ser esclarecida antes de construir.

**Entrega:** fluxo e tabela problema/critério/teste/pergunta. **Critérios:** fluxo com retorno; qualidade antecipada; comportamento observável; pergunta relevante.

**Resposta:** “Cancelamento de reserva ativa libera o horário” pode ser discutido por Produto, Dev e QA antes do código. Após implementação, executar reserva/cancelamento/consulta. Feedback de recepção retorna às decisões. Pergunta: quem pode cancelar? O curso não deve assumir controle de acesso que não foi definido.

**Dica:** critério não precisa explicar como o código será escrito. **Variação difícil:** incluir suporte e Dados no retorno de uma reclamação.

## Atividade 3 — Front-end, back-end, API e dados

**Contexto:** pessoas de diferentes áreas precisam conversar sobre comportamento e componentes. **Cenário:** uma interface futura da Agenda Clara solicita uma reserva. **Objetivo:** distinguir papéis sem tratar hipótese como observação de arquitetura real.

1. Desenhar usuário → interface → API → regra → armazenamento.
2. Explicar o papel de cada elemento em uma frase.
3. Marcar a interface e a API como propostas futuras; o simulador usa chamadas locais e memória.
4. Escrever uma entrada e uma resposta conceitual de reserva.
5. Registrar o que uma tela sozinha não permite concluir.

**Entrega:** diagrama e explicação dos componentes. **Critérios:** separar interface de regra; API de banco; hipótese de implementação; entrada/saída coerentes.

**Resposta:** interface recebe nome/horário; API seria contrato de comunicação; regra verifica disponibilidade; armazenamento mantém estado. No laboratório, não existe API HTTP; dicionário com status não é resposta HTTP. Observar uma mensagem não prova que não houve reserva indevida, nem revela qual banco o serviço usa.

**Dica:** a analogia do restaurante é ponto de partida, não arquitetura completa. **Variação difícil:** explicar efeito de reiniciar armazenamento em memória versus persistência.

## Atividade 4 — Pensamento computacional e mapa final

**Contexto:** investigar problema exige organizar hipóteses. **Cenário:** uma pessoa não consegue reservar H09. **Objetivo:** aplicar decomposição, padrões, abstração e algoritmo e concluir mapa mental.

1. Dividir consulta, entrada, validação, ocupação e confirmação.
2. Propor dois padrões possíveis, marcando-os como hipóteses.
3. Selecionar os dados mínimos: nome, horário, estado e resultado.
4. Escrever passos que diferenciem horário ocupado de nome inválido.
5. Concluir mapa com seis áreas, quatro conceitos técnicos, quatro pilares e três conexões explicadas.
6. Apresentar o mapa em três minutos; registrar interesse e próximo estudo.

**Entrega:** mapa e algoritmo de investigação. **Critérios:** conceitos corretos; conexões com exemplos; hipóteses identificadas; sequência executável em linguagem natural.

**Resposta:** decompor consulta e reserva; verificar se H09 está ocupado e se nome tem conteúdo; comparar retorno com regra; registrar estado. Não concluir “problema no banco” só porque a reserva falhou. Conexão do mapa: “Produto define RN03 → QA testa espaços → Dev implementa validação”.

**Dica:** não avaliar beleza acima de clareza. **Variação difícil:** propor uma pergunta que ajuda a distinguir falha de regra prevista.

## Entrega final, rubrica e recuperação

Organizar as quatro atividades e o mapa final. Identificar cada versão, o feedback e a revisão.

| Critério | 0 | 1 | 2 |
|---|---|---|---|
| Conceitos | Contradiz papéis ou componentes | Confusão parcial | Diferencia e explica |
| Completude | Falta entrega principal | Faltam itens | Cumpre enunciado |
| Evidência | Sem exemplo ou fonte | Exemplos insuficientes | Entradas, fontes ou hipóteses identificadas |
| Justificativa | Não conecta | Conexão vaga | Relaciona área, comportamento e carreira |

Parâmetro formativo: 6/8, sem zero em conceitos ou evidência. Professor registra um acerto e uma lacuna; aluno corrige e explica a mudança. Esta rubrica torna explícitos os critérios das tarefas anteriores, sem definir regra de certificação.

Para quem não conseguiu, começar por uma funcionalidade e duas áreas, depois ampliar. Para quem avançou, aplicar a variação difícil. O professor pede um exemplo novo na reapresentação para conferir aprendizagem, não apenas edição do arquivo.

