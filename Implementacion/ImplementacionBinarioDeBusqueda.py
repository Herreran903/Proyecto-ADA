import GeneradorDatosIniciales
from Modelos.BinarioEscena import  ArbolBinarioBusqueda as arbolEscena
from Modelos.BinarioParte import ArbolBinarioBusqueda as arbolParte
from Modelos.BinarioEspectaculo import ArbolBinarioBusqueda as arbolEspectaculo
import time
import matplotlib.pyplot as plt

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(160)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 3)

##SOLUCION 1

print("Solucion 1")

espectaculo = []
for parte in ESPECTACULO:
    part = []
    for escena in parte:
        arbolEscena1 = arbolEscena()
        arbolEscena1.insertarAnimales(escena)
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado

"""
escena1 = GeneradorDatosIniciales.generarEscenarioAlAzar(ANIMALES)

arbolEscena1 = arbolEscena()
arbolEscena1.insertarAnimales(escena1)

for i in arbolEscena1.inorder_traversal():
    print(i)

print("Grandeza escena1")
print(arbolEscena1.suma())

escena2 = GeneradorDatosIniciales.generarEscenarioAlAzar(ANIMALES)
arbolEscena2 = arbolEscena()
arbolEscena2.insertarAnimales(escena2)

for i in arbolEscena2.inorder_traversal():
    print(i)

print("Grandeza escena2")
print(arbolEscena2.suma())

escena3 = GeneradorDatosIniciales.generarEscenarioAlAzar(ANIMALES)
arbolEscena3 = arbolEscena()
arbolEscena3.insertarAnimales(escena3)

for i in arbolEscena3.inorder_traversal():
    print(i)

print("Grandeza escena3")
print(arbolEscena3.suma())

parte1 = [arbolEscena1, arbolEscena2, arbolEscena3]
arbolParte1 = arbolParte()
arbolParte1.insertarEscenas(parte1)

print("Parte1")
print(arbolParte1)

print("Grandeza parte1")
print(arbolParte1.sumar())

print("PromedioParte1")
print(arbolParte1.promedio())

arbolEscena4 = arbolEscena()
arbolEscena4.insertarAnimales(GeneradorDatosIniciales.generarEscenarioAlAzar(ANIMALES))

arbolEscena5 = arbolEscena()
arbolEscena5.insertarAnimales(GeneradorDatosIniciales.generarEscenarioAlAzar(ANIMALES))

parte2 =  [arbolEscena1, arbolEscena2, arbolEscena3, arbolEscena4, arbolEscena5]
arbolParte2 = arbolParte()
arbolParte2.insertarEscenas(parte2)

print("Parte2")
print(arbolParte2)

print("Grandeza parte2")
print(arbolParte2.sumar())

espectaculo1 = [arbolParte1, arbolParte2]
arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo1)

print("Espectaculo1")
print(arbolEspectaculo1)
print("escena mas grande")
print(arbolEspectaculo1.encontrar_maximo().valor.encontrar_maximo())
print("escena mas pequeña")
print(arbolEspectaculo1.encontrar_maximo().valor.encontrar_minimo())
print("promedio")
print(arbolEspectaculo1.encontrar_maximo().valor.promedio())
"""