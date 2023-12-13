import random

from Modelos.Animal import Animal

## Las siguientes funciones se usaran exclusivamente para generar un espectaculo al azar. A partir de ellas
## se generarn los epectaculos con sus respectivas estructa de datos. Se generarn conjuntos de Python, para los
## escearios, partes y espectaculos, y luego se convertiran a las estructuras de datos correspondientes. Los
## animales seran objetos de la clase Animal.


# Lista de nombres de animales para generar los animales al azar.

NOMBRE_ANIMALES = ["Leon", "Tigre", "Jirafa", "Elefante", "Cocodrilo", "Cebra", "Hipopotamo",
                   "Avestruz", "Pinguino", "Panda", "Lobo", "Oso", "Puma", "Gorila", "Mono",
                   "Aguila", "Pato", "Cisne", "Pez", "Tiburon", "Ballena", "Delfin", "Pulpo",
                   "Cangrejo", "Serpiente", "Raton", "Ardilla", "Castor", "Conejo", "Gato", "Perro",
                   "Caballo", "Vaca", "Cerdo", "Oveja", "Gallina", "Pavo", "Pato", "Paloma", "Gaviota",
                   "Loro", "Colibri", "Mariposa", "Abeja", "Hormiga", "Mosca", "Mosquito", "Grillo",
                   "Saltamontes", "Cigarra", "Libelula", "Escorpion", "Araña", "Caracol", "Lombriz",
                   "Rana", "Sapo", "Salamandra", "Tortuga", "Iguana", "Camaleon", "Cocodrilo", "Tortuga"]


# Funcion que genera una lista de animales al azar. Recibe como parametro la cantidad de animales que se desean generar.

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

# Funcion que genera un escenario al azar. Recibe como parametro una lista de animales.

def generarEscenarioAlAzar(animales):

    animalesSelectos = random.sample(animales, 3)

    while len(set(animal.grandeza for animal in animalesSelectos)) < 3:
        animalesSelectos = random.sample(animales, 3)

    return animalesSelectos

# Funcion que genera una parte al azar. Recibe como parametro una lista de animales y la cantidad de escenarios que
# se desean generar.

def generarParteAlAzar(animales, k):

    parte: list[list[Animal]] = []

    for i in range(k):
        escenario = generarEscenarioAlAzar(animales)
        parte.append(escenario)

    return parte

# Funcion que genera un espectaculo al azar. Recibe como parametro una lista de animales, la cantidad de escenarios
# que se desean generar y la cantidad de partes que se desean generar.

def generarEspectaculoAlAzar(animales, k, m):

    espectaculo: list[list[list[Animal]]] = []

    primerActo = generarParteAlAzar(animales, (m-1)*k)

    auxPrimerActo = primerActo.copy()

    espectaculo.append(primerActo)

    for i in range(m-1):
        parte = random.sample(auxPrimerActo, k)
        espectaculo.append(parte)
        auxPrimerActo = [escenario for escenario in auxPrimerActo if escenario not in parte]

    return espectaculo