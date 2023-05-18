from dijkstra import Grafo
import os

def limpar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

limpar_terminal()

grafo = Grafo()
grafo.graph = {
    1: {5: 13, 2: 25},
    2: {1: 25, 3: 30},
    3: {2: 30, 14: 9, 12: 9},
    4: {5: 4.5},
    5: {4: 4.5, 8: 7, 1: 13},
    6: {7: 5},
    7: {6: 5},
    8: {14: 9, 9: 4, 5: 7, 15: 8},
    9: {8: 4},
    10: {12: 5.5, 11: 2, 16: 6, 13: 5},
    11: {10: 2, 15: 12},
    12: {10: 5.5, 3: 9},
    13: {10: 5},
    14: {8: 9, 3: 9},
    15: {11: 12, 8: 8}
}
while True:
    vertice_inicial = int(input('\n\n->Diga a cidade em que está: '))
    
    vertice_final = int(input('->Diga a cidade para onde vai: '))
    
    menor_distancia = grafo.dijkstra(vertice_inicial, vertice_final)

    if(menor_distancia == float('inf')):
        print(f"\n-->Não há caminho entre {vertice_inicial} e {vertice_final}.")

    else:
        print(f"\n-->A menor distância entre {vertice_inicial} e {vertice_final} é: {menor_distancia}Km.")

    saida = input("Deseja sair (S/N)?: ")
    limpar_terminal()
    if saida.lower() == "s" :
        break

'''
n = int(input("Digite o número de arestas:"))
for i in range(n):
    v1 = input("valor do vértice 1: ")
    v2 = input("valor do vértice 2: ")
    p = input("valor do peso:")
    grafo.adicionar_aresta(v1, v2, p)

for vertice in grafo.graph:
    print(f"{vertice}:")
    for vizinho, peso in grafo.graph{vertice}:
        print(f"  Vizinho: {vizinho} - Peso: {peso}")'''