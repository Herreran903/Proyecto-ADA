from Modelos.Animal import Animal

class Pila:
    def __init__(self, items: list[Animal]):
        self.items = items
        self.grandezaTotal = items[0].grandeza + items[1].grandeza + items[2].grandeza
        self.maxGrandeza = max(items).grandeza

    def isEmpty(self):
        return self.items == []

    def pushItem(self, item):
        self.items.append(item)

    def popItem(self):
        return self.items.pop()

    def lenght(self):
        return len(self.items)

    def getGrandeza(self):
        return self.grandezaTotal
    
    def maxGrandeza(self):
        return max(self.items).grandeza