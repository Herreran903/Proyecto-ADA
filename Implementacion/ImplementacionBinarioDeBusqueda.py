import GeneradorDatosIniciales
from Modelos.BinarioEscena import  ArbolBinarioBusqueda as arbolEscena
from Modelos.BinarioParte import ArbolBinarioBusqueda as arbolParte
import time
import matplotlib.pyplot as plt

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(160)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 3)

## SOLUCION 1

#print("Solucion 1")

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
arbolParte1.insertarPartes(parte1)

for i in arbolParte1.inorder_traversal():
    print(i)

print("Grandeza parte1")
print(arbolParte1.sumar())

print("PromedioParte1")
print(arbolParte1.promedio())



"""
## SOLUCION 1

print("Solucion 1")

espectaculo = []
for parte in ESPECTACULO:
    part = []
    for escena in parte:
        arbolEscena1 = arbolEscena()
        arbolEscena1.insertarAnimales(escena)
        escenaObjeto = escenaRojiNegro(arbolEscena1)
        part.append(escenaObjeto)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    parteObjeto = parteRojiNegro(arbolParte1)
    espectaculo.append(parteObjeto)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)
espectaculoObjeto = EspectaculoRojiNegro(arbolEspectaculo1)

espectaculoOrdenado = espectaculoObjeto.partes.inOrderEspectaculo()

print("Espectaculo")
for i in espectaculoOrdenado:
    print(i)

print("Escena mas grande")
print(espectaculoObjeto.maxEscena)
print("Escena mas pequeña")
print(espectaculoObjeto.minEscena)
print("Promedio grandeza espectaculo")
print(espectaculoObjeto.promedio)

"""
