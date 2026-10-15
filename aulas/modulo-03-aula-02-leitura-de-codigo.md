# Roteiro de Aula — Módulo 3, Aula 2

# Leitura de Código e Comportamento

> **Papel deste documento:** definir o que será ensinado, praticado e avaliado.  
> A condução minuto a minuto, falas sugeridas, respostas esperadas e intervenções ficam no [script do professor](scripts/modulo-03-aula-02-leitura-de-codigo.md).

## Objetivo da aula

Ensinar o iniciante a ler código pelo comportamento, rastreando entradas, decisões e retornos sem exigir domínio completo da linguagem.

Ao final, o aluno deverá conseguir:

- localizar função/método de interesse
- rastrear uma chamada concreta
- identificar retorno antecipado e mudança de estado
- comparar a mesma lógica em Python, JavaScript e TypeScript de forma introdutória
- distinguir lógica de sintaxe

## Conteúdos e conceitos

### Ler pelo contrato
- nome da operação
- entrada
- resultado esperado

### Estado e retorno
- condição pode encerrar cedo
- retorno comunica resultado
- estado só muda em caminhos específicos

### Mesma lógica, outra sintaxe
- Python como base didática
- JavaScript como comparação
- TypeScript adiciona tipos explícitos

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

- [E-book do Módulo 3](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)
- laboratório Agenda Clara
- editor com destaque de sintaxe

## Exemplos planejados

### Exemplo 1
Rastrear Ana/H09 e Bruno/H09.

### Exemplo 2
Localizar retorno de horário inválido.

### Exemplo 3
Comparar `validar_nome` em Python, JavaScript e TypeScript.

## Demonstração planejada — Rastrear duas chamadas e comparar uma lógica entre linguagens

1. Localizar `reservar`.
2. Rastrear Ana/H09 em agenda vazia.
3. Rastrear Bruno/H09 na mesma agenda.
4. Localizar o retorno que impede duplicidade.
5. Mostrar `validar_nome` equivalente em Python, JS e TS sem aprofundar sintaxe.

**Resultado pedagógico esperado:** o aluno lê comportamento e percebe que lógica pode ser transferida entre linguagens.

## Dinâmica em grupo — Leia pelo comportamento

**Cenário:** Cada dupla recebe uma entrada diferente do laboratório e precisa explicar o caminho sem comentar o arquivo inteiro.

1. Identificar entrada.
2. Marcar as condições relevantes.
3. Registrar retorno e estado final.
4. Trocar com outra dupla para revisão.

**Entrega esperada:** trilha de execução anotada

**Critérios:** caminho coerente; retorno identificado; estado final correto; explicação focada.

## Exercício individual

Rastreie nome válido com H12 em agenda vazia. Indique onde a operação para, qual retorno é produzido e se o estado muda. Depois escreva em uma frase o que seria igual se essa regra estivesse em JavaScript.

**Entrega:** rastreamento + frase de transferência

**Critérios:** retorno correto; estado correto; linha/condição decisiva identificada; lógica separada da sintaxe.

## Perguntas de verificação

- Preciso entender todo o arquivo para explicar uma função?
- Depois de um `return`, o restante daquele caminho executa?
- Ao passar de Python para JS/TS, a lógica precisa ser reaprendida do zero?

> As respostas esperadas e intervenções ficam exclusivamente no script do professor.

## Tarefa para casa

1. Rastrear outra entrada do laboratório.
2. Registrar retorno e estado.
3. Escolher uma função simples de lógica do Módulo 2 e observar uma versão equivalente em JS ou TS, sem obrigação de programar um projeto.
4. Entregar `m03-aula-02-revisao.md`.

**Entrega:** rastreamento revisado + comparação curta

## Conexão com a trilha

A Aula 3 introduz Git para registrar mudanças e permitir que a evolução do projeto seja explicada.

## Referências

- [E-book correspondente](../ebooks/modulo-03-introducao-ao-desenvolvimento-de-software.md)
- [Laboratório Agenda Clara](../portfolio/agenda-clara/README.md)
- [Script do professor](scripts/modulo-03-aula-02-leitura-de-codigo.md)
