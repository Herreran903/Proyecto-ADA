import GeneradorDatosIniciales
from Estructuras.EspectaculoHeap import EspectaculoHeap

ANIMALES = GeneradorDatosIniciales.generarAnimalesAlAzar(9)

ESPECTACULO = GeneradorDatosIniciales.generarEspectaculoAlAzar(ANIMALES, 3, 2)

## SOLUCION 1

print("Solucion 1")
print(EspectaculoHeap(ESPECTACULO))
