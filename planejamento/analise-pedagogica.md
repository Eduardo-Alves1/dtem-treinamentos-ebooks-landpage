# Análise pedagógica — DTEM Treinamentos

**Data:** 8 de outubro de 2026. **Escopo:** ementa publicada, ementa local, página HTML do projeto, E-book e quatro aulas existentes do Módulo 1.

## Fontes e limite da análise

A [ementa pública](https://dtemtreinamentos.com.br/ementa/) foi consultada por requisição HTTP pelo terminal, com resposta 200, após falha da ferramenta de navegação. A página confirma os oito módulos, o foco inicial em QA/Produto, os entregáveis de portfólio e o bônus de carreira. Os títulos e resumos dos módulos correspondem à [cópia HTML local](../landpage/ementa/index.html). A [ementa.md](../ementa.md) detalha tópicos e entregas usados na criação. A página publicada não define a carga horária total nem a forma de avaliação; essas decisões são propostas pedagógicas deste material.

## O que a proposta oferece

A formação apresenta oito módulos: Fundamentos, Lógica, Desenvolvimento, QA, Produto, Gestão, SDLC e Projeto Final, com bônus de carreira. O posicionamento mais coerente é **formação inicial com experimentação de papéis e portfólio**, com aprofundamento introdutório em QA, Produto e organização do trabalho. As evidências de aprendizagem devem sustentar essa promessa. Concluir os módulos não equivale a dominar todas as profissões apresentadas.

## Diagnóstico dos materiais existentes

| Material | Evidência encontrada | Ajuste aplicado nesta revisão |
|---|---|---|
| E-book do Módulo 1 | Conceito, explicações, exemplos, exercícios e conexões com carreira por tópico | Acrescentar contrato de aprendizagem, critérios verificáveis e caso contínuo |
| Aula 1 — Mercado e áreas | Comparação de papéis, leitura de vagas e início do mapa mental | Separar interesse pessoal de evidência de compreensão; adicionar exemplo avaliado |
| Aula 2 — Empresa tech | Fluxo de trabalho, papéis, dinâmica e critérios de cadastro | Explicitar qualidade compartilhada e participação de QA desde requisitos |
| Aula 3 — Front/back/API/banco | Exemplos técnicos, fluxo e cenários de cadastro | Diferenciar observação de interface de hipótese sobre arquitetura |
| Aula 4 — Pensamento computacional | Quatro pilares, investigação e entrega do mapa | Acrescentar critérios de conclusão e procedimento de recuperação |

Os roteiros existentes são utilizáveis e não precisam ser descartados. Entretanto, tarefas como “descrever”, “pesquisar” e “atualizar o mapa” precisam de quantidade mínima, evidência e retorno do professor. O diagrama da Aula 2 coloca QA depois de Desenvolvimento; isso serve como simplificação de sequência, mas precisa mostrar prevenção de defeitos antes da implementação. Afirmações sobre vagas devem ser tratadas como vocabulário ilustrativo ou pesquisa feita pelo aluno, sem simular uma pesquisa atual de mercado.

## Decisões de desenho instrucional

1. Manter a ordem dos oito módulos da ementa. Produto antecede a execução integrada no projeto; em QA, usar requisitos fornecidos para não depender de conteúdo ainda não estudado.
2. Usar o caso fictício Agenda Clara em todos os módulos novos. Seus dados e regras ficam no [caderno do caso](../atividades/caso-agenda-clara.md).
3. Separar conteúdo para estudo, roteiro de condução e evidência de portfólio. Cada aula nova indica capítulo, objetivo observável, demonstração, prática e correção.
4. Seguir o formato definido para a mentoria: quatro encontros de até 90 minutos por módulo, incluindo pausa de 5 minutos. O script seleciona a prática principal ao vivo; as atividades completas são concluídas depois. São 34 encontros com o bônus; apresentações e recuperação podem exigir encontros adicionais.
5. Dedicar prática em dupla e prática individual em todas as aulas. Primeiro prever uma resposta, depois observar, explicar e transferir para uma situação nova.
6. Fornecer rubrica de 0 a 2 por critério, respostas de referência e nova tentativa. Avaliar o raciocínio e a evidência, sem privilegiar quem já conhece ferramentas.
7. Permitir papel e arquivos Markdown quando não houver conta Jira/Azure DevOps. O objetivo é compreender o fluxo; demonstrações na ferramenta devem usar documentação oficial vigente.
8. Entregar projeto viável sem desenvolvimento web obrigatório. O simulador local permite execução de testes; o aluno distingue implementação em Python, simulação de interface e deploy simulado.

## Ajustes de posicionamento recomendados

Apresentar QA e Produto como possibilidades de atuação exploradas pelo curso. Evitar prometer que PO é sempre uma primeira vaga ou que aprender uma ferramenta garante empregabilidade. Na ementa local, substituir a formulação “LinkedIn (ATS)” por “LinkedIn, currículo e leitura de vagas”: ATS é um sistema de gestão de candidaturas, distinto do perfil público de LinkedIn. O bônus criado já faz essa distinção. Manter currículo e entrevistas no bônus; não acrescentar um nono módulo obrigatório.

No site, esclarecer carga horária, modalidade, pré-requisitos, acesso aos materiais e forma de feedback quando essas condições forem definidas. Nenhuma alteração no site foi feita nesta etapa.

## Avaliação e recuperação

Cada entrega usa quatro critérios com notas 0, 1 ou 2: correção conceitual, completude, evidência verificável e justificativa. Total de 8 pontos. Atingir 6 pontos e não ter zero em correção conceitual ou evidência é o parâmetro formativo proposto. Não é regra comercial de certificação.

O professor devolve um acerto, uma lacuna e uma ação objetiva. O aluno corrige o artefato, registra o que mudou e apresenta novamente. Se não houver computador, entrega o raciocínio no papel e realiza a parte de execução posteriormente, com acesso assistido; a evidência de execução continua necessária onde prevista.

## Referências de apoio

As escolhas didáticas e os casos são autorais. Para aprofundamento técnico, consultar [Python](https://docs.python.org/3/tutorial/), [Git](https://git-scm.com/docs/gittutorial), [Scrum Guide](https://scrumguides.org/scrum-guide.html) e [ISTQB CTFL](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/). Exemplos de empresas nos materiais são ilustrações de práticas, sem atribuição de processos internos a marcas reais.
