from Modelos.RojiNegroParte import ArbolRojoNegro

class ParteRojiNegro:
    def __init__(self, arbol: ArbolRojoNegro):
        self.escenas = arbol
        self.maxEscena = arbol.max()
        self.minEscena = arbol.min()
        self.grandeza = arbol.suma()
        self.promedio = arbol.promedio()

    def __str__(self):
        escenas = self.escenas.inOrder()
        escenas_str = "".join(str(escena) for escena in escenas)
        return f"{escenas_str}"

        