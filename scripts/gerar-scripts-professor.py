"""Gera scripts de falas autorais e adapta roteiros DTEM ao encontro de 90 minutos."""
from pathlib import Path
import json
import os
import re

ROOT = Path(__file__).resolve().parents[1]
KEEP = "m02a01"
SCHEDULE = """| Intervalo | Etapa | Minutos |
|---|---|---:|
| 00–08 | Abertura e diagnóstico | 8 |
| 08–25 | Conceitos e exemplos | 17 |
| 25–45 | Demonstração guiada | 20 |
| 45–50 | Pausa | 5 |
| 50–65 | Dinâmica em dupla ou grupo | 15 |
| 65–77 | Exercício individual | 12 |
| 77–85 | Correção e dúvidas | 8 |
| 85–90 | Fechamento e tarefa | 5 |
| Total | | 90 |
"""
SHORT_TABLE = """| Etapa | Minutos |
|---|---:|
| Abertura e diagnóstico | 8 |
| Conceitos e exemplos | 17 |
| Demonstração guiada | 20 |
| Pausa | 5 |
| Dinâmica em dupla ou grupo | 15 |
| Exercício individual | 12 |
| Correção e dúvidas | 8 |
| Fechamento e orientação da tarefa | 5 |
| Total | 90 |
"""
records = {}
for path in sorted((ROOT / "scripts/falas").glob("*.json")):
    for record in json.loads(path.read_text(encoding="utf-8")):
        if record["id"] in records:
            raise ValueError("Registro duplicado: " + record["id"])
        records[record["id"]] = record

def rel(source, target):
    return os.path.relpath(target, source.parent).replace(os.sep, "/")

def quote(text):
    return "\n".join("> " + line for line in text.splitlines())

def safe_write(path, content):
    if ROOT not in path.resolve().parents:
        raise ValueError("Destino fora do projeto")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")

def title_of(text):
    match = re.search(r"\*\*Tema:\*\* ([^\n]+)", text)
    if match:
        return match.group(1).split(". **Objetivo")[0].rstrip(".")
    headings = re.findall(r"^# (.+)$", text, re.M)
    return next(h for h in headings if "ROTEIRO" not in h)

