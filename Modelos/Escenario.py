from Modelos.Animal import Animal

class Escenario:
    def __init__(self, animales: set[Animal]):
        self.animales = animales

    def __str__(self):
        animales_str = ", ".join(str(animal) for animal in self.animales)
        return f"Escenario: {animales_str}"