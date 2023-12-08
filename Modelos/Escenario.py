from Modelos.Animal import Animal

class Escenario:
    def __init__(self):
        self.animalesLista = list()

    def __str__(self):
        animales_str = ", ".join(str(animal) for animal in self.animales)
        return f"Escenario: {animales_str}"