def render(record, source, target, title, ebook):
    group_time = {
        "b02": "5 minutos para a primeira entrevista; 5 para trocar papéis; 3 para feedback; 2 para registrar a melhoria.",
        "m08a04": "2 minutos para conferir um vínculo; 10 para até dois pitches de 5 minutos; 3 para feedback. As demais apresentações são entregas pós-aula ou exigem agenda adicional.",
    }.get(record["id"], "2 minutos para ler e organizar; 5 para produzir; 5 para trocar revisão; 3 para compartilhar.")
    theory = []
    for number, (label, speech) in enumerate(record["talk"], 1):
        theory.append(f"### Explicação {number} — {label}\n\n**Fala sugerida:**\n\n{quote(speech)}\n\n"
                      "**Ação:** escrever uma palavra-chave e pedir um exemplo com palavras do aluno. "
                      "Se houver dúvida, pedir a entrada, regra ou situação concreta que sustenta a resposta.")
    demo = []
    for number, (action, speech) in enumerate(record["demo"], 1):
        demo.append(f"### Passo {number} — {action}\n\n**Fala durante a demonstração:**\n\n{quote(speech)}\n\n"
                    "**Ação:** mostrar o registro correspondente antes de avançar; "
                    "pedir uma previsão e conferir a resposta com a evidência.")
    corrections = "\n\n".join(
        f"**Se o aluno {error[0].lower()}:**\n\n{quote(error[1])}" for error in record["interventions"])
    steps = "\n".join(f"{i+1}. {step}" for i, step in enumerate(record["group"]))
    home_name = source.stem + "-revisao.md"
    source_link = rel(target, source)
    ebook_link = rel(target, ebook)
    case_link = rel(target, ROOT / "atividades/caso-agenda-clara.md")
    rules_link = rel(target, ROOT / "planejamento/analise-pedagogica.md")
    return f"""# Script do professor — {title}

**DTEM Treinamentos · encontro ao vivo de até 90 minutos, gravado para revisão.**

Este documento contém falas e ações de condução. Adaptar a linguagem ao próprio estilo, preservando conceitos,
exemplos e critérios. Os intervalos incluem escrita, espera, interação e prática; não são 90 minutos de leitura.
Não depende de vídeos prévios. O aluno pode consultar o E-book e rever a gravação depois.

**Roteiro:** [planejamento da aula]({source_link}).  
**Material de estudo:** [E-book correspondente]({ebook_link}).  
**Caso:** [Agenda Clara]({case_link}), empresa e dados fictícios.

## Objetivo e materiais

**Objetivo observável:** {record["goal"]}.  
**Materiais:** {record["materials"]}.

Antes do encontro, preparar o exemplo e conferir os recursos necessários. Em tarefas de ferramenta, preparar
conta e ambiente com antecedência. Se a execução estiver indisponível, percorrer manualmente e declarar o método;
publicação ou execução exigidas pela entrega devem ser concluídas depois com apoio. Não inventar evidência.

## Agenda de condução

{SCHEDULE}
O roteiro original contém o caderno completo de atividades. Nesta versão, os enunciados de grupo e individual
abaixo definem o recorte do encontro. A tarefa de casa conclui os itens restantes. Se precisar reduzir extensão,
preservar demonstração, tentativa individual, feedback e orientação da entrega.

## 00–08 — Abertura e diagnóstico

**Mostrar:** título da aula e objetivo. **Fala de abertura:**

{quote(record["opening"])}

**Condução:** dar dois minutos para uma previsão individual no chat ou caderno. Colher duas respostas,
sem exigir fala de todos. Esperar aproximadamente 30 segundos antes de completar a resposta.
Não confundir silêncio inicial com falta de capacidade; oferecer a situação concreta novamente.

**Pergunta de diagnóstico:** “{record["check"][0]}”

**Referência para o professor:** {record["check"][1]}

**Transição para a explicação:**

> Vamos transformar essa primeira resposta em um raciocínio que outra pessoa consiga conferir.
> A cada exemplo, anotem a decisão e a informação que a sustenta.

## 08–25 — Explicação teórica e exemplos

Dividir os 17 minutos entre as três explicações, a escrita e duas perguntas breves.
Usar as falas como apoio, sem acrescentar uma exposição inteira do E-book.

{chr(10).join(theory)}

**Mostrar no quadro:** {record["visual"]}.

**Checagem de compreensão:** “{record["check"][0]}”  
**Resposta esperada:** {record["check"][1]}

**Transição:**

> Agora vou percorrer um exemplo pensando em voz alta. Antes de mostrar o resultado,
> vou pedir uma previsão. Observem onde uma regra ou evidência muda a decisão.

## 25–45 — Demonstração guiada

**Preparação:** abrir os dados, documento, código ou cartões indicados. Reservar aproximadamente cinco minutos
por passo e os minutos finais para uma previsão e uma dúvida. Em comandos, executar uma operação de cada vez
e conferir estado. Não substituir falha de ambiente por uma afirmação de execução bem-sucedida.

{chr(10).join(demo)}

**Pergunta após a demonstração:** “Qual decisão vocês conseguem explicar sem copiar a frase que usei?”

**Referência:** a resposta precisa relacionar situação, decisão e fundamento.
As falas de cada passo indicam o comportamento ou a interpretação que deve ser conferido.

**Transição:**

> Na prática, vocês vão alternar quem conduz e quem revisa. O objetivo é produzir algo
> que o colega consiga conferir, e não somente repetir minha demonstração.

## 45–50 — Pausa

Deixar horário de retorno visível e não apresentar conteúdo obrigatório durante os cinco minutos.
Na gravação, indicar o ponto em que a atividade seguinte começa.

## 50–65 — Dinâmica em dupla ou grupo

**Nome:** Revisão com explicação — {title}.  
**Contexto profissional:** uma equipe precisa revisar seu trabalho antes de avançar.
**Objetivo:** aplicar os conceitos e produzir um registro conferível no recorte da aula.

**Fala de orientação:**

> Uma pessoa começa conduzindo e a outra confere as decisões. Na metade, troquem funções.
> Registrem o que fizeram e qual informação justifica o resultado.
> Se discordarem, expliquem a diferença usando regra ou evidência, em vez de escolher pela maioria.

**Enunciado e passo a passo:**

{steps}

**Tempo:** {group_time}
Selecionar duas duplas para falar e recolher as demais por escrito. Em aulas de entrevista ou apresentação,
usar o mesmo tempo para a primeira participação, troca e feedback.

**Entrega esperada:** registro da atividade com contexto, decisão, fundamento e uma revisão.
**Critérios:** cumprir as etapas, preservar as regras e permitir que o colega confira.
**Referência de correção:** usar os exemplos da demonstração e verificar o que mudou no novo caso,
sem exigir palavras idênticas.

**Perguntas ao circular:** “Qual passo está sendo executado?”, “Qual evidência sustenta isso?”
e “O que precisaria mudar para sua conclusão ser diferente?”

**Dica para a dupla:** separar o que observou do que está supondo.
**Variação difícil:** formular um contraexemplo ou limite; transferir para casa se não couber.

## 65–77 — Exercício individual

**Fala do professor — enunciado:**

{quote(record["individual"])}

**Tempo:** 2 minutos de leitura, 7 de resolução e 3 de revisão/entrega.
Cada aluno entrega uma resposta própria, mesmo quando a atividade anterior foi em grupo.

**Entrega:** artefato pedido no enunciado, acompanhado de uma explicação breve da decisão.
**Critérios:** correção, completude do recorte, evidência e justificativa. Aplicar a
[rubrica formativa]({rules_link}), de 0 a 2 por critério. Referência proposta: 6/8, sem zero em correção ou evidência.

**Ajuda graduada:** pedir que identifique primeiro a entrada, regra ou exigência; depois que escolha o próximo
passo. Não resolver todas as etapas. Registrar qual parte foi assistida e conferir transferência em uma tentativa nova.

**Gabarito comentado — revelar depois da tentativa:**

{quote(record["answer"])}

## 77–85 — Correção, intervenções e dúvidas

**Fala para iniciar a correção:**

> Se sua resposta foi diferente, mantenha a primeira versão. Vamos descobrir em qual decisão
> o raciocínio mudou. Corrigir e explicar a mudança faz parte da aprendizagem.

{corrections}

**Dúvida central da aula:** “{record["check"][0]}”

**Como responder:**

{quote(record["check"][1])}

**Se perguntarem se a resposta precisa ser igual:**

> Não precisa repetir minha frase. Precisa respeitar as regras e permitir que outra pessoa
> confira como você chegou à decisão.

**Se perguntarem como usar a gravação:**

> Localize o trecho em que surgiu a dúvida, reveja o exemplo e depois tente uma entrada ou situação nova.
> Assistir de novo ajuda; explicar sua própria decisão é o que vamos avaliar.

**Modelo de devolutiva:**

> Você acertou ao identificar a decisão principal. Falta mostrar a informação que a sustenta.
> Acrescente essa evidência e explique o que mudou na sua revisão.

Selecionar duas dúvidas para os oito minutos. Registrar as demais para resposta após a aula ou retomada.
Não ampliar silenciosamente a duração do encontro.

## 85–90 — Fechamento e tarefa para casa

**Fala de fechamento:**

> Hoje trabalhamos como {record["goal"]}.
> Para revisar, procure uma decisão, a evidência que a sustenta e uma limitação que ainda precisa de atenção.
> Guardem a primeira versão e a correção; isso ajuda a explicar a evolução no portfólio.

**Pergunta de saída:** “O que você mudou na sua primeira previsão, e por quê?”

**Tarefa de casa — falar à turma:**

{quote(record["home"])}

**Tempo-base:** 30–45 minutos para revisão. Se o enunciado exigir concluir vários artefatos, execução pendente
ou preparação da entrega final, combinar prazo e tempo adicional explicitamente; não prometer que tudo cabe
nesse intervalo.

**Entrega:** `{home_name}`, ou arquivos específicos pedidos, contendo resposta inicial, feedback,
versão revisada e explicação. O professor verifica a revisão no início do encontro seguinte.

**Dica:** usar E-book e gravação como apoio; identificar empresa fictícia e origem da evidência.
**Variação difícil:** acrescentar uma situação nova ou uma dúvida de aplicação, com proposta de investigação.

## Checklist do professor e uso da gravação

- [ ] Preparar recursos e exemplo antes do encontro.
- [ ] Pedir previsão antes de revelar referência.
- [ ] Conferir compreensão por exemplo, não por memorização.
- [ ] Alternar condução e revisão na dupla.
- [ ] Preservar exercício individual.
- [ ] Declarar execução, simulação e limites corretamente.
- [ ] Registrar feedback, tarefa e dúvidas pendentes.
- [ ] Disponibilizar gravação para revisão e indicar os blocos de demonstração e correção.

Percentual de vídeo assistido é sinal de utilização, não prova de domínio.
Usar artefato e explicação para avaliar aprendizagem; não penalizar o aluno por uma falha de registro de reprodução.
"""

