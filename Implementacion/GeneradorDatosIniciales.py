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
                   "Rana", "Sapo", "Salamandra", "Tortuga", "Iguana", "Camaleon", "Cocodrilo", "Tortuga",
                   "Leopardo", "Jaguar", "Pantera", "Guepardo", "Hiena", "Zorro", "Mapache", "Zorrillo",
                   "Erizo", "Koala", "Kanguru", "Wombat", "Suricata", "Huron", "Tejon", "Comadreja",
                   "Nutria", "Morsa", "Foca", "León marino", "Orca", "Beluga", "Narval", "Morsa",
                   "Hipopótamo pigmeo", "Tapir", "Okapi", "Ñu", "Búfalo", "Bisonte", "Alce", "Caribu",
                   "Reno", "Saiga", "Antílope", "Impala", "Gacela", "Chita", "Puercoespín", "Lemur",
                   "Tarsio", "Colobo", "Babuino", "Mandrill", "Capuchino", "Lémur de cola anillada", "Lémur ratón",
                   "Lémur enano", "Lémur de vientre rojo", "Lémur de coronilla dorada", "Lémur de hocico rojo", "Lémur de cola anillada",
                   "Lémur de collar", "Lémur negro", "Lémur blanco y negro", "Lémur de panza roja", "Lémur rufo rojo", "Lémur de Verreaux",
                   "Lémur indri", "Lémur de bambú", "Lémur enano de cola roja", "Lémur de Alaotra", "Lémur de cola roja", "Lémur blanco de frente",
                   "Lémur coronado", "Lémur de Sclater", "Lémur de Barbe", "Lémur de Gerp", "Lémur de Gentle", "Lémur de Jolly", "Lémur de Raffray",
                   "Lémur de Scott", "Lémur de Spix", "Lémur de Robacza", "Lémur de Simpona", "Lémur de Colla", "Lémur de Brown", "Lémur de Czerlon",
                   "Lémur de Dow", "Lémur de Indri", "Lémur de Groves", "Lémur de Hombron", "Lémur de Laurillard", "Lémur de Oconnelli", "Lémur de Perrier",
                   "Lémur de William", "Lémur dorado", "Lémur flavifrons", "Lémur fulvus", "Lémur Hapalemur", "Lémur maki", "Lémur nigerrimus", "Lémur orablanca",
                   "Lémur pardo", "Lémur pálido", "Lémur plateado", "Lémur rubriventer", "Lémur rufifrons", "Lémur sifaca", "Lémur Variegata", "Lémur Weiszs",
                   "Lémur willem", "Lémur mongoz", "Lémur de mamíferos", "Lémur de prosimios", "Lémur de antropoides", "Lémur de primates", "Lémur de simios", "Lémur de monos",
                   "Lémur de tarseros", "Lémur de prosimios", "Lémur de loris", "Lémur de tarsero", "Lémur de lémures", "Lémur de monos", "Lémur de primates", "Lémur de simios",
                   "Lémur de grandes simios"]

# Funcion que genera una lista de animales al azar. Recibe como parametro la cantidad de animales que se desean generar.

def generarAnimalesAlAzar(n):
    animales = []
    if n > len(NOMBRE_ANIMALES):
        raise Exception("No hay suficientes animales para generar un escenario de ese tamaño")
    elif n < 3:
        raise Exception("Los escenarios deben tener al menos 3 animales")
    else:
        pass
    nombres_elegidos = set()
    for i in range(n):
        while True:
            nombre = random.choice(NOMBRE_ANIMALES)
            if nombre not in nombres_elegidos:
                nombres_elegidos.add(nombre)
                break
        grandeza = i + 1
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
        while any(all(animal in s for animal in escenario) for s in parte):
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