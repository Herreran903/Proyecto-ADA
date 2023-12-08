import random

from Estructuras.ParteHeap import ParteHeap
from Modelos.Animal import Animal
from Estructuras.EscenarioHeap import EscenarioHeap
from Modelos.Escenario import Escenario
from Modelos.Espectaculo import Espectaculo
from Modelos.Parte import Parte

NOMBRE_ANIMALES = ["Leon", "Tigre", "Jirafa", "Elefante", "Cocodrilo", "Cebra", "Hipopotamo",
                   "Avestruz", "Pinguino", "Panda", "Lobo", "Oso", "Puma", "Gorila", "Mono",
                   "Aguila", "Pato", "Cisne", "Pez", "Tiburon", "Ballena", "Delfin", "Pulpo",
                   "Cangrejo", "Serpiente", "Raton", "Ardilla", "Castor", "Conejo", "Gato", "Perro",
                   "Caballo", "Vaca", "Cerdo", "Oveja", "Gallina", "Pavo", "Pato", "Paloma", "Gaviota",
                   "Loro", "Colibri", "Mariposa", "Abeja", "Hormiga", "Mosca", "Mosquito", "Grillo",
                   "Saltamontes", "Cigarra", "Libelula", "Escorpion", "Araña", "Caracol", "Lombriz",
                   "Rana", "Sapo", "Salamandra", "Tortuga", "Iguana", "Camaleon", "Cocodrilo", "Tortuga"]


def generarAnimalesAlAzar(n):
    animales: list[Animal] = []

    if n > len(NOMBRE_ANIMALES):
        raise Exception("No hay suficientes animales para generar un escenario de ese tamaño")
    elif n < 3:
        raise Exception("Los escenarios deben tener al menos 3 animales")
    else:
        pass

    for i in range(n):
        nombre = random.choice(NOMBRE_ANIMALES)
        grandeza = i+1
        animales.append(Animal(nombre, grandeza))
    return animales


listaDeAnimalesAlAzar = generarAnimalesAlAzar(9)

def generarEscenarioAlAzar(animales):

    animalesSelectos = random.sample(animales, 3)

    while len(set(animal.grandeza for animal in animalesSelectos)) < 3:
        animalesSelectos = random.sample(animales, 3)

    return EscenarioHeap(animalesSelectos).buildHeap()


def generarParteAlAzar(animales, k):

    parte = []

    for i in range(k):
        escenario = generarEscenarioAlAzar(animales)
        parte.append(escenario)

    return ParteHeap(parte).buildHeap()


print(Espectaculo(9, 3, 3).crearEspectaculoHeap().ordenarEspectaculo())