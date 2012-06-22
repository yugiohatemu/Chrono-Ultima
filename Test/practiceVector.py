#!/usr/bin/python
import math
import sys, pygame
from pygame.locals import *


pygame.init()
size = width, height = 480, 480
screen = pygame.display.set_mode(size) 
ball = pygame.image.load("ball.bmp")
pygame.event.set_blocked(MOUSEMOTION)

A = (0.0, 0.0) 
B = (240.0, 480.0)
C = (480, 0) 
speed = (200,150)
#clock = pygame.time.Clock()
x = 0.0
y = 0.0

while 1:        
    for event in pygame.event.get():         
        if event.type == QUIT: 
            sys.exit() 
    screen.fill((0,0,0))
    screen.blit(ball, (x,y))
    
    #time_passed = clock.tick(30) / 1000.0
    #x += speed[0] * time_passed
    #y += speed[1] * time_passed
    
    if x < 240 and y < 480:
        x +=1
        y +=2
    elif x >= 240 and y >0:
        x +=1
        y -=2
        
    
    pygame.display.update()
