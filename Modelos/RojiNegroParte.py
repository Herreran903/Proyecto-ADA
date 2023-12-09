from Estructuras.Escena2 import Escena2
from Modelos.Pila import Pila

from binarytree import build, Node

class RedBlackTreeNode():
    def _init_(self, escena: Pila, color="Rojo"):
        self.clave = escena.GrandezaTotal
        self.valor = escena.maxGrandeza
        self.izquierda = None
        self.derecha = None
        self.padre = None
        self.color = color

class RedBlackTree:
    def _init_(self):
        self.Nil = RedBlackTreeNode(None, None, "Negro")
        self.root = self.Nil

    def insert(self, value: list[Escena2]):
        if not self.root:
            self.root = RedBlackTreeNode(value, 'black')
        else:
            self.root = self._insert(self.root, value)
            self.root.color = 'black'

    def _insert(self, node, value):
        if not node:
            return RedBlackTreeNode(value, 'red')

        # Perform standard BST insert
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # Duplicates are not allowed

        # Fix the tree
        if node.right and node.right.color == 'red':
            if node.left and node.left.color == 'red':
                node.color = 'red'
                node.left.color = 'black'
                node.right.color = 'black'
            else:
                if value > node.right.value:
                    return self._rotate_left(node)
                else:
                    node.right = self._rotate_right(node.right)
                    return self._rotate_left(node)
        elif node.left and node.left.color == 'red':
            if value < node.left.value:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        return node

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        new_root.color, node.color = node.color, 'red'
        return new_root

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        new_root.color, node.color = node.color, 'red'
        return new_root

    def display(self):
        if self.root:
            return self.root

    def maximo(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        while nodo.derecha != self.NIL:
            nodo = nodo.derecha

        return nodo.clave, nodo.valor

    def minimo(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        while nodo.izquierda != self.NIL:
            nodo = nodo.izquierda

        return nodo.clave, nodo.valor

    def delete(self, clave):
        nodo = self._buscar_nodo(clave)
        if nodo is None:
            raise ValueError(f"La clave {clave} no está en el árbol.")
        self._delete_nodo(nodo)

    def _delete_nodo(self, nodo):
        y = nodo
        y_color_original = y.color
        if nodo.izquierda == self.NIL:
            x = nodo.derecha
            self._transplantar(nodo, nodo.derecha)
        elif nodo.derecha == self.NIL:
            x = nodo.izquierda
            self._transplantar(nodo, nodo.izquierda)
        else:
            y = self._encontrar_minimo(nodo.derecha)
            y_color_original = y.color
            x = y.derecha
            if y.padre == nodo:
                x.padre = y
            else:
                self._transplantar(y, y.derecha)
                y.derecha = nodo.derecha
                y.derecha.padre = y
            self._transplantar(nodo, y)
            y.izquierda = nodo.izquierda
            y.izquierda.padre = y
            y.color = nodo.color
        if y_color_original == "Negro":
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x != self.raiz and x.color == "Negro":
            if x == x.padre.izquierda:
                hermano = x.padre.derecha
                if hermano.color == "Rojo":
                    hermano.color = "Negro"
                    x.padre.color = "Rojo"
                    self.rotacion_izquierda(x.padre)
                    hermano = x.padre.derecha
                if hermano.izquierda.color == "Negro" and hermano.derecha.color == "Negro":
                    hermano.color = "Rojo"
                    x = x.padre
                else:
                    if hermano.derecha.color == "Negro":
                        hermano.izquierda.color = "Negro"
                        hermano.color = "Rojo"
                        self.rotacion_derecha(hermano)
                        hermano = x.padre.derecha
                    hermano.color = x.padre.color
                    x.padre.color = "Negro"
                    hermano.derecha.color = "Negro"
                    self.rotacion_izquierda(x.padre)
                    x = self.raiz
            else:
                hermano = x.padre.izquierda
                if hermano.color == "Rojo":
                    hermano.color = "Negro"
                    x.padre.color = "Rojo"
                    self.rotacion_derecha(x.padre)
                    hermano = x.padre.izquierda
                if hermano.derecha.color == "Negro" and hermano.izquierda.color == "Negro":
                    hermano.color = "Rojo"
                    x = x.padre
                else:
                    if hermano.izquierda.color == "Negro":
                        hermano.derecha.color = "Negro"
                        hermano.color = "Rojo"
                        self.rotacion_izquierda(hermano)
                        hermano = x.padre.izquierda
                    hermano.color = x.padre.color
                    x.padre.color = "Negro"
                    hermano.izquierda.color = "Negro"
                    self.rotacion_derecha(x.padre)
                    x = self.raiz
        x.color = "Negro"

    def _transplantar(self, u, v):
        if u.padre == self.NIL:
            self.raiz = v
        elif u == u.padre.izquierda:
            u.padre.izquierda = v
        else:
            u.padre.derecha = v
        v.padre = u.padre

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda != self.NIL:
            nodo = nodo.izquierda
        return nodo

    def _buscar_nodo(self, clave):
        return self._buscar_nodo_recursivo(self.raiz, clave)

    def _buscar_nodo_recursivo(self, nodo, clave):
        if nodo == self.NIL or clave == nodo.clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar_nodo_recursivo(nodo.izquierda, clave)
        return self._buscar_nodo_recursivo(nodo.derecha, clave)

class RojiNegroParte:
    def __init__(self, escenarios: list[Pila]):
        self.escenarios = escenarios
