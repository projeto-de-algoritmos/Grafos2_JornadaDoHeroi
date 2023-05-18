class Grafo:
    def __init__(self):
        self.graph = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, peso))
        self.graph[v].append((u, peso))
