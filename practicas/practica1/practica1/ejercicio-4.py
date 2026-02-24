### 4. Compara el numero de nodos expandidos entre el algoritmo de primero en profundidad y primero en amplitud.

# Estado final:
estado_final = (1, 2 ,3,
                4, 5, 6,
                7, 8, 0)

#Simulacion 8-Puzzle:

"""
Implementación del problema del 8-puzzle modelado como: (S, A, T, s0, F, C).
Usando el algoritmo DFS iterativo.
"""
class EightPuzzle:

    def __init__(self,
                 estado_inicial,
                 estado_final):
        """
        s0 -> estado_inicial
        F  -> estado_final
        """
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final


    # Devuelve el índice donde se encuentra el 0.
    def encontrar_vacio(self,
                        estado):
        return estado.index(0)


    # Devuelve una lista de acciones válidas desde el estado dado.
    def acciones(self,
                 estado):
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

    
    # Devuelve el nuevo estado después de aplicar la acción.
    def resultado(self,
                  estado,
                  accion):
        """
        Función de transición: Lógica del movimiento, si el vacío está en el índice i:
          "arriba" -> intercambia con i-3
          "abajo" -> intercambia con i+3
          "izquierda" -> intercambia con i-1
          "derecha" -> intercambia con i + 1
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
            nuevo_estado[indice]
        )

        return tuple(nuevo_estado)


    # Reconstruye la secuencia de acciones desde el nodo meta hasta el nodo inicial usando los padres.
    def reconstruir_camino(self,
                           nodo):
        acciones = []

        while nodo["padre"] is not None:
            acciones.append(nodo["accion"])
            nodo = nodo["padre"]

        acciones.reverse()
        return acciones


    # Búsqueda en profundidad iterativa. Devuelve la lista de acciones si encuentra solución.
    def dfs(self):
        nodo_inicial = {
            "estado": self.estado_inicial,
            "padre": None,
            "accion": None
        }
        
        pila = [nodo_inicial]
        visitados = set()
        nodos_expandidos = 0
        
        while pila:
            nodo = pila.pop()
            estado = nodo["estado"]
            
            if estado == self.estado_final:
                return self.reconstruir_camino(nodo), nodos_expandidos
            
            if estado not in visitados:
                visitados.add(estado)
                nodos_expandidos += 1
                for accion in self.acciones(estado):
                    sucesor = self.resultado(estado, accion)
                    nuevo_nodo = {
                        "estado": sucesor,
                        "padre": nodo,
                        "accion": accion
                    }
                    pila.append(nuevo_nodo)
                    
        return None

    # Búsqueda en amplitud iterativa. Devuelve la lista de acciones si encuentra solución.
    def bfs(self):
        nodo_inicial = {
            "estado": self.estado_inicial,
            "padre": None,
            "accion": None
        }
        
        cola = [nodo_inicial]
        visitados = set()
        nodos_expandidos = 0
        
        while cola:
            nodo = cola.pop(0)
            estado = nodo["estado"]
            
            if estado == self.estado_final:
                return self.reconstruir_camino(nodo), nodos_expandidos
            
            if estado not in visitados:
                visitados.add(estado)
                nodos_expandidos += 1
                for accion in self.acciones(estado):
                    sucesor = self.resultado(estado, accion)
                    nuevo_nodo = {
                        "estado": sucesor,
                        "padre": nodo,
                        "accion": accion
                    }
                    cola.append(nuevo_nodo)
                    
        return None



estado_inicial = (1, 0, 2,
                  6, 3, 4,
                  7, 5, 8)

problema = EightPuzzle(estado_inicial, estado_final)

solucion1 = problema.dfs()
solucion2 = problema.bfs()

print("Solution DFS:", solucion1, "\n")
print("Solution BFS:", solucion2, "\n")


# Para DFS (profundidad), los nodos expandidos fueron:
#  Solution DFS: ([...], 143186)

# Mientras que para BFS (amplitud), los nodos expandidos fueron:

# Solution BFS: (['derecha', 'abajo', 'izquierda', 'izquierda', 'arriba', 'derecha', 'derecha', 'abajo', 'izquierda', 'arriba', 'izquierda', 'abajo', 'derecha', 'abajo', 'derecha'], 8350)


# Lo que refleja el funcionamiento de DFS y BFS, dadoque expandir nodos por profundidad puede derivar en pasos innecesarios que realentizan la solucion.
