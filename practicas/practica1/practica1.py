En el problema del rompecabezas de 8 piezas (8-puzzle):
*   S: Todas las configuraciones del tablero.
*   A: Mover espacio vacio: arriba/abajo/izquierda/derecha
*   S0: Configuración inicial
*   F: Conjunto de configuraciones finales.
*   T: Intercambiar espacio vacío con pieza adjacente
*   C: Normalmente uniforme. 1 por movimiento.

#### ¿Cómo representar los estados? Aunque visualicemos una matriz de 3x3 no existe ningún impedimento para tener una representación lineal de los estados.

(1,2,3,
 4,0,5,
 6,7,8)


#### Determinar estado inicial y estados finales.

class EightPuzzle:

    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo

#### Definir las acciones. ¿Cómo saber que acciones son válidas en ciertos estados? Necesitamos saber la ubicación del 0.

def encontrar_vacio(self, estado):
    """
    Devuelve el índice donde se encuentra el 0 (espacio vacío)
    """
    return estado.index(0)

# Convertir la representación lineal en filas y columnas. Indicar las acciones válidas según filas y columnas.

def acciones(self, estado):
    """
    Devuelve una lista de acciones válidas desde el estado dado.
    """
    acciones_posibles = []

    indice = self.encontrar_vacio(estado)
    fila = indice // 3
    columna = indice % 3

    # Verificar movimiento arriba
    if fila > 0:
        acciones_posibles.append("arriba")

    # Verificar movimiento abajo
    if fila < 2:
        acciones_posibles.append("abajo")

    # Verificar movimiento izquierda
    if columna > 0:
        acciones_posibles.append("izquierda")

    # Verificar movimiento derecha
    if columna < 2:
        acciones_posibles.append("derecha")

    return acciones_posibles

# Función de transición: Lógica del movimiento, si el vacío está en el índice i:
#    "arriba" -> intercambia con i-3
#    "abajo" -> intercambia con i+3
#    "izquierda" -> intercambia con i-1
#    "derecha" -> intercambia con i + 1

def resultado(self, estado, accion):
    """
    Devuelve el nuevo estado después de aplicar la acción.
    """
    indice = self.encontrar_vacio(estado)

    # Convertimos a lista para poder modificar
    nuevo_estado = list(estado)

    if accion == "arriba":
        intercambio = indice - 3
    elif accion == "abajo":
        intercambio = indice + 3
    elif accion == "izquierda":
        intercambio = indice - 1
    elif accion == "derecha":
        intercambio = indice + 1
    else:
        raise ValueError("Acción inválida")

    # Intercambio
    nuevo_estado[indice], nuevo_estado[intercambio] = (
        nuevo_estado[intercambio],
        nuevo_estado[indice],
    )


    return tuple(nuevo_estado)


# ¿Necesitamos una función de costo? No para los algoritmos de búsqueda desinformada. Pero si necesitamos llevar un registro de los estados visitados.

def dfs(self):
    """
    Búsqueda en profundidad iterativa.
    Devuelve True si encuentra la meta, False si no.
    """

    pila = [self.estado_inicial]
    visitados = set()

    while pila:
        estado = pila.pop()

        if estado == self.estado_objetivo:
            return True

        if estado not in visitados:
            visitados.add(estado)

            for accion in self.acciones(estado):
                sucesor = self.resultado(estado, accion)
                pila.append(sucesor)

    return False


# No es suficiente. Queremos que nos regrese las acciones. Necesitamos una estructura Nodo, de preferencia una clase, pero aquí nos conformaremos con un diccionario.

