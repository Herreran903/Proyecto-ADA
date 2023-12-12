from Modelos.Animal import Animal
class EscenarioHeap:
    def __init__(self, heap: list[Animal]):
        self.heap = heap
        self.grandezaTotal = heap[0].grandeza + heap[1].grandeza + heap[2].grandeza

    def __str__(self):
        heap_str = "-".join(str(animal) for animal in self.heap)
        return f" \n EscenarioHeap: \n {heap_str} Grandeza Total: {self.grandezaTotal} \n"
    def getHeap(self):
        return self.heap
    def heapify(self, n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and self.heap[izquierda].grandeza > self.heap[mayor].grandeza:
            mayor = izquierda

        if derecha < n and self.heap[derecha].grandeza > self.heap[mayor].grandeza:
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