from Modelos.RojiNegroEspectaculo import ArbolRojoNegro

class EspectaculoRojiNegro:
    def __init__(self, arbol: ArbolRojoNegro):
        self.partes = arbol
        self.maxEscena = arbol.max().valor.maxEscena
        self.minEscena = arbol.max().valor.minEscena
        self.promedio = arbol.max().valor.promedio