lessons = sorted((ROOT / "aulas").glob("modulo-*-aula-*.md"))
lessons += sorted((ROOT / "bonus").glob("aula-*.md"))
for source in lessons:
    match = re.match(r"modulo-(\d+)-aula-(\d+)-", source.name)
    if match:
        module, number = map(int, match.groups())
        key = f"m{module:02d}a{number:02d}"
        ebook = next((ROOT / "ebooks").glob(f"modulo-{module:02d}-*.md"))
    else:
        number = int(re.match(r"aula-(\d+)", source.name).group(1))
        key = f"b{number:02d}"
        ebook = ROOT / "ebooks/bonus-preparacao-para-o-mercado.md"
    target = source.parent / "scripts" / source.name
    text = source.read_text(encoding="utf-8-sig")
    title = title_of(text)
    if key == KEEP:
        if not target.exists():
            raise ValueError("Script da primeira aula ausente")
    else:
        if key not in records:
            raise ValueError("Falas ainda não preparadas para " + key)
        safe_write(target, render(records[key], source, target, title, ebook))

    if rel(source, target) not in text:
        first, rest = text.split("\n", 1)
        text = first + "\n\n**Condução com falas prontas:** [script do professor](" + rel(source, target) + "). " \
            "Seguir a sequência de até 90 minutos. As atividades abaixo formam o caderno completo; " \
            "o script define o recorte ao vivo e a conclusão em casa. A gravação serve para revisão posterior.\n" + rest
    text = re.sub(r"\| Etapa \|[^\n]*\n\|[^\n]*\n(?:\|[^\n]*\n)*?\| Total(?: sugerido)? \|[^\n]*\n",
                  SHORT_TABLE, text, count=1)
    # O roteiro da primeira aula adaptada já usa esta tabela; preservá-la.
    if "| Total | 90 |" not in text:
        raise ValueError("Tabela de duração não encontrada: " + source.name)
    replacements = {
        "— 10 minutos": "— 8 minutos",
        "— 20 minutos": "— 17 minutos",
        "— 15 minutos": "— 20 minutos",
        "— 25 minutos": "— 15 minutos",
        "Preservar o tempo de aula já indicado, distribuindo a prática dentro das etapas existentes.":
            "Usar o script para distribuir o encontro de até 90 minutos e orientar a conclusão em casa.",
        "Distribua os 20 minutos": "Distribua os 17 minutos",
        "Trocar papéis após dez minutos.": "Trocar papéis após cinco minutos.",
        "**Tempo:** 20 minutos.": "**Tempo:** 12 minutos.",
        "**Distribuição:** 3 minutos de leitura; 10 de execução; 7 de revisão cruzada; 5 de compartilhamento.":
            "**Distribuição:** 2 minutos de leitura; 5 de execução; 5 de revisão cruzada; 3 de compartilhamento.",
        "1. Em 3 minutos, ler o enunciado de cada atividade e identificar a regra ou premissa.":
            "1. Em 2 minutos, ler o recorte do enunciado no script e identificar a regra ou premissa.",
        "2. Em 10 minutos, executar as etapas abaixo e registrar o resultado.":
            "2. Em 5 minutos, executar o recorte principal e registrar o resultado.",
        "3. Em 7 minutos, revisar o colega: localizar uma evidência, uma lacuna e uma proposta de correção.":
            "3. Em 5 minutos, trocar funções e revisar uma evidência, uma lacuna e uma correção.",
        "4. Em 5 minutos, apresentar uma decisão e sua justificativa; com muitas duplas, selecionar duas e recolher as demais por escrito.":
            "4. Em 3 minutos, selecionar duas duplas para apresentar; recolher as demais por escrito.",
    }
    if key != KEEP:
        for old, new in replacements.items():
            text = text.replace(old, new)
        text = re.sub(r"(## Exercício individual) — \d+ minutos", r"\1 — 12 minutos", text)
        text = re.sub(r"(## Perguntas para os alunos e correção) — \d+ minutos", r"\1 — 8 minutos", text)
    # Remover duplo ponto de frases geradas, preservando código e pontuação normal.
    text = text.replace("código..", "código.").replace("validação..", "validação.")
    safe_write(source, text)

