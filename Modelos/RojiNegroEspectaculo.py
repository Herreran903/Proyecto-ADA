from Estructuras.ParteRojiNegro import ParteRojiNegro
class Nodo:

    def __init__ (self, clave, valor, color, izquierda = None, derecha = None, padre = None):
        self.clave = clave
        self.valor = valor
        self.color = color
        self.izquierda = izquierda
        self.derecha = derecha
        self.padre = padre

    def __str__(self):
        return f"(Grandeza Parte: {self.clave} \n{self.valor} )"

class ArbolRojoNegro:
    def __init__(self):
        self.NIL = Nodo(None, None, 'NEGRO')  # Nodo nulo
        self.raiz = self.NIL

    def insertar(self, parte: ParteRojiNegro):
        nuevo_nodo = Nodo(parte.grandeza, parte, 'ROJO', self.NIL, self.NIL, self.NIL)
        self._insertar_nodo(nuevo_nodo)
        self._reparar_insercion(nuevo_nodo)

    def _insertar_nodo(self, nuevo_nodo):
        nodo_actual = self.raiz
        nodo_anterior = self.NIL

        while nodo_actual != self.NIL:
            nodo_anterior = nodo_actual
            if nuevo_nodo.clave < nodo_actual.clave:
                nodo_actual = nodo_actual.izquierda

            elif nuevo_nodo.clave == nodo_actual.clave:

                if nodo_actual.valor.maxEscena.clave < nodo_anterior.valor.maxEscena.clave:
                    nodo_actual = nodo_actual.izquierda

                else:
                    nodo_actual = nodo_actual.derecha

            else:
                nodo_actual = nodo_actual.derecha

        nuevo_nodo.padre = nodo_anterior

        if nodo_anterior == self.NIL:
            self.raiz = nuevo_nodo
        elif nuevo_nodo.clave < nodo_anterior.clave:
            nodo_anterior.izquierda = nuevo_nodo
        else:
            nodo_anterior.derecha = nuevo_nodo

    def _reparar_insercion(self, nodo):
        while nodo.padre.color == 'ROJO':
            if nodo.padre == nodo.padre.padre.izquierda:
                tio = nodo.padre.padre.derecha
                if tio.color == 'ROJO':
                    nodo.padre.color = 'NEGRO'
                    tio.color = 'NEGRO'
                    nodo.padre.padre.color = 'ROJO'
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecha:
                        nodo = nodo.padre
                        self._rotar_izquierda(nodo)
                    nodo.padre.color = 'NEGRO'
                    nodo.padre.padre.color = 'ROJO'
                    self._rotar_derecha(nodo.padre.padre)
            else:
                tio = nodo.padre.padre.izquierda
                if tio.color == 'ROJO':
                    nodo.padre.color = 'NEGRO'
                    tio.color = 'NEGRO'
                    nodo.padre.padre.color = 'ROJO'
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:
                        nodo = nodo.padre
                        self._rotar_derecha(nodo)
                    nodo.padre.color = 'NEGRO'
                    nodo.padre.padre.color = 'ROJO'
                    self._rotar_izquierda(nodo.padre.padre)

        self.raiz.color = 'NEGRO'

    def _rotar_izquierda(self, nodo):
        hijo_derecha = nodo.derecha
        nodo.derecha = hijo_derecha.izquierda
        if hijo_derecha.izquierda != self.NIL:
            hijo_derecha.izquierda.padre = nodo
        hijo_derecha.padre = nodo.padre
        if nodo.padre == self.NIL:
            self.raiz = hijo_derecha
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = hijo_derecha
        else:
            nodo.padre.derecha = hijo_derecha
        hijo_derecha.izquierda = nodo
        nodo.padre = hijo_derecha

    def _rotar_derecha(self, nodo):
        hijo_izquierda = nodo.izquierda
        nodo.izquierda = hijo_izquierda.derecha
        if hijo_izquierda.derecha != self.NIL:
            hijo_izquierda.derecha.padre = nodo
        hijo_izquierda.padre = nodo.padre
        if nodo.padre == self.NIL:
            self.raiz = hijo_izquierda
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = hijo_izquierda
        else:
            nodo.padre.derecha = hijo_izquierda
        hijo_izquierda.derecha = nodo
        nodo.padre = hijo_izquierda

    def lenght(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo == self.NIL:
            return 0

        return 1 + self.lenght(nodo.izquierda) + self.lenght(nodo.derecha)

    def min(self):
        if self.raiz == self.NIL:
            return None  # Árbol vacío
        nodo_actual = self.raiz
        while nodo_actual.izquierda != self.NIL:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def max(self):
        if self.raiz == self.NIL:
            return None  # Árbol vacío
        nodo_actual = self.raiz
        while nodo_actual.derecha != self.NIL:
            nodo_actual = nodo_actual.derecha
        return nodo_actual

    def inOrderEspectaculo(self):
        list = self.inOrder()
        n = len(list)
        espectaculo = list[n-1]
        list.pop()
        list.insert(0, espectaculo)

        return list


    def inOrder(self):
        """
        Retorna una lista con los nodos del árbol en orden ascendente.
        """
        nodes_list = []
        if self.raiz == self.NIL:
            return nodes_list
        else:
            self.inOrderAux(self.raiz, nodes_list)
            return nodes_list

    def inOrderAux(self, nodo, nodes_list):
        """
        Método auxiliar para realizar el recorrido in-order y agregar los nodos a la lista.
        """
        if nodo != self.NIL:
            # Recorrer el subárbol izquierdo
            self.inOrderAux(nodo.izquierda, nodes_list)

            # Agregar el nodo actual a la lista
            nodes_list.append(nodo)

            # Recorrer el subárbol derecho
            self.inOrderAux(nodo.derecha, nodes_list)

    def insertarPartes(self, partes: list[ParteRojiNegro]):
        for parte in partes:
            self.insertar(parte)