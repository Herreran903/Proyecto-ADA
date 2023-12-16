class Animal:
    def __init__(self, nombre: str, grandeza: int):
        self.nombre = nombre
        self.grandeza = grandeza

    def __str__(self):
        return f"({self.nombre}, {self.grandeza})\n"