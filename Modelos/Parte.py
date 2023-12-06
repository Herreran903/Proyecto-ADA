from Modelos.Escenario import Escenario

class Parte:
    def __init__(self, escenarios: set[Escenario]):
        self.escenarios = escenarios

    def __str__(self):
        escenarios_str = ", ".join(str(escenario) for escenario in self.escenarios)
        return f"Parte: {escenarios_str}"