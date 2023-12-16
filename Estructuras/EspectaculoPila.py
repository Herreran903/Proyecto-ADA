import random
from Modelos.Animal import Animal
from Modelos.Escenario import Escenario
from Modelos.Parte import Parte
from Modelos.Pila import Pila
from Estructuras.EscenarioPila import EscenarioPila
from Estructuras.PartePila import PartePila

class EspectaculoPila:
    def __init__(self, animales, m, k):
        self.animales = animales
        self.m = m
        self.k = k
        self.partes = []


    def mostrar_espectaculo(self):
        for i, parte in enumerate(self.partes, start=1):
            print(f"Parte {i}")
            for escenario in parte.escenarios:
                print("Escenario")
                for animal in escenario.animales:
                    print(animal)

    def obtener_datos_espectaculo(self):
        animales_participacion = {}

        for parte in self.partes:
            for escenario in parte.escenarios:
                for animal in escenario.animales:
                    if animal.nombre in animales_participacion:
                        animales_participacion[animal.nombre] += 1
                    else:
                        animales_participacion[animal.nombre] = 1

        animal_mas_participacion = max(animales_participacion, key=animales_participacion.get)
        animal_menos_participacion = min(animales_participacion, key=animales_participacion.get)

        menor_grandeza_total = float('inf')
        mayor_grandeza_total = float('-inf')

        for parte in self.partes:
            for escenario in parte.escenarios:
                grandeza_total = sum(animal.grandeza for animal in escenario.animales)
                menor_grandeza_total = min(menor_grandeza_total, grandeza_total)
                mayor_grandeza_total = max(mayor_grandeza_total, grandeza_total)

        promedio_grandeza = sum(animal.grandeza for animal in self.animales) / len(self.animales)

        return {
            "animal_mas_participacion": (animal_mas_participacion, animales_participacion[animal_mas_participacion]),
            "animal_menos_participacion": (animal_menos_participacion, animales_participacion[animal_menos_participacion]),
            "menor_grandeza_total": menor_grandeza_total,
            "mayor_grandeza_total": mayor_grandeza_total,
            "promedio_grandeza": promedio_grandeza
        }
