import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800,600))
score= 0

pygame.display.set_caption("Space invaders")
icon = pygame.image.load("ship.png")
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('ship.png')
playerX =370
playerY = 480
playerX_change = 0


# Enemy

enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 40

# Bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

def player(x,y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))

def isColision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False


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

        if event.key == pygame.K_ESCAPE:
            if bullet_state == "ready":

                bulletX = playerX
                fire_bullet(playerX, bulletY)


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
    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    #Colision
    collision = isColision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state == "ready"
        score += 1
        print(score)
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

