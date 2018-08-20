# Snake Game in python 3.7 using pygame

#Imports
# Pygame: for helping in creating the game 
# SYS: for 3d modeling and using system modules 
# Random: random number for the food apearing randomly  
# Time: useful for exit functions

import pygame, sys, random, time

check_errors = pygame.init() #initializing pygame
if check_errors[1] > 0:
    print("(!) Had {0} initialziing errors,exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Game is initialized!")

#Creating the game surface

playSurface = pygame.display.set_mode((800,400))
pygame.display.set_caption('Snake Game')

# Colors for the game 
red = pygame.Color(255, 0, 0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0) #score
white = pygame.Color(255, 255, 255) #background
brown = pygame.Color(165, 42, 42) #food

# Control the frames
frameController = pygame.time.Clock()

# variables
snakePos = [100, 50]
snakeBody = [[100,50], [90,50], [80,50]]

foodPos = [random.randrange(1,80)*10, random.randrange(1,40)*10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

#creating function for gameisOver

def gameOver():
    myFont = pygame.font.SysFont('arial', 50)
    gameIsOverSurf = myFont.render('Game Over!', True, red)
    gameIsOverRect = gameIsOverSurf.get_rect()
    gameIsOverRect.midtop = (400,25)
    playSurface.blit(gameIsOverSurf,gameIsOverRect)
    pygame.display.flip()
gameOver()
time.sleep(10)

