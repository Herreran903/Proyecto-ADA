from Modelos.BinarioParte import  ArbolBinarioBusqueda as arbolParte
class Nodo:
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return f"parte: {self.llave} \n{self.valor}"

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def __str__(self):
        orden_Str = "".join(str(parte) for parte in self.inOrderEspectaculo())
        return f"{orden_Str}"

    def insertar(self, escena: arbolParte):
        self.raiz = self._insertar(self.raiz, escena)

    def _insertar(self, nodo, escena: arbolParte):
        if nodo is None:
            return Nodo(escena.sumar(), escena)

        if escena.sumar() < nodo.llave:
            nodo.izquierda = self._insertar(nodo.izquierda, escena)
        elif escena.sumar() == nodo.llave:
            if nodo.valor.suma() < escena.sumar():
                nodo.izquierda = self._insertar(nodo.izquierda, escena)
            else:
                nodo.derecha = self._insertar(nodo.derecha, escena)
        else:
            nodo.derecha = self._insertar(nodo.derecha, escena)

        return nodo
    def encontrar_maximo(self):
        if self.raiz is None:
            return None

        nodo_actual = self.raiz
        while nodo_actual.derecha:
            nodo_actual = nodo_actual.derecha

        return nodo_actual

    def insertarPartes(self, arbolParte: list[arbolParte]):
        for parte in arbolParte:
            self.insertar(parte)

    def inOrderEspectaculo(self):
        list = self.inorder_traversal()
        n = len(list)
        espectaculo = list[n-1]
        list.pop()
        list.insert(0, espectaculo)

        return list
    def inorder_traversal(self):
        elementos = []
        self._inorder_traversal(self.raiz, elementos)
        return elementos

    def _inorder_traversal(self, nodo, elementos):
        if nodo:
            self._inorder_traversal(nodo.izquierda, elementos)
            elementos.append(nodo)
            self._inorder_traversal(nodo.derecha, elementos)

