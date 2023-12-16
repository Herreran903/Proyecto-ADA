from Estructuras.EscenarioHeap import EscenarioHeap

class ParteHeap:
    def __init__(self, heap: list[EscenarioHeap]):
        self.heap = heap
        self.grandezaTotal = self.sumarGrandezas()
        self.buildHeap()

    def __str__(self):
        heap_str = ", ".join(str(escenario) for escenario in self.heap)
        return f"  \n ParteHeap: {heap_str} \n Grandeza Total Parte: {self.grandezaTotal}"

    def getHeap(self):
        return self.heap

    def heapify(self, n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2
        if izquierda < n and self.heap[izquierda].grandezaTotal > self.heap[mayor].grandezaTotal:
            mayor = izquierda
        elif izquierda < n and self.heap[izquierda].grandezaTotal == self.heap[mayor].grandezaTotal:
            if self.heap[izquierda].heap[2].grandeza > self.heap[mayor].heap[2].grandeza:
                mayor = izquierda
            elif self.heap[izquierda].heap[2].grandeza == self.heap[mayor].heap[2].grandeza:
                if self.heap[izquierda].heap[1].grandeza > self.heap[mayor].heap[1].grandeza:
                    mayor = izquierda
                elif self.heap[izquierda].heap[1].grandeza == self.heap[mayor].heap[1].grandeza:
                    if self.heap[izquierda].heap[0].grandeza > self.heap[mayor].heap[0].grandeza:
                        mayor = izquierda
        if derecha < n and self.heap[derecha].grandezaTotal > self.heap[mayor].grandezaTotal:
            mayor = derecha
        elif derecha < n and self.heap[derecha].grandezaTotal == self.heap[mayor].grandezaTotal:
            if self.heap[derecha].heap[2].grandeza > self.heap[mayor].heap[2].grandeza:
                mayor = derecha
            elif self.heap[derecha].heap[2].grandeza == self.heap[mayor].heap[2].grandeza:
                if self.heap[derecha].heap[1].grandeza > self.heap[mayor].heap[1].grandeza:
                    mayor = derecha
                elif self.heap[derecha].heap[1].grandeza == self.heap[mayor].heap[1].grandeza:
                    if self.heap[derecha].heap[0].grandeza > self.heap[mayor].heap[0].grandeza:
                        mayor = derecha
        if mayor != i:
            self.heap[i], self.heap[mayor] = self.heap[mayor], self.heap[i]
            self.heapify(n, mayor)

    def buildHeap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)
        return self

    def heapSort(self):
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heapify(i, 0)
        return self

    def sumarGrandezas(self):
        self.grandezaTotal = 0
        for escenario in self.heap:
            self.grandezaTotal += escenario.grandezaTotal
        return self.grandezaTotal

    def maxHeap(self):
        return self.heap[0]

    def minHeap(self):
        minimo = self.heap[0]
        for escena in self.heap:
            if escena.grandezaTotal < minimo.grandezaTotal:
                minimo = escena
        return minimo