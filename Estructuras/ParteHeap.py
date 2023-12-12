from Estructuras.EscenarioHeap import EscenarioHeap


class ParteHeap:
    def __init__(self, heap: list[EscenarioHeap]):
        self.heap = heap


    def __str__(self):
        heap_str = ", ".join(str(escenario) for escenario in self.heap)
        return f"  \n ParteHeap: {heap_str}"

    def getHeap(self):
        return self.heap

    def heapify(self, n, i):
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

    def heapSort(self):
        n = len(self.heap)
        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.heapify(i, 0)