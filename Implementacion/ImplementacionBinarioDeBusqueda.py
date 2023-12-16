import GeneradorDatosIniciales
from Modelos.BinarioEscena import  ArbolBinarioBusqueda as arbolEscena
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
