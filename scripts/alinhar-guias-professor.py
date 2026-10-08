"""Alinha guias e navegação ao formato semanal solicitado."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
for book in sorted((ROOT / "ebooks").glob("*.md")):
    text = book.read_text(encoding="utf-8-sig")
    text = re.sub(r"^\*\*Tempo proposto:\*\*.*$", "**Tempo proposto:** quatro encontros de até 90 minutos, com pausa de 5 minutos incluída: até 6 horas ao vivo por módulo. Reservar estudo posterior para concluir atividades e revisar a entrega. A gravação é a do próprio encontro; não há vídeos teóricos prévios obrigatórios.", text, flags=re.M)
    text = re.sub(r"^\*\*Duração sugerida:\*\*.*$", "**Duração sugerida:** quatro encontros de até 90 minutos, incluindo pausa de 5 minutos: até 6 horas ao vivo. O script delimita a prática do encontro; o restante do caderno é concluído depois. Usar papel ou Markdown se uma ferramenta estiver indisponível, identificando a simulação e concluindo posteriormente a execução exigida.", text, flags=re.M)
    text = re.sub(r"\n\*\*Atualização da Aula 1:\*\*.*\n", "\n", text)
    text = text.replace("Sugestão: dois encontros de 120 minutos, com pausa incluída; 30–45 minutos de revisão por encontro.", "Formato: dois encontros de até 90 minutos, com pausa incluída; até 3 horas ao vivo. Concluir e revisar os rascunhos depois, usando a gravação do encontro como apoio.")
    if book.name.startswith("modulo-01"):
        text = re.sub(r"(### Tempo sugerido\n\n)\| Etapa \| Tempo sugerido \|.*?(?=\n### Estratégia)", r"\1Quatro encontros de até 90 minutos, incluindo pausa: até 6 horas ao vivo. Cada aula tem seu script com explicação, demonstração e prática. Consultar os quatro roteiros para a sequência; concluir o caderno de atividades fora do encontro.\n", text, flags=re.S)
    if "## Scripts com falas para o professor" not in text:
        if book.name.startswith("modulo-"):
            module = book.name.split("-")[1]
            sources = sorted((ROOT/"aulas").glob(f"modulo-{module}-aula-*.md"))
            folder = "aulas"
        else:
            sources = sorted((ROOT/"bonus").glob("aula-*.md"))
            folder = "bonus"
        links = "\n".join(f"- [Aula {n} — script com falas](../{folder}/scripts/{src.name})" for n, src in enumerate(sources,1))
        text += "\n\n## Scripts com falas para o professor\n\nUsar o roteiro para planejar, o script para conduzir e este E-book para aprofundar. As falas são apoio adaptável, com exemplos, perguntas, gabaritos e intervenções. O aluno revê a gravação do encontro na plataforma.\n\n"+links+"\n\nPlanejar inicialmente 30–45 minutos de revisão e conclusão por aula; exercícios técnicos, projeto final e portfólio podem exigir blocos maiores. Combinar essa carga e os prazos com a turma. Não comprimir toda a prática original em 90 minutos.\n"
    book.write_text(text.rstrip()+"\n", encoding="utf-8")
index = ROOT/"planejamento/trilha-e-indice.md"
text = index.read_text(encoding="utf-8-sig")
text = re.sub(r"(## Organização e tempo sugerido\n\n).*?(?=\n## Como usar os materiais)", r"\1Todos os oito módulos têm quatro encontros de até 90 minutos: **32 encontros e até 48 horas ao vivo**. Com as duas aulas de carreira, são **34 encontros e até 51 horas**, incluindo pausas. A sequência semanal corresponde a 34 semanas de conteúdo, antes de feriados, recessos, recuperação e encontros extras.\n\nConsultar o [índice de scripts com falas](scripts-do-professor.md). A demonstração e a prática principal acontecem ao vivo; a gravação fica disponível para revisão. Não há vídeos teóricos prévios obrigatórios. O caderno completo continua nos roteiros e E-books, com conclusão fora do encontro.\n\nPlanejar 30–45 minutos iniciais de estudo posterior por aula e ampliar os blocos conforme a atividade, especialmente projeto final e portfólio. As apresentações de todos os alunos e defesas ao vivo podem exigir encontros adicionais. Combinar carga de tarefas, prazos e ritmo com a turma antes de fechar o calendário comercial.\n",text,flags=re.S)
index.write_text(text,encoding="utf-8")
audit = ROOT/"planejamento/analise-pedagogica.md"
text = audit.read_text(encoding="utf-8-sig").replace("4. Trabalhar com quatro aulas de 120 minutos por módulo novo, com pausa de 10 minutos incluída. O tempo é proposta pedagógica, não carga comercial confirmada.", "4. Seguir o formato definido para a mentoria: quatro encontros de até 90 minutos por módulo, incluindo pausa de 5 minutos. O script seleciona a prática principal ao vivo; as atividades completas são concluídas depois. São 34 encontros com o bônus; apresentações e recuperação podem exigir encontros adicionais.")
audit.write_text(text,encoding="utf-8")
readme = ROOT/"README.md"
text = readme.read_text(encoding="utf-8-sig")
if "[scripts com falas do professor]" not in text:
    text = text.replace("Todos os materiais finais estão em Markdown.", "Todos os materiais finais estão em Markdown.\n\nAs **34 aulas** possuem [scripts com falas do professor](planejamento/scripts-do-professor.md), com sequência de até 90 minutos, demonstrações, perguntas, respostas esperadas e tarefas. As gravações são dos encontros ao vivo e servem para revisão na plataforma.")
readme.write_text(text,encoding="utf-8")
print("Guias, E-books e navegação alinhados ao formato de 90 minutos.")