def dfs(self):
    """
    Búsqueda en profundidad iterativa.
    Devuelve la lista de acciones si encuentra solución.
    """

    nodo_inicial = {
        "estado": self.estado_inicial,
        "padre": None,
        "accion": None
    }

    pila = [nodo_inicial]
    visitados = set()

    while pila:
        nodo = pila.pop()
        estado = nodo["estado"]

        if estado == self.estado_objetivo:
            return self.reconstruir_camino(nodo)

        if estado not in visitados:
            visitados.add(estado)

            for accion in self.acciones(estado):
                sucesor = self.resultado(estado, accion)

                nuevo_nodo = {
                    "estado": sucesor,
                    "padre": nodo,
                    "accion": accion
                }

                pila.append(nuevo_nodo)

    return None


# Con esto podemos reconstruir el camino.

def reconstruir_camino(self, nodo):
    acciones = []

    while nodo["padre"] is not None:
        acciones.append(nodo["accion"])
        nodo = nodo["padre"]

    acciones.reverse()
    return acciones









# Código completo:

class EightPuzzle:
    """
    Implementación del problema del 8-puzzle modelado como:
    (S, A, T, s0, F, C)

    Algoritmo DFS iterativo.
    """

    def __init__(self, estado_inicial, estado_objetivo):
        """
        s0 -> estado_inicial
        F  -> estado_objetivo
        """
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo


    def encontrar_vacio(self, estado):
        """
        Devuelve el índice donde se encuentra el 0.
        Representación lineal:
        0 1 2
        3 4 5
        6 7 8
        """
        return estado.index(0)


    def acciones(self, estado):
        """
        Devuelve una lista de acciones válidas desde el estado dado.
        """
        acciones_posibles = []

        indice = self.encontrar_vacio(estado)
        fila = indice // 3
        columna = indice % 3


        if fila > 0:
            acciones_posibles.append("arriba")


        if fila < 2:
            acciones_posibles.append("abajo")


        if columna > 0:
            acciones_posibles.append("izquierda")


        if columna < 2:
            acciones_posibles.append("derecha")

        return acciones_posibles


    def resultado(self, estado, accion):
        """
        Devuelve el nuevo estado después de aplicar la acción.
        """
        indice = self.encontrar_vacio(estado)
        nuevo_estado = list(estado)

        if accion == "arriba":
            intercambio = indice - 3
        elif accion == "abajo":
            intercambio = indice + 3
        elif accion == "izquierda":
            intercambio = indice - 1
        elif accion == "derecha":
            intercambio = indice + 1
        else:
            raise ValueError("Acción inválida")


        nuevo_estado[indice], nuevo_estado[intercambio] = (
            nuevo_estado[intercambio],
            nuevo_estado[indice],
        )

        return tuple(nuevo_estado)


    def reconstruir_camino(self, nodo):
        """
        Reconstruye la secuencia de acciones desde el nodo meta
        hasta el nodo inicial usando los padres.
        """
        acciones = []

        while nodo["padre"] is not None:
            acciones.append(nodo["accion"])
            nodo = nodo["padre"]

        acciones.reverse()
        return acciones


    def dfs(self):
        """
        Búsqueda en profundidad iterativa.
        Devuelve la lista de acciones si encuentra solución.
        """

        nodo_inicial = {
            "estado": self.estado_inicial,
            "padre": None,
            "accion": None
        }

        pila = [nodo_inicial]
        visitados = set()

        while pila:
            nodo = pila.pop()
            estado = nodo["estado"]


            if estado == self.estado_objetivo:
                return self.reconstruir_camino(nodo)


            if estado not in visitados:
                visitados.add(estado)

                for accion in self.acciones(estado):
                    sucesor = self.resultado(estado, accion)

                    nuevo_nodo = {
                        "estado": sucesor,
                        "padre": nodo,
                        "accion": accion
                    }

                    pila.append(nuevo_nodo)

        return None





estado_inicial = (1,2,3,
                  4,0,5,
                  6,7,8)

estado_objetivo = (1,2,3,
                   4,5,6,
                   7,8,0)

problema = EightPuzzle(estado_inicial, estado_objetivo)

solucion = problema.dfs()

print("Solución:", solucion)



# En la práctica se les pide contar el número de nodos expandidos. ¿Qué se debe agregar para poder obtener esto?
