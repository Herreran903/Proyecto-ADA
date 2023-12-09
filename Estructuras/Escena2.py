from Modelos.Animal import Animal
from Modelos.Pila import Pila

class Escena2:
    def __init__(self, pila: Pila):
        self.pila = pila
        self.grandeza = pila.getGrandeza()
        self.maxGrandeza = pila.maxGrandeza()
    
    def getPila(self):
        return self.pila
    
    def mayorGrandeza(self):
        return self.pila.getGrandeza()