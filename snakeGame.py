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
time.sleep(8)
