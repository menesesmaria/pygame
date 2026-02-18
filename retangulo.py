import pygame
import sys

pygame.init()

largura = 800
altura = 800

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Retangulo")

branco = (255, 255, 255)
vermelho = (255, 0, 0)

x = 200
y = 150
largura_ret = 200
altura_ret = 100

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(branco)

    pygame.draw.rect(tela, vermelho, (x, y, largura, altura))

    pygame.display.update()