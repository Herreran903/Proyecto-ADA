from Modelos.Animal import Animal
from Modelos.RojiNegroEscena import ArbolRojoNegro

class EscenaRojinegro:
    def __init__(self, arbol: ArbolRojoNegro):
        self.arbol = arbol
        self.grandeza = arbol.suma()
        self.maxGrandeza = arbol.max()

    def __str__(self):
        animales = self.arbol.inOrder()
        escenas_str = "".join(str(animal) for animal in animales)
        return f"{escenas_str}"