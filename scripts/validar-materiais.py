"""Valida estrutura, links locais, exemplos Python e regras do laboratório DTEM."""
from pathlib import Path
import contextlib
import importlib.util
import io
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
erros = []

def conferir(condicao, mensagem):
    if not condicao:
        erros.append(mensagem)

def normalizar(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto.lower())
                   if unicodedata.category(c) != "Mn")

ebooks = sorted((ROOT / "ebooks").glob("modulo-*.md"))
aulas = sorted((ROOT / "aulas").glob("modulo-*.md"))
bonus = sorted((ROOT / "bonus").glob("aula-*.md"))
conferir(len(ebooks) == 8, f"Esperados 8 E-books; encontrados {len(ebooks)}")
conferir(len(aulas) == 32, f"Esperadas 32 aulas; encontradas {len(aulas)}")
conferir(len(bonus) == 2, f"Esperadas 2 aulas de bônus; encontradas {len(bonus)}")

arquivos = []
for pasta in ("ebooks", "aulas", "bonus", "atividades", "planejamento", "portfolio"):
    arquivos.extend((ROOT / pasta).rglob("*.md"))
arquivos.append(ROOT / "README.md")
links = 0
for arquivo in arquivos:
    texto = arquivo.read_text(encoding="utf-8-sig")
    conferir(texto.count("```") % 2 == 0, f"Cerca de código sem par: {arquivo.name}")
    conferir("\ufffd" not in texto, f"Caractere de substituição: {arquivo.name}")
    for alvo in re.findall(r"\]\(([^)]+)\)", texto):
        alvo = alvo.strip("<>").split("#", 1)[0]
        if not alvo or re.match(r"^[a-z]+:", alvo, re.I):
            continue
        links += 1
        conferir((arquivo.parent / alvo).exists(), f"Link inexistente em {arquivo.name}: {alvo}")

campos = ("conceito", "explicacao simples", "explicacao tecnica", "exemplo do mundo real",
          "exemplo dentro de uma empresa", "erros comuns de iniciantes", "boas praticas",
          "como isso aparece em vagas", "como isso ajuda na carreira", "exercicio pratico")
for arquivo in ebooks:
    texto = arquivo.read_text(encoding="utf-8-sig")
    conferir("```mermaid" in texto, f"Diagrama ausente: {arquivo.name}")
    if arquivo.name.startswith("modulo-01"):
        continue
    secoes = re.split(r"^## topico \d+ — ", normalizar(texto), flags=re.M)[1:]
    conferir(bool(secoes), f"Tópicos ausentes: {arquivo.name}")
    for numero, secao in enumerate(secoes, 1):
        secao = secao.split("\n## ", 1)[0]
        for campo in campos:
            conferir("### " + campo in secao, f"{arquivo.name}, tópico {numero}: falta {campo}")

for numero in range(1, 9):
    conferir(len(list((ROOT / "aulas").glob(f"modulo-{numero:02d}-aula-*.md"))) == 4,
             f"Módulo {numero}: quantidade de aulas diferente de quatro")

spec = importlib.util.spec_from_file_location("agenda", ROOT / "portfolio/agenda-clara/agenda_clara.py")
modulo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modulo)
agenda = modulo.Agenda()
conferir(agenda.consultar() == ["H09", "H10", "H11"], "RN01: catálogo")
conferir(agenda.reservar("", "H11")["status"] == "nome_invalido", "RN03: vazio")
conferir(agenda.reservar("   ", "H11")["status"] == "nome_invalido", "RN03: espaços")
conferir(agenda.consultar() == ["H09", "H10", "H11"], "RN03: estado preservado")
primeira = agenda.reservar("Ana", "H09")
conferir(primeira["status"] == "sucesso", "RN04: reserva")
anterior = {k: dict(v) for k, v in agenda.reservas.items()}
conferir(agenda.reservar("Bruno", "H09")["status"] == "conflito", "RN02/RN05: conflito")
conferir(agenda.reservas == anterior, "RN05: preservar reserva")
conferir(agenda.cancelar(999)["status"] == "nao_encontrado", "RN07: id inexistente")
conferir(agenda.reservas == anterior, "RN07: preservar demais")
conferir(agenda.reservar("Dani", "H12")["status"] == "horario_invalido", "RN08")
conferir(agenda.reservas == anterior, "RN08: preservar estado")
conferir(agenda.cancelar(primeira["id"])["status"] == "cancelado", "RN06: cancelar")
conferir("H09" in agenda.consultar(), "RN06: liberar")
nova = agenda.reservar("Carla", "H09")
conferir(nova["id"] != primeira["id"], "Re-reserva: novo id")
conferir(agenda.cancelar(primeira["id"])["status"] == "nao_encontrado", "Id antigo")
conferir(agenda.reservas[nova["id"]]["nome"] == "Carla", "Preservar re-reserva")
agenda.reservar("Dani", "H10")
agenda.reservar("Edu", "H11")
conferir(agenda.consultar() == [], "Catálogo esgotado")
variante = modulo.AgendaComDefeito()
conferir(variante.reservar("   ", "H11")["status"] == "sucesso", "BUG01 plantado")
conferir("H11" not in variante.consultar(), "BUG01: efeito no estado")

texto_logica = (ROOT / "ebooks/modulo-02-logica-de-programacao.md").read_text(encoding="utf-8")
blocos = re.findall(r"```python\n(.*?)\n```", texto_logica, flags=re.S)
esperadas = [
    ["Ana Exemplo H09 2", "5", "23", "True"],
    ["nome_invalido"],
    ["['H09', 'H11']"],
    ["Tentativa 1", "Tentativa 2", "Tentativa 3"],
    ["'Ana' True", "'' False", "'   ' False"],
]
conferir(len(blocos) == 5, f"Esperados cinco exemplos Python; encontrados {len(blocos)}")
for numero, (bloco, esperado) in enumerate(zip(blocos, esperadas), 1):
    saida = io.StringIO()
    try:
        with contextlib.redirect_stdout(saida):
            exec(compile(bloco, f"exemplo-{numero}", "exec"), {})
        conferir(saida.getvalue().splitlines() == esperado, f"Saída divergente: exemplo {numero}")
    except Exception as exc:
        erros.append(f"Falha no exemplo {numero}: {exc}")

if erros:
    print("\n".join(erros))
    raise SystemExit(1)
print(f"OK: {len(ebooks)} E-books, {len(aulas)} aulas, {len(bonus)} aulas de bônus")
print(f"OK: {len(arquivos)} arquivos Markdown; {links} links locais conferidos")
print("OK: RN01–RN08, re-reserva, catálogo esgotado e BUG01")
print("OK: cinco exemplos Python executados com as saídas documentadas")