scripts = sorted((ROOT / "aulas/scripts").glob("modulo-*.md"))
scripts += sorted((ROOT / "bonus/scripts").glob("aula-*.md"))
index = """# Scripts do professor — índice de condução

Todos os 32 roteiros dos módulos e as duas aulas de carreira possuem script com falas.
Cada encontro tem até 90 minutos, com explicação, demonstração, prática, correção e tarefa.
As gravações são dos encontros ao vivo e ficam para revisão; não há exigência de vídeos prévios.

Os scripts separam **falar**, **mostrar**, **perguntar**, **esperar** e **corrigir**.
Usar o roteiro para planejamento, o script para condução e o E-book para aprofundamento.

| Aula | Falas e condução | Planejamento |
|---|---|---|
"""
for source in lessons:
    target = source.parent / "scripts" / source.name
    title = title_of(source.read_text(encoding="utf-8"))
    index += f"| {title} | [Script]({rel(ROOT / 'planejamento/scripts-do-professor.md', target)}) | [Roteiro]({rel(ROOT / 'planejamento/scripts-do-professor.md', source)}) |\n"
index += """
## Tempo e conclusão das atividades

São 34 encontros-base de até 90 minutos: até 51 horas ao vivo, incluindo pausa.
As tarefas completas dos módulos continuam previstas no caderno e são concluídas com estudo e revisão fora da aula.
Essa redistribuição substitui o cronograma inicial de 71 horas ao vivo; não significa que todo conteúdo foi ensinado
no mesmo tempo. Reservar encontros adicionais de reforço se a turma precisar e explicitar isso no calendário.
Este ajuste não estabelece duração comercial ou quantidade de cobranças.

## Uso pelo professor

1. Preparar exemplo e recursos antes de gravar.
2. Pedir previsão e ouvir duas respostas antes de mostrar a referência.
3. Seguir o recorte de prática e preservar a tentativa individual.
4. Usar as intervenções para pedir evidência e esclarecer o erro.
5. Indicar o que precisa ser concluído em casa e quando será devolvido.
6. Disponibilizar gravação com indicação de demonstração e correção.

O texto é apoio de fala, não obrigação de leitura literal. Cada exemplo e gabarito deve continuar
coerente com as regras do caso, inclusive ao adaptar nomes e entradas.
"""
safe_write(ROOT / "planejamento/scripts-do-professor.md", index)
print(f"Gerados {len(scripts)} scripts; {len(lessons)} roteiros adaptados para 90 minutos.")
