from Estructuras.Escena2 import Escena2 
from Modelos.RojiNegroParte import ArbolRojoNegro, Nodo

class Parte2:
    def __init__(self, arbol: ArbolRojoNegro):
        self.escenas = arbol
        self.maxEscena = arbol.max()
        self.minEscena = arbol.min()
        self.promedio = arbol.promedio()

        