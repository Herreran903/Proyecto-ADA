from Modelos.Animal import Animal
from Modelos.BinarioEscena import  ArbolBinarioBusqueda as arbolEscena
class Nodo:
    def __init__(self, llave, valor):
        self.llave = llave
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return f"escena:\n{self.valor}"

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def __str__(self):
        orden_Str = "".join(str(escena) for escena in self.inorder_traversal())
        return f"{orden_Str}"

    def insertar(self, escena:arbolEscena):
        self.raiz = self._insertar(self.raiz, escena)

    def _insertar(self, nodo, escena: arbolEscena):
        if nodo is None:
            return Nodo(escena.suma(), escena)

        if escena.suma() < nodo.llave:
            nodo.izquierda = self._insertar(nodo.izquierda, escena)
        elif escena.suma() == nodo.llave:
            if nodo.valor.suma() < escena.suma():
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

    def encontrar_minimo(self):
        if self.raiz is None:
            return None

        nodo_actual = self.raiz
        while nodo_actual.izquierda:
            nodo_actual = nodo_actual.izquierda

        return nodo_actual

    def sumar(self):
        return self._sumar_llaves(self.raiz)

    def _sumar_llaves(self, nodo):
        if nodo is None:
            return 0

        suma_izquierda = self._sumar_llaves(nodo.izquierda)
        suma_derecha = self._sumar_llaves(nodo.derecha)

        return nodo.llave + suma_izquierda + suma_derecha

    def promedio(self):
        suma_llaves, cantidad_nodos = self._calcular_promedio(self.raiz)

        if cantidad_nodos == 0:
            return None
        else:
            return suma_llaves / cantidad_nodos

    def _calcular_promedio(self, nodo):
        if nodo is None:
            return 0, 0

        suma_izquierda, cantidad_izquierda = self._calcular_promedio(nodo.izquierda)
        suma_derecha, cantidad_derecha = self._calcular_promedio(nodo.derecha)

        suma_total = nodo.llave + suma_izquierda + suma_derecha
        cantidad_total = 1 + cantidad_izquierda + cantidad_derecha

        return suma_total, cantidad_total

    def insertarPartes(self, arbolEscena: list[arbolEscena]):
        for escena in arbolEscena:
            self.insertar(escena)

    def inorder_traversal(self):
        elementos = []
        self._inorder_traversal(self.raiz, elementos)
        return elementos

    def _inorder_traversal(self, nodo, elementos):
        if nodo:
            self._inorder_traversal(nodo.izquierda, elementos)
            elementos.append(nodo)
            self._inorder_traversal(nodo.derecha, elementos)

