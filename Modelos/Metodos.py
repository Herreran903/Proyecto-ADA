import random

from Modelos.Animal import Animal
from Modelos.Escenario import Escenario
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

def generarEscenarioAlAzar(animales):

    animales_selectos = random.sample(animales, 3)

    while len(set(animal.grandeza for animal in animales_selectos)) < 3:
        animales_selectos = random.sample(animales, 3)

    return Escenario(animales_selectos)

def generarParteAlAzar(animales, k):

    parte = []

    for i in range(k):
        escenario = generarEscenarioAlAzar(animales)
        parte.append(escenario)

    return Parte(parte)

def generarEspectaculoAlAzar(animales, k, m):

    espectaculo = []

    primerActo = generarParteAlAzar(animales, (m-1)*k)

    espectaculo.append(primerActo)

    for i in range(m-1):
        acto = generarParteAlAzar(animales, k)
        espectaculo.append(acto)

    return espectaculo


animales = generarAnimalesAlAzar(10)

espectaculo = generarEspectaculoAlAzar(animales, 3, 2)

i = 0
for parte in espectaculo:
    i += 1
    print("Parte", i)
    for escenario in parte.escenarios:
        print("Escenario")
        for animal in escenario.animales:
            print(animal)
