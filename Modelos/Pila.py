from Modelos.Animal import Animal
import copy

class Pila:
    def __init__(self, max):
        self.max = max
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pushItem(self, item):
        if len(self.items) == self.max:
            raise Exception("La pila esta llena")
        else:
            self.items.append(item)

    def popItem(self):
        if self.isEmpty():
            raise Exception("La pila esta vacia")
        else:
            return self.items.pop()

    def length(self):
        return len(self.items)
    
    def insert(pila, animales: list[Animal]):

        if len(animales) > pila.max:
            raise Exception("El tamaño de la pila es menor al tamaño de la lista")
        else:
            for i in range(len(animales)):
                pila.pushItem(animales[i])

        return pila
    
    def mayorGrandeza(self):
        if self.isEmpty():
            raise Exception("La pila esta vacia")
        else:
            auxpila = copy.deepcopy(self)
            max = 0
            while not auxpila.isEmpty():
                aux = auxpila.popItem()
                if aux.grandeza > max:
                    max = aux.grandeza
            
            return max
    
    def GrandezaTotal(self):
        if self.isEmpty():
            raise Exception("La pila esta vacia")
        else:
            auxpila = copy.deepcopy(self)
            total = 0
            while not auxpila.isEmpty():
                aux = auxpila.popItem()
                total += aux.grandeza
            
            return total