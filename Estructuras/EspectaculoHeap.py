from Modelos.Animal import Animal
from Estructuras.EscenarioHeap import EscenarioHeap
from Estructuras.ParteHeap import ParteHeap


class EspectaculoHeap:

    def __init__(self, heap: list[list[list[Animal]]]):
        self.heap = heap
        self.construirZoologicoHeap()

    # def construirZoologicoHeap(self):


    def __str__(self):
        heap_str = ", ".join(str(escenario) for escenario in self.lista)
        return f"  \n EspectaculoHeap: {heap_str}"

    def getHeap(self):
        return self.lista

    def heapify(self, n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and self.lista[izquierda].grandezaTotal > self.lista[mayor].grandezaTotal:
            mayor = izquierda

        if derecha < n and self.lista[derecha].grandezaTotal > self.lista[mayor].grandezaTotal:
            mayor = derecha

        if mayor != i:
            self.lista[i], self.lista[mayor] = self.lista[mayor], self.lista[i]
            self.heapify(n, mayor)

    def buildHeap(self):
        n = len(self.lista)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        return self

    def heapSort(self):
        n = len(self.lista)
        for i in range(n - 1, 0, -1):
            self.lista[i], self.lista[0] = self.lista[0], self.lista[i]
            self.heapify(i, 0)
        return self
