from Modelos.Animal import Animal
class Nodo:
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return f"{self.valor}"

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def __str__(self):
        return f"{self.inorder_traversal()}"

    def insertar(self, animal:Animal):
        self.raiz = self._insertar(self.raiz, animal)

    def _insertar(self, nodo, animal: Animal):
        if nodo is None:
            return Nodo(animal.grandeza, animal)

        if animal.grandeza < nodo.llave:
            nodo.izquierda = self._insertar(nodo.izquierda, animal)
        elif animal.grandeza > nodo.llave:
            nodo.derecha = self._insertar(nodo.derecha, animal)

        return nodo
    def encontrar_maximo(self):
        if self.raiz is None:
                return None

        nodo_actual = self.raiz
        while nodo_actual.derecha:
            nodo_actual = nodo_actual.derecha

        return nodo_actual

    def encontrar_minimo(self):
        if self.raiz is None:
            return None

        nodo_actual = self.raiz
        while nodo_actual.izquierda:
            nodo_actual = nodo_actual.izquierda

        return nodo_actual

    def suma(self):
        if self.raiz is None:
            return 0  # Árbol vacío
        suma = self.raiz.llave + self.raiz.izquierda.llave + self.raiz.derecha.llave
        return suma

    def insertarAnimales(self, animales: list[Animal]):
        for animal in animales:
            self.insertar(animal)

    def inorder_traversal(self):
        elementos = []
        self._inorder_traversal(self.raiz, elementos)
        return elementos

    def _inorder_traversal(self, nodo, elementos):
        if nodo:
            self._inorder_traversal(nodo.izquierda, elementos)
            elementos.append(nodo)
            self._inorder_traversal(nodo.derecha, elementos)

