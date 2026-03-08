"""
Ejercicio 5 y 6:
- Aplicar A* pesado con heurística Manhattan para el 8-puzzle.
- Comparar número de nodos expandidos para pesos 0, 0.8 y 1.

Definición usada de A* pesado:
    f(n) = (1 - w) * g(n) + w * h(n)
"""

from heapq import heappop, heappush


class EightPuzzle:
    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo

    def encontrar_vacio(self, estado):
        return estado.index(0)

    def acciones(self, estado):
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
        acciones = []

        while nodo["padre"] is not None:
            acciones.append(nodo["accion"])
            nodo = nodo["padre"]

        acciones.reverse()
        return acciones

    def distancia_manhattan(self, estado):
        distancia = 0
        for indice, valor in enumerate(estado):
            if valor == 0:
                continue

            fila_actual = indice // 3
            columna_actual = indice % 3

            indice_objetivo = self.estado_objetivo.index(valor)
            fila_objetivo = indice_objetivo // 3
            columna_objetivo = indice_objetivo % 3

            distancia += abs(fila_actual - fila_objetivo) + abs(columna_actual - columna_objetivo)

        return distancia

    def a_estrella_pesado(self, peso):
        if not 0 <= peso <= 1:
            raise ValueError("El peso debe estar entre 0 y 1.")

        nodo_inicial = {
            "estado": self.estado_inicial,
            "padre": None,
            "accion": None,
            "g": 0,
        }

        frontera = []
        contador = 0

        h_inicial = self.distancia_manhattan(self.estado_inicial)
        f_inicial = (1 - peso) * 0 + peso * h_inicial
        heappush(frontera, (f_inicial, h_inicial, contador, nodo_inicial))

        mejor_costo_g = {self.estado_inicial: 0}
        nodos_expandidos = 0

        while frontera:
            _, _, _, nodo_actual = heappop(frontera)
            estado_actual = nodo_actual["estado"]
            g_actual = nodo_actual["g"]

            if g_actual > mejor_costo_g.get(estado_actual, float("inf")):
                continue

            if estado_actual == self.estado_objetivo:
                return self.reconstruir_camino(nodo_actual), nodos_expandidos

            nodos_expandidos += 1

            for accion in self.acciones(estado_actual):
                sucesor = self.resultado(estado_actual, accion)
                nuevo_g = g_actual + 1

                if nuevo_g < mejor_costo_g.get(sucesor, float("inf")):
                    mejor_costo_g[sucesor] = nuevo_g

                    h_sucesor = self.distancia_manhattan(sucesor)
                    f_sucesor = (1 - peso) * nuevo_g + peso * h_sucesor

                    contador += 1
                    nuevo_nodo = {
                        "estado": sucesor,
                        "padre": nodo_actual,
                        "accion": accion,
                        "g": nuevo_g,
                    }
                    heappush(frontera, (f_sucesor, h_sucesor, contador, nuevo_nodo))

        return None, nodos_expandidos


def main():
    estado_inicial = (
        5, 4, 2,
        3, 1, 7,
        0, 6, 8,
    )

    estado_objetivo = (
        1, 2, 3,
        4, 5, 6,
        7, 8, 0,
    )

    problema = EightPuzzle(estado_inicial, estado_objetivo)
    pesos = [0, 0.8, 1]

    resultados = []

    print("Ejercicio 5: A* pesado + Manhattan")
    for peso in pesos:
        solucion, nodos_expandidos = problema.a_estrella_pesado(peso)
        resultados.append((peso, solucion, nodos_expandidos))

        print(f"\nPeso w = {peso}")
        print(f"Nodos expandidos: {nodos_expandidos}")

        if solucion is None:
            print("No se encontró solución.")
        else:
            print(f"Longitud de la solución: {len(solucion)}")
            print(f"Acciones: {solucion}")

    print("\nEjercicio 6: Comparación de nodos expandidos")
    for peso, _, nodos_expandidos in resultados:
        print(f"w = {peso}: {nodos_expandidos} nodos")

    mejor = min(resultados, key=lambda x: x[2])
    print(f"\nMenor cantidad de nodos expandidos: w = {mejor[0]} ({mejor[2]} nodos)")


if __name__ == "__main__":
    main()
