# Roteiro de Aula — Módulo 7, Aula 2

# Rastreabilidade e Análise de Impacto

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-07-aula-02-rastreabilidade-e-impacto.md).

## Objetivo da aula

Ensinar rastreabilidade como conexão verificável entre necessidade, regra, história, teste, defeito e versão, usando esses vínculos para avaliar impacto de mudanças.

Ao final, o aluno deverá conseguir:

- montar uma cadeia de rastreabilidade
- explicar por que rastreabilidade não é apenas link
- identificar artefatos afetados por mudança
- distinguir evidência atual de cobertura futura
- produzir análise de impacto simples

## Conteúdos e conceitos

### Rastreabilidade
- origem da necessidade
- vínculo entre artefatos
- possibilidade de conferir

### Análise de impacto
- mudança invalida premissas
- artefatos precisam revisão
- não reutilizar aprovação cegamente

### Versão e evidência
- resultado pertence a uma versão
- reteste precisa referência
- cobertura não se transfere automaticamente

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

- E-book do Módulo 7
- matriz de rastreabilidade
- artefatos Agenda Clara

## Exemplos planejados

### Exemplo 1
Cadeia RN03–US02–TC03–BUG01.

### Exemplo 2
Mudança para incluir H12 no catálogo.

### Exemplo 3
Nova regra de tamanho mínimo de nome.

## Demonstração planejada — Montar cadeia e analisar uma mudança

1. Ligar RN03 à história/critério correspondente.
2. Ligar ao TC03.
3. Ligar BUG01 à evidência da variante.
4. Identificar a versão usada no reteste.
5. Alterar uma premissa e listar impactos.

**Resultado pedagógico esperado:** o aluno consegue explicar não só a cadeia, mas o que precisa ser revisto quando algo muda.

## Dinâmica em grupo — Seguir a mudança

**Cenário:** A regra de catálogo muda para incluir H12 depois de histórias, testes e documentação já existirem.

1. Localizar artefatos que mencionam catálogo.
2. Classificar impacto: precisa mudar / precisa verificar / não afetado.
3. Atualizar uma linha da matriz.
4. Explicar qual evidência precisa ser refeita.

**Entrega esperada:** matriz de impacto

**Critérios:** dependências identificadas; impacto justificado; versão/evidência considerada; nenhuma aprovação antiga reaproveitada sem análise.

## Exercício individual

Com H12 entrando no catálogo, indique pelo menos uma regra, um caso, uma documentação ou exemplo e uma execução que precisam ser revistos. Justifique cada item.

**Entrega:** análise individual de impacto

**Critérios:** itens concretos; relação com mudança; justificativa; nova evidência proposta.

## Perguntas de verificação

- Rastreabilidade é apenas colocar links entre arquivos?
- Teste aprovado em versão anterior continua válido após qualquer mudança?
- Todos os artefatos sempre mudam quando uma regra muda?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Completar vínculos principais.
2. Adicionar versão às evidências.
3. Escolher uma mudança e registrar impacto.
4. Entregar `m07-aula-02-revisao.md`.

**Entrega:** matriz de rastreabilidade + análise de impacto

## Conexão com a trilha

A Aula 3 usa esses vínculos para antecipar perguntas e prevenir ambiguidades com Shift Left.

## Referências

- [E-book correspondente](../ebooks/modulo-07-ciclo-de-vida-do-software.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-07-aula-02-rastreabilidade-e-impacto.md)
