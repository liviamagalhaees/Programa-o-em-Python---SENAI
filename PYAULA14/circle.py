import pygame
pygame.init()
tela = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tela.fill((0, 0, 0))
    pygame.draw.circle(tela, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()
pygame.quit()