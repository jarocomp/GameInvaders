import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space invaders")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)
running =  True
while running:
    for event in pygame.event.get():
        screen.fill((0,0,0))
        pygame.display.update()