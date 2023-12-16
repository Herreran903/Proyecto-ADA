import GeneradorDatosIniciales
from Modelos.RojiNegroEscena import  ArbolRojoNegro as arbolEscena
from Modelos.RojiNegroParte import  ArbolRojoNegro as arbolParte
from Modelos.RojiNegroEspectaculo import  ArbolRojoNegro as arbolEspectaculo
from Estructuras.EscenaRojiNegro import EscenaRojinegro as escenaRojiNegro
from Estructuras.ParteRojiNegro import ParteRojiNegro as parteRojiNegro
from Estructuras.EspectaculoRojiNegro import EspectaculoRojiNegro as EspectaculoRojiNegro


ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(15)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 3)

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