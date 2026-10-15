# Roteiro de Aula — Módulo 8, Aula 3

# Testes, Defeitos e Evidências

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-08-aula-03-testes-e-defeitos.md).

## Objetivo da aula

Executar e organizar as evidências do projeto final, distinguindo teste executado, BUG01 reproduzível e BUG02 fornecido como incidente fictício que não deve ser apresentado como execução.

Ao final, o aluno deverá conseguir:

- executar os casos prioritários com estado controlado
- registrar versão e resultado
- reproduzir BUG01
- analisar BUG02 sem fingir reprodução
- emitir parecer limitado às evidências

## Conteúdos e conceitos

### Evidência de execução
- versão
- entrada/estado
- esperado/observado
- método de execução

### BUG01 versus BUG02
- BUG01 executável na variante
- BUG02 é registro fictício fornecido
- não inventar execução

### Parecer proporcional
- evidência sustenta decisão
- pendência aparece
- limites preservados

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

- E-book do Módulo 8
- oito casos do kit
- referência e variante
- registros BUG01/BUG02

## Exemplos planejados

### Exemplo 1
TC03/BUG01.

### Exemplo 2
BUG02 de cancelamento em versão fictícia.

### Exemplo 3
Sequência autoral de rejeição.

## Demonstração planejada — Executar BUG01 e analisar BUG02 corretamente

1. Preparar estado e versão.
2. Executar um caso de referência.
3. Reproduzir BUG01 na variante.
4. Ler BUG02 como documento fornecido.
5. Montar plano de confirmação de BUG02 sem marcar como executado.

**Resultado pedagógico esperado:** o aluno distingue fontes e força da evidência.

## Dinâmica em grupo — Provar comportamento

**Cenário:** Cada dupla recebe um caso executável e um registro fornecido que precisa ser analisado.

1. Executar o caso com versão/estado registrados.
2. Separar observado de hipótese.
3. Analisar o registro fornecido.
4. Escrever o que seria necessário para reproduzi-lo.
5. Trocar evidências com outra dupla para conferência.

**Entrega esperada:** registro de execução + plano de investigação

**Critérios:** fonte da evidência clara; nenhuma execução inventada; estado/versão presentes; plano de confirmação reproduzível.

## Exercício individual

Crie uma sequência nova de rejeição, execute na versão disponível e registre entrada, estado, esperado, observado e resultado. Depois escreva uma frase dizendo o que essa evidência permite — e não permite — concluir.

**Entrega:** caso autoral executado + conclusão limitada

**Critérios:** execução verificável; esperado independente; limite da conclusão; versão identificada.

## Perguntas de verificação

- Posso dizer que reproduzi BUG02?
- Uma evidência de um caso prova todo o sistema?
- Qual diferença entre ‘não encontrei falha’ e ‘não existe falha’?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Executar/conferir os oito casos previstos.
2. Organizar BUG01 com reteste.
3. Manter BUG02 como incidente fornecido com plano de confirmação.
4. Atualizar matriz de rastreabilidade.
5. Entregar `m08-aula-03-revisao.md`.

**Entrega:** bloco de qualidade do dossiê

## Conexão com a trilha

A Aula 4 fecha o projeto com decisão de release, dossiê, apresentação e limites do portfólio.

## Referências

- [E-book correspondente](../ebooks/modulo-08-projeto-final-hands-on.md)
- [Caso Agenda Clara](../atividades/caso-agenda-clara.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-08-aula-03-testes-e-defeitos.md)
