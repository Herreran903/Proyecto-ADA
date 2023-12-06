import Modelos.Animal
import Modelos.Escenario
import Modelos.Espectaculo
import Modelos.Parte
import Modelos.Metodos
from Modelos import Metodos


def main():
    a = Metodos.generarAnimalesAlAzar(9)
    print(len(a))


main()