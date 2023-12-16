import GeneradorDatosIniciales
from Modelos.RojiNegroEscena import  ArbolRojoNegro as arbolEscena
from Modelos.RojiNegroParte import  ArbolRojoNegro as arbolParte
from Modelos.RojiNegroEspectaculo import  ArbolRojoNegro as arbolEspectaculo
from Estructuras.EscenaRojiNegro import EscenaRojinegro as escenaRojiNegro
from Estructuras.ParteRojiNegro import ParteRojiNegro as parteRojiNegro
from Estructuras.EspectaculoRojiNegro import EspectaculoRojiNegro as EspectaculoRojiNegro
import time
import matplotlib.pyplot as plt

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(160)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 3)

## SOLUCION 1

#print("Solucion 1")
#print(EspectaculoHeap(ESPECTACULO))

## PRUEBAS  DE TIEMPO
x = []
y = []

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 2, 2)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA1: ", tiempo_total)
x.append(2*(2*(2-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 4, 4)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA2: ", tiempo_total)
x.append(2*(4*(4-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 8, 8)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA3: ", tiempo_total)
x.append(8)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 16, 16)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA4: ", tiempo_total)
x.append(2*(16*(16-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 32, 32)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA5: ", tiempo_total)
x.append(2*(32*(32-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 64, 64)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA6: ", tiempo_total)
x.append(2*(64*(64-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 128, 128)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA7: ", tiempo_total)
x.append(2*(128*(128-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 148, 148)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA8: ", tiempo_total)
x.append(2*(148*(148-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 168, 168)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA9: ", tiempo_total)
x.append(2*(168*(168-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 188, 188)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA10: ", tiempo_total)
x.append(2*(188*(188-1)))
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 208, 208)

inicio_tiempo = time.time()
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
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEB11: ", tiempo_total)
x.append(2*(208*(208-1)))
y.append(tiempo_total)

plt.plot(x, y)
plt.xlabel('Cantidad de escenarios')
plt.ylabel('Tiempo de ejecucion')
plt.title('Tiempo de ejecucion de la solucion 1')
plt.show()

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
