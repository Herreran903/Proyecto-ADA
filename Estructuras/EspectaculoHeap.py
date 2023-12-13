from Modelos.Animal import Animal
from Estructuras.EscenarioHeap import EscenarioHeap
from Estructuras.ParteHeap import ParteHeap


class EspectaculoHeap:

    def __init__(self, heap: list[list[list[Animal]]]):
        self.heap = heap
        self.maxEscenario = None
        self.minEscenario = None
        self.prom = None
        self.construirZoologicoHeap()

    def construirZoologicoHeap(self):

        for i in range(len(self.heap)):
            for j in range(len(self.heap[i])):
                self.heap[i][j] = EscenarioHeap(self.heap[i][j])

        for i in range(len(self.heap)):
            self.heap[i] = ParteHeap(self.heap[i])

        self.buildHeap()

        self.maxEscenario = self.heap[0].maxHeap()
        self.minEscenario = self.heap[0].minHeap()

        self.prom = self.promedio()

        return self

    def ordenarZoologico(self):

        for parte in self.heap:
            for escenario in parte.getHeap():
                print("ESCENARIOOOOOOOOOOOOOOO",escenario)
                escenario.heapSort()
                print("2ESCENARIOOOOOOOOOOOOOOO",escenario)

        for parte in self.heap:
            parte.heapSort()

        self.heapSort(1)

        return self


    def __str__(self):
        heap_str = ", ".join(str(escenario) for escenario in self.heap)
        maxmin_str = f"Maximo: {self.maxEscenario} \n Minimo: {self.minEscenario}"
        promedio_str = f"Promedio: {self.prom}"
        return f"  \n EspectaculoHeap: {heap_str} \n {maxmin_str} \n {promedio_str}"

    def getHeap(self):
        return self.heap

    def heapify(self, n, i,):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and self.heap[izquierda].grandezaTotal > self.heap[mayor].grandezaTotal:
            mayor = izquierda

        if derecha < n and self.heap[derecha].grandezaTotal > self.heap[mayor].grandezaTotal:
            mayor = derecha

        if mayor != i:
            self.heap[i], self.heap[mayor] = self.heap[mayor], self.heap[i]
            self.heapify(n, mayor)

    def buildHeap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        return self

    def heapSort(self, start_index=0):
        n = len(self.heap)
        for i in range(n - 1, start_index, -1):
            self.heap[i], self.heap[start_index] = self.heap[start_index], self.heap[i]
            self.heapify(i, start_index)
        return self

    def promedio(self):
        promedio = 0
        for parte in self.heap:
            promedio += parte.grandezaTotal
        return promedio / len(self.heap)