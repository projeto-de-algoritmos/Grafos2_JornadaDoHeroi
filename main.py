from dijkstra import Grafo
import os

def limpar_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

limpar_terminal()

grafo = Grafo()

grafo.adicionar_aresta('Eldoria', 'Drakonheim', 13)
grafo.adicionar_aresta('Eldoria', 'Mythosia', 25)
grafo.adicionar_aresta('Mythosia', 'Eldoria', 25)
grafo.adicionar_aresta('Mythosia', 'Avaloria', 30)
grafo.adicionar_aresta('Avaloria', 'Mythosia', 30)
grafo.adicionar_aresta('Avaloria', 'Vale Verdejante', 9)
grafo.adicionar_aresta('Avaloria', 'Stormgate', 9)
grafo.adicionar_aresta('Serendell', 'Drakonheim', 4.5)
grafo.adicionar_aresta('Drakonheim', 'Serendell', 4.5)
grafo.adicionar_aresta('Drakonheim', 'Celestia', 7)
grafo.adicionar_aresta('Drakonheim', 'Eldoria', 13)
grafo.adicionar_aresta('Sylvanor', 'Frostholm', 5)
grafo.adicionar_aresta('Frostholm', 'Sylvanor', 5)
grafo.adicionar_aresta('Celestia', 'Vale Verdejante', 9)
grafo.adicionar_aresta('Celestia', 'Shadowfen', 4)
grafo.adicionar_aresta('Celestia', 'Drakonheim', 7)
grafo.adicionar_aresta('Celestia', 'Ironhold', 8)
grafo.adicionar_aresta('Shadowfen', 'Celestia', 4)
grafo.adicionar_aresta('Crystalis', 'Stormgate', 5.5)
grafo.adicionar_aresta('Crystalis', 'Emberfall', 2)
grafo.adicionar_aresta('Crystalis', 'Stormgate', 6)
grafo.adicionar_aresta('Crystalis', 'Picos Radiantes', 5)
grafo.adicionar_aresta('Emberfall', 'Crystalis', 2)
grafo.adicionar_aresta('Emberfall', 'Ironhold', 12)
grafo.adicionar_aresta('Stormgate', 'Crystalis', 5.5)
grafo.adicionar_aresta('Stormgate', 'Avaloria', 9)
grafo.adicionar_aresta('Picos Radiantes', 'Crystalis', 5)
grafo.adicionar_aresta('Vale Verdejante', 'Celestia', 9)
grafo.adicionar_aresta('Vale Verdejante', 'Avaloria', 9)
grafo.adicionar_aresta('Ironhold', 'Emberfall', 12)
grafo.adicionar_aresta('Ironhold', 'Celestia', 8)

local_atual = 'Celestia'

print("================================================================================================================================================================")
print(f"Seja bem vindo, ó nobre herói! Eu sou seu parceiro de viagem, o mapa do Mago Dijkstra! meu objetivo é te ajudar e te dizer a menor distância\ne o caminho mais rápido até sua jornarda!")

while True:
    print(f"Você está em {local_atual}, para onde quer ir, nobre guerreiro?")
    vertice_final = input('->Diga a cidade para onde vai: ')
    
    menor_distancia, caminho = grafo.dijkstra(local_atual, vertice_final)

    if(menor_distancia == float('inf')):
        print(f"\n-->Não há caminho entre {local_atual} e {vertice_final}.")

    else:
        local_atual = vertice_final
        print(f"\n-->A menor distância entre {local_atual} e {vertice_final} é: {menor_distancia}Km.")
        caminho_formatado = ' -> '.join(caminho)
        print(caminho_formatado)

    
   
    saida = input("\nDeseja sair (S/N)?: ")
    limpar_terminal()
    if saida.lower() == "s" :
        break

