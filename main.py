from dijkstra import Grafo
import os
import threading
import pygame
from PIL import Image

def show_window(image_path, exit_event):
    # Carrega a imagem
    image = Image.open(image_path)
    image = image.convert("RGB")

    # Obtém as dimensões da imagem
    image_width, image_height = image.size

    # Inicializa o Pygame
    pygame.init()

    # Cria a janela
    window = pygame.display.set_mode((image_width, image_height))
    pygame.display.set_caption("Janela da Imagem")

    # Carrega a imagem no formato do Pygame
    pygame_image = pygame.image.load(image_path)

    # Exibe a imagem na janela
    window.blit(pygame_image, (0, 0))
    pygame.display.flip()

    # Loop principal do Pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if exit_event.is_set():
            running = False

    # Encerra o Pygame
    pygame.quit()

def run_code(image_path):
    show_window(image_path)

exit_event = threading.Event()

# Função para executar o código do Pygame
def run_code(image_path, exit_event):
    show_window(image_path, exit_event)

# Caminho da imagem
image_path = "./mapa.png"

# Cria uma thread para executar o código do Pygame
pygame_thread = threading.Thread(target=run_code, args=(image_path, exit_event))
pygame_thread.start()

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

print("====================================================================================================================================================")
print(f"Seja bem vindo, ó nobre herói! Eu sou seu parceiro de viagem, o mapa do Mago Dijkstra! meu objetivo é te ajudar e te dizer a menor distância\ne o caminho mais rápido até sua jornarda! Vamos sair de Celestia e começar nossa aventura!")
print("====================================================================================================================================================")

while True:
    print(f"\nVocê está em {local_atual}, para onde quer ir, nobre guerreiro?")
    contador = 1
    for vertice in grafo.graph:
        print(f"{contador}.{vertice}")
        contador = contador + 1
    print("\n")

    vertice_final = input('->Diga a cidade para onde nós vamos: ')
    
    menor_distancia, caminho = grafo.dijkstra(local_atual, vertice_final)

    if(menor_distancia == float('inf')):
        print(f"\n-->Não há caminho entre {local_atual} e {vertice_final}. Tente de novo!")

    else:
        local_atual = vertice_final
        caminho_formatado = ' -> '.join(caminho)
        print(caminho_formatado)
        print(f"\n-->A menor distância entre {local_atual} e {vertice_final} é: {menor_distancia}Km. O caminho é {caminho_formatado}. Vamos lá!")
        

    
   
    saida = input("\nDeseja sair (S/N)?: ")
    limpar_terminal()
    if saida.lower() == "s" :
        exit_event.set()
        break

pygame_thread.join()