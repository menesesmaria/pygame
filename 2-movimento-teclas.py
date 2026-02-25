import pygame

pygame.init()

largura, altura = 500, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimento em computação gráfica")

branco = (255, 255, 255)
azul = (0, 0, 255)

x, y = 250, 250
velocidade = 5

executando = True

while executando:
    tela.fill(branco)
    pygame.draw.circle(tela, azul, (x, y), 20)

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade  
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()