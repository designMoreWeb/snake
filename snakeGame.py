# Snake Game in python 3.7 using pygame

# Imports
# Pygame: for helping in creating the game
# SYS: for 3d modeling and using system modules
# Random: random number for the food apearing randomly
# Time: useful for exit functions

import pygame, sys, random, time

check_errors = pygame.init()  # initializing pygame
if check_errors[1] > 0:
    print("(!) Had {0} initialziing errors,exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Game is initialized!")

# Creating the game surface

playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game')

# Colors for the game
red = pygame.Color(255, 0, 0)  # gameover
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# Control the frames
frameController = pygame.time.Clock()

# variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

# creating function for gameisOver


def gameOver():
    myFont = pygame.font.SysFont('arial', 50)
    gameIsOverSurf = myFont.render('Game Over!', True, red)
    gameIsOverRect = gameIsOverSurf.get_rect()
    gameIsOverRect.midtop = (360, 15)
    playSurface.blit(gameIsOverSurf, gameIsOverRect)
    pygame.display.flip()

    time.sleep(10)
    pygame.quit()  # snake game exit
    sys.exit()  # console exit


# the main logic for the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeTo == "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeTo == "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeTo == "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeTo == "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event((QUIT)))

# Validate for directions
if changeTo == 'RIGHT' and not direction == 'LEFT':
    direction = 'RIGHT'
if changeTo == 'LEFT' and not direction == 'RIGHT':
    direction = 'LEFT'
if changeTo == 'UP' and not direction == 'DOWN':
    direction = 'UP'
if changeTo == 'DOWN' and not direction == 'UP':
    direction = 'DOWN'

if direction == 'RIGHT':
    snakePos[0] += 10
if direction == 'LEFT':
    snakePos[0] -= 10
if direction == 'UP':
    snakePos[1] -= 10
if direction == 'DOWN':
    snakePos[1] += 10

# SNAKE body Movement
snakeBody.insert(0, list(snakePos))
if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
    foodSpawn = False
else:
    snakeBody.pop()

if foodSpawn == False:
    foodPos = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodSpawn = True

# Graphics
playSurface.fill(white)
for pos in snakeBody:
    pygame.draw.rect(playSurface, green, pygame.RECT(pos[0], pos[1], 10, 10))

pygame.draw.rect(playSurface, brown, pygame.RECT(foodPos[0], foodPos[1], 10, 10))

if snakePos[0] > 720 or snakePos[0] < 0:
    gameOver()
if snakePos[1] > 450 or snakePos[1] < 0:
    gameOver()
    
pygame.display.flip()
frameController.tick(23)
