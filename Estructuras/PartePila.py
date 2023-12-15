from Estructuras.EscenarioPila import EscenarioPila


class PartePila:
    def __init__(self, pila: list[EscenarioPila]):
        self.pila = pila
        self.grandezaTotal = self.sumarGrandezas()
        self.buildPila()

    def __str__(self):
        pila_str = ", ".join(str(escenario) for escenario in self.pila)
        return f"  \n PartePila: {pila_str} \n Grandeza Total Parte: {self.grandezaTotal}"
    
    def getPila(self):
        return self.pila
