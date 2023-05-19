import heapq

class Grafo:
    def __init__(self):
        self.graph = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, peso))

    def dijkstra(self, vertice_inicial, vertice_final):
        distancias = {vertice: float('inf') for vertice in self.graph}
        distancias[vertice_inicial] = 0
        heap = [(0, vertice_inicial)]
        caminho = {vertice_inicial: [vertice_inicial]}

        while heap:
            distancia_atual, vertice_atual = heapq.heappop(heap)

            if vertice_atual == vertice_final:
                return distancia_atual, caminho[vertice_atual]

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.graph[vertice_atual]:
                distancia = distancia_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(heap, (distancia, vizinho))
                    caminho[vizinho] = caminho[vertice_atual] + [vizinho]

        return float('inf'), []