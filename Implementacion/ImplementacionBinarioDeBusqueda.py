import GeneradorDatosIniciales
from Estructuras.BinarioEscena import  ArbolBinarioBusqueda as arbolEscena
from Estructuras.BinarioParte import ArbolBinarioBusqueda as arbolParte
from Estructuras.BinarioEspectaculo import ArbolBinarioBusqueda as arbolEspectaculo
import time
import matplotlib.pyplot as plt

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(160)

"""
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