from Modelos.Animal import Animal

class EscenarioPila:
    def __init__(self, pila: list[Animal]):
        self.pila = pila
        self.grandezaTotal = pila[0].grandeza + pila[1].grandeza + pila[2].grandeza
        self.buildPila()

    def __str__(self):
        pila_str = "-".join(str(animal) for animal in self.pila)
        return f" \n EscenarioPila: \n {pila_str} Grandeza Total Escena: {self.grandezaTotal} \n"
    
    def getPila(self):
        return self.pila