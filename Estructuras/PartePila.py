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

    def buildPila(self):
        self.pila.sort(key=lambda escenario_pila: escenario_pila.grandezaTotal)

    def sumarGrandezas(self):
        return sum(escenario_pila.grandezaTotal for escenario_pila in self.pila)

    def getGrandezaMinima(self):
        return min(escenario_pila.grandezaTotal for escenario_pila in self.pila)

    def getGrandezaMaxima(self):
        return max(escenario_pila.grandezaTotal for escenario_pila in self.pila)

    def getEscenarioMayorGrandeza(self):
        return max(self.pila, key=lambda escenario_pila: escenario_pila.grandezaTotal)

    def getEscenarioMenorGrandeza(self):
        return min(self.pila, key=lambda escenario_pila: escenario_pila.grandezaTotal)
        
