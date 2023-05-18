from dijkstra import Grafo
import os

def limpar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

limpar_terminal()
grafo = Grafo()
grafo.adicionar_aresta('A', 'B', 2)
grafo.adicionar_aresta('A', 'C', 4)
grafo.adicionar_aresta('B', 'C', 3)

vertice_inicial = 'A'
vertice_final = 'C'
menor_distancia = grafo.dijkstra(vertice_inicial, vertice_final)

print(f"A menor distância entre '{vertice_inicial}' e '{vertice_final}' é: {menor_distancia}")



'''
n = int(input("Digite o número de arestas:"))
for i in range(n):
    v1 = input("valor do vértice 1: ")
    v2 = input("valor do vértice 2: ")
    p = input("valor do peso:")
    grafo.adicionar_aresta(v1, v2, p)

for vertice in grafo.graph:
    print(f"{vertice}:")
    for vizinho, peso in grafo.graph[vertice]:
        print(f"  Vizinho: {vizinho} - Peso: {peso}")'''