class Animal:
    def __init__(self, nombre: str, grandeza: int):
        self.nombre = nombre
        self.grandeza = grandeza
        self.repeticiones = 0

    def aumentarRepeticiones(self):
        self.repeticiones += 1

    def __str__(self):
        return f"Animal: {self.nombre}, Grandeza: {self.grandeza}, Repeticiones: {self.repeticiones} \n"