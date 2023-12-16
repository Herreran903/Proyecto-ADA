
from Estructuras.EspectaculoPila import EspectaculoPila
from Modelos.Metodos import generarAnimalesAlAzar

animales = generarAnimalesAlAzar(10)

espectaculo = EspectaculoPila(animales, 3, 2)
espectaculo.generar_espectaculo_al_azar()
espectaculo.mostrar_espectaculo()

datos_espectaculo = espectaculo.obtener_datos_espectaculo()
print("Datos del Espectáculo:")
print(f"Animal más participante: {datos_espectaculo['animal_mas_participacion']}")
print(f"Animal menos participante: {datos_espectaculo['animal_menos_participacion']}")
print(f"Menor grandeza total: {datos_espectaculo['menor_grandeza_total']}")
print(f"Mayor grandeza total: {datos_espectaculo['mayor_grandeza_total']}")
print(f"Promedio de grandeza: {datos_espectaculo['promedio_grandeza']}")
