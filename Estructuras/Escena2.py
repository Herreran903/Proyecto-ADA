from Modelos.Animal import Animal
from Modelos.Pila import Pila

class Escena2:
    def __init__(self, pila: Pila):
        self.pila = pila
        self.grandeza = pila.GrandezaTotal()
        self.maxGrandeza = pila.mayorGrandeza()

    def __str__(self) -> str:
        pila_str = "-".join(str(animal) for animal in self.pila.items)
        return f" \n EscenaPila: \n {pila_str} Grandeza Total: {self.grandeza} \n Grandeza Maxima: {self.maxGrandeza} \n"