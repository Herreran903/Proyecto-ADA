import random

from Estructuras.EscenarioHeap import EscenarioHeap
from Estructuras.ParteHeap import ParteHeap
from Modelos.Animal import Animal
from Modelos.Parte import Parte

class Espectaculo:

    NOMBRE_ANIMALES = ["Leon", "Tigre", "Jirafa", "Elefante", "Cocodrilo", "Cebra", "Hipopotamo",
                       "Avestruz", "Pinguino", "Panda", "Lobo", "Oso", "Puma", "Gorila", "Mono",
                       "Aguila", "Pato", "Cisne", "Pez", "Tiburon", "Ballena", "Delfin", "Pulpo",
                       "Cangrejo", "Serpiente", "Raton", "Ardilla", "Castor", "Conejo", "Gato", "Perro",
                       "Caballo", "Vaca", "Cerdo", "Oveja", "Gallina", "Pavo", "Pato", "Paloma", "Gaviota",
                       "Loro", "Colibri", "Mariposa", "Abeja", "Hormiga", "Mosca", "Mosquito", "Grillo",
                       "Saltamontes", "Cigarra", "Libelula", "Escorpion", "Araña", "Caracol", "Lombriz",
                       "Rana", "Sapo", "Salamandra", "Tortuga", "Iguana", "Camaleon", "Cocodrilo", "Tortuga"]

    def __init__(self, n, m, k):
        self.k = k
        self.m = m
        self.n = n
        self.animales = self.generarAnimalesAlAzar(n)
        self.granApertura = None
        self.partes = []

    def generarAnimalesAlAzar(self, n):

        animales: list[Animal] = []

        if n > len(self.NOMBRE_ANIMALES):
            raise Exception("No hay suficientes animales para generar un escenario de ese tamaño")
        elif n < 3:
            raise Exception("Los escenarios deben tener al menos 3 animales")
        else:
            pass

        for i in range(n):
            nombre = random.choice(self.NOMBRE_ANIMALES)
            grandeza = i+1
            animales.append(Animal(nombre, grandeza))

        return animales

    def generarEscenarioAlAzar(self):

        animalesSelectos = random.sample(self.animales, 3)

        while len(set(animal.grandeza for animal in animalesSelectos)) < 3:
            animalesSelectos = random.sample(self.animales, 3)

        return EscenarioHeap(animalesSelectos).buildHeap()

    def generarParteAlAzar(self):

        parte = []

        for i in range(self.k):
            escenario = self.generarEscenarioAlAzar()
            parte.append(escenario)

        return ParteHeap(parte).buildHeap()

    def crearEspectaculoHeap(self):

        auxEscenarios = []

        for i in range((self.m-1)*self.k):
            auxEscenarios.append(self.generarEscenarioAlAzar())

        print(len(auxEscenarios))

        self.granApertura = ParteHeap(auxEscenarios)

        print(len(self.granApertura.getHeap()))

        for i in range(self.m-1):
            auxParte = random.sample(self.granApertura.getHeap(), self.k)
            self.partes.append(ParteHeap(auxParte))

        return self

    def ordenarEspectaculo(self):
        self.granApertura.heapSort()
        for parte in self.partes:
            parte.heapSort()
            for escenario in parte.getHeap():
                escenario.heapSort()
        return self
    def __str__(self):
        partes_str = ", ".join(str(parte) for parte in self.partes)
        return f"Espectaculo: \n Gran Apertura: {self.granApertura} \n Partes: {partes_str}"
