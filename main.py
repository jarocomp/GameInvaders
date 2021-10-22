import pygame
import random
import math

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
num_of_enemies = 6

# Enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

# Bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"
score = 0

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY =10

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (0,255,0))
    screen.blit(score, (x,y))

def player(x,y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

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

    # boundary for enemy
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change [i]= 0.1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.1
            enemyY[i] += enemyY_change[i]
        # Colision
        collision = isColision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score)
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(0,150)
        enemy(enemyX[i], enemyY[i], i)
    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

        
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()

