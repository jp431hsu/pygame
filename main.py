import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
SELECTION = []
SELECTION.append('player.png')
SELECTION.append('tofu.png')
SELECTION.append('chips.png')
SELECTION.append('github.png')


#playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

enemyX = []   #calc random with memory
for i in range(num_of_enemies):
    x = 0
    x = random.randint(0, 736)
    if x not in enemyX:
        enemyX.append(x)

enemyY = []       # same ^
for i in range(num_of_enemies):
    y = 0
    y = random.randint(50, 150)
    if y not in enemyY:
        enemyY.append(y)


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
  #  enemyX.append(random.randint(0, 736))          calc random int, OLD WAY
  #  enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

paused = False    # added for pause
# Game Loop
pngFiles = True
paused = False
running = True

while running and pngFiles:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  #key 1
                ship = 0
                playerImg = pygame.image.load(SELECTION[ship]) #first index of selection list
                pngFiles = False
            if event.key == pygame.K_2:   #key 2
                ship = 1
                playerImg = pygame.image.load(SELECTION[ship]) #second index of selection list
                pngFiles = False
            if event.key == pygame.K_3:   #key 3
                ship = 2
                playerImg = pygame.image.load(SELECTION[ship]) #third index of selection list
                pngFiles = False   
            if event.key == pygame.K_4:   #key 4
                ship = 3
                playerImg = pygame.image.load(SELECTION[ship]) #fourth index of selection list
                pngFiles = False      
    spacer = 1
    for shipOption in SELECTION:
        screen.blit( pygame.image.load(shipOption), ( 450, (150+spacer)))
        spacer += 120  

     #code for ship selection text
    shipSelectionText = ["PICK", "1", "2", "3", "4"]
    ssLabel = []

    for word in shipSelectionText:
        ssLabel.append(over_font.render(word, True, (255,255,255)))
    
    textSpacer = -120
    for word in ssLabel:
        screen.blit(word, (135, (150 + textSpacer)))
        textSpacer += 120  

    pygame.display.update()          
                
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Pausing       added for pause
              paused = True                      #added for pause
            if event.key == pygame.K_u:  # Unpausing  added for pause
              paused = False                    #added for pause
#            if event.key == pygame.K_p:           #added for pause
#                paused = not paused             #added for pause
            if event.key == pygame.K_LEFT and paused == False:
                playerX_change = -5
            if event.key == pygame.K_RIGHT and paused == False:
                playerX_change = 5
            if event.key == pygame.K_UP and paused == False:   #added for move up
                playerY_change = -5                            #added for move up
            if event.key == pygame.K_DOWN and paused == False:   #added for move down
                playerY_change = 5                              #added for move down
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change      #added for up and down
#playerY += playerY_change
    if playerY <= 0:     #north boundary
        playerY = 0
    elif playerY >= 500:     #south boundary
        playerY = 500
    # Enemy Movement
    if not paused:   #added for pause
        for i in range(num_of_enemies):

            # Game Over
            if enemyY[i] > playerY:    #old value is 440, now if player crosses alien then the game is over
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 736)     # old way to handle collisions
                enemyY[i] = random.randint(50, 150)    #
            '''for i in range(num_of_enemies):
            x = 0
            x = random.randint(0, 736)
            if x not in enemyX:
            enemyX.append(x)
            for i in range(num_of_enemies):
            y = 0
            y = random.randint(50, 150)
            if y not in enemyY:
            enemyY.append(y)'''

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()
