import GeneradorDatosIniciales
from Estructuras.RojiNegroEscena import  ArbolRojoNegro as arbolEscena
from Estructuras.RojiNegroParte import  ArbolRojoNegro as arbolParte
from Estructuras.RojiNegroEspectaculo import  ArbolRojoNegro as arbolEspectaculo
import time
import matplotlib.pyplot as plt

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(160)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 3)

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
print(arbolEspectaculo1) #imprime el espectaculo ordenado
print("Escena mas grande")
print(arbolEspectaculo1.max().valor.max()) # imprime la escena mas grande
print("Escena mas pequeña")
print(arbolEspectaculo1.max().valor.min()) # imprime la escena mas pequeña
print("Promedio")
print(arbolEspectaculo1.max().valor.promedio()) # imprime el promedio


## SOLUCION 1

"""
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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
        part.append(arbolEscena1)

    arbolParte1 = arbolParte()
    arbolParte1.insertarEscenas(part)
    espectaculo.append(arbolParte1)

arbolEspectaculo1 = arbolEspectaculo()
arbolEspectaculo1.insertarPartes(espectaculo)

espectaculoOrdenado = arbolEspectaculo1.inOrderEspectaculo()
#print(arbolEspectaculo1) #imprime el espectaculo ordenado
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

