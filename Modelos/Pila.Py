from Modelos.Animal import Animal

class Pila:
    def __init__(self, items: list[Animal]):
        self.items = items

    def isEmpty(self):
        return self.items == []

    def pushItem(self, item):
        self.items.append(item)

    def popItem(self):
        return self.items.pop()

    def lenght(self):
        return len(self.items)

    def getGrandeza(self):
        return self.items[0].grandeza + self.items[1].grandeza + self.items[2].grandeza
    
    def maxGrandeza(self):
        return max(self.items[0].grandeza , self.items[1].grandeza , self.items[2].grandeza)