from Modelos import Animal
from Modelos import Pila

class Escenario2:
    def __init__(self, pila: Pila):
        self.pila = pila
        self.grandeza = pila.getGrandeza()
    
    def getPila(self):
        return self.pila
    
    def mayorGrandeza(self):
        return self.pila.getGrandeza()