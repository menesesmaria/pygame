import pygame
import sys

pygame.init()

largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Quadrado com Pygame")

branco = (255, 255, 255)
azul = (0, 0, 255)

x = 250
y = 150
tamanho = 100

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    tela.fill(branco)

    pygame.draw.rect(tela, azul, (x, y, tamanho, tamanho))

    pygame.display.update()