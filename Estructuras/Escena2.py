from Modelos.Animal import Animal
from Modelos.Pila import Pila

class Escena2:
    def __init__(self, pila: Pila):
        self.pila = pila
        self.grandeza = pila.GrandezaTotal()
        self.maxGrandeza = pila.mayorGrandeza()