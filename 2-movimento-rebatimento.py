import pygame

pygame.init()

largura, altura = 500, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimento em computação gráfica")

branco = (255, 255, 255)
azul = (0, 0, 255)

x, y = 250, 250
velocidade_x = 5
velocidade_y = 5
raio = 20

executando = True

while executando:
    tela.fill(branco)
    pygame.draw.circle(tela, azul, (x, y), raio)

    x += velocidade_x
    y += velocidade_y

    if x + raio > largura or x - raio < 0:
        velocidade_x = -velocidade_x
    if y + raio >= altura or y - raio < 0:
        velocidade_y = -velocidade_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()