"""Simulador educacional DTEM: chamadas sequenciais, dados em memória."""
class Agenda:
    def __init__(self):
        self.catalogo = ("H09", "H10", "H11")
        self.reservas = {}
        self.proximo_id = 1

    def consultar(self):
        ocupados = {r["horario"] for r in self.reservas.values()}
        return [h for h in self.catalogo if h not in ocupados]

    def reservar(self, nome, horario):
        if not isinstance(nome, str) or not nome.strip():
            return {"status": "nome_invalido"}
        if horario not in self.catalogo:
            return {"status": "horario_invalido"}
        if horario not in self.consultar():
            return {"status": "conflito"}
        identificador = self.proximo_id
        self.proximo_id += 1
        self.reservas[identificador] = {"nome": nome.strip(), "horario": horario}
        return {"status": "sucesso", "id": identificador}

    def cancelar(self, identificador):
        if identificador not in self.reservas:
            return {"status": "nao_encontrado"}
        del self.reservas[identificador]
        return {"status": "cancelado"}


class AgendaComDefeito(Agenda):
    """Defeito plantado: espaços são aceitos como nome válido."""
    def reservar(self, nome, horario):
        if isinstance(nome, str) and nome and not nome.strip():
            nome = "Nome não informado"
        return super().reservar(nome, horario)


def demonstrar(classe):
    agenda = classe()
    print("\nVersão:", classe.__name__)
    print("Horários:", agenda.consultar())
    print("Reserva Ana:", agenda.reservar("Ana Exemplo", "H09"))
    print("Conflito Bruno:", agenda.reservar("Bruno Exemplo", "H09"))
    print("Nome com espaços:", agenda.reservar("   ", "H11"))
    print("Cancelar 1:", agenda.cancelar(1))
    print("Horários finais:", agenda.consultar())


if __name__ == "__main__":
    demonstrar(Agenda)
    demonstrar(AgendaComDefeito)

