import pygame
import random
import time

# Pygame
pygame.init()

# initialization time

start_time = time.time()
font = pygame.font.Font(None, 50)  # font
big_font = pygame.font.Font(None, 100)

#music
sound = pygame.mixer.Sound("sound1.mp3")
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)

# Screen
screen = pygame.display.set_mode((1100,700))

#Background
backgroundImg = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Penguin Game")
icon = pygame.image.load('penguin.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 50
playerY = 420
playerX_change = 0
playerY_change = -0

# Enemy
enemyImg = [random.choice([pygame.image.load('enemy.png'),pygame.image.load('enemy2.png')]),
            random.choice([pygame.image.load('enemy.png'),pygame.image.load('enemy2.png')]),
            random.choice([pygame.image.load('enemy.png'),pygame.image.load('enemy2.png')]),
            random.choice([pygame.image.load('enemy.png'),pygame.image.load('enemy2.png')])]

enemylist = [
    [random.randint(0,1050), random.randint(0,650)],
    [random.randint(0,1050), random.randint(0,650)],
    [random.randint(0,1050), random.randint(0,650)],
    [random.randint(0,1050), random.randint(0,650)]
]
score = 0
enemyX_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(z,x):
        screen.blit(z, x)

# Game loop
running = True
while running:

# RGB red-green-blue
    screen.fill((172, 208, 237))

#Background image
    screen.blit(backgroundImg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                playerY_change = 0
                print("backward")
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
                playerY_change = 0
                print("forward")
            if event.key == pygame.K_DOWN:
                print("fly down")
                playerY_change = 5
                playerX_change = 0

            if event.key == pygame.K_UP:
                print("fly up")
                playerY_change = -5
                playerX_change = 0
        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0

    playerY += playerY_change
    playerX += playerX_change

#collision 
    player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())
    for i in range(len(enemylist)):
        enemy_rect = pygame.Rect(enemylist[i][0], enemylist[i][1], enemyImg[i].get_width(), enemyImg[i].get_height())
        if player_rect.colliderect(enemy_rect):
            enemylist[i] = (random.randint(0,1100), random.randint(0,700))
            enemyImg[i] =  random.choice([pygame.image.load('enemy.png'),pygame.image.load('enemy2.png')])
            score += 1
            sound.play()


    if playerX <=0:
        playerX = 0
    elif playerX >= 990:
        playerX = 990

    if playerY <=0:
        playerY = 0
    elif playerY >= 580:
        playerY = 580

#時間得分
    time_limit = 60 - int(time.time() - start_time)
    timer_text = font.render(f"Time: {time_limit}s", True, (255, 0, 0))
    if time_limit == 0:
        lose = big_font.render("GameOver", True, (0, 0,0))
        screen.blit(lose, (1100//2-200, 700//2))
        pygame.display.update()
        pygame.time.delay(5000)
        running = False
        print("你的得分是:{}".format(score))
    score_text = font.render(f"Score:{score}", True, (0, 0, 0))
    screen.blit(timer_text, (900, 10))
    screen.blit(score_text, (10, 10))

    player(playerX,playerY)
    enemy(enemyImg[0],enemylist[0])
    enemy(enemyImg[1],enemylist[1])
    enemy(enemyImg[2],enemylist[2])
    enemy(enemyImg[3],enemylist[3])

    pygame.display.update()