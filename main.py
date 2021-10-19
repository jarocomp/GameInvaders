import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space invaders")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('ship.png')
playerX =370
playerY = 480

def player(x,y):
    screen.blit(playerImg, (playerX, playerY))

# Game loop
running =  True
while running:
    screen.fill((0,0,0))
    playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()

