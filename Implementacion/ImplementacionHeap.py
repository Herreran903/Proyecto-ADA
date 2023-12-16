import GeneradorDatosIniciales
from Estructuras.EspectaculoHeap import EspectaculoHeap
import time
import matplotlib.pyplot as plt

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(160)

#ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 3)

## SOLUCION 1

#print("Solucion 1")
#print(EspectaculoHeap(ESPECTACULO))


## PRUEBAS  DE TIEMPO
x = []
y = []

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 2, 2)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA1: ", tiempo_total)
x.append(2)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 4, 4)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA2: ", tiempo_total)
x.append(4)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 8, 8)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA3: ", tiempo_total)
x.append(8)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 16, 16)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA4: ", tiempo_total)
x.append(16)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 32, 32)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA5: ", tiempo_total)
x.append(32)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 64, 64)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA6: ", tiempo_total)
x.append(64)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 128, 128)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA7: ", tiempo_total)
x.append(128)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 148, 148)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA8: ", tiempo_total)
x.append(148)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 168, 168)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA9: ", tiempo_total)
x.append(168)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 188, 188)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEBA10: ", tiempo_total)
x.append(188)
y.append(tiempo_total)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 208, 208)

inicio_tiempo = time.time()
EspectaculoHeap(ESPECTACULO)
fin_tiempo = time.time()

tiempo_total = fin_tiempo - inicio_tiempo
print("PRUEB11: ", tiempo_total)
x.append(208)
y.append(tiempo_total)



