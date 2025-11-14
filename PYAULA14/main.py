# Example file showing a basic pygame "game loop"
import pygame

pygame.init() 
tela = pygame.display.set_mode((300,200))
pygame.display.set_caption('titulo')
run = True

while run: 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    tela.fill('purple')
    pygame.draw.rect(tela,'white',(140,95,30,30)) #onde vai estar o retangulo nos eixos x e y
    pygame.draw.ellipse(tela,'black',(120,125,30,30))
    pygame.draw.circle(tela, 'yellow', (100, 65), 30)
    pygame.display.flip()

pygame.quit()

