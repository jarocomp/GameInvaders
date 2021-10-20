import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space invaders")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('ship.png')
playerX =370
playerY = 480
playerX_change = 0


# Enemy

enemyImg = pygame.image.load('invader.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 40

def player(x,y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

# Game loop
running =  True
while running:
    screen.fill((0,0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check of pressed key

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.1

        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    playerX += playerX_change

    # boundary for ship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    # boundary for enemy
    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

