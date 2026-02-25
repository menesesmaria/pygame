import pygame
import sys

pygame.init()

largura, altura = 500, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimento em computação gráfica")

branco = (255, 255, 255)
azul = (0, 0, 255)

x, y = 250, 250
raio = 20

clock = pygame.time.Clock()
executando = True

while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    tela.fill(branco)
    pygame.draw.circle(tela, azul, (x, y), raio)

    pygame.display.update()
    clock.tick(60)

pygame.quit()



