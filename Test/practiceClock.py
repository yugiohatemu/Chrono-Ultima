import sys, pygame
import math
from pygame.locals import *

pygame.init()
size = width, height = 320, 240
x = 0
screen = pygame.display.set_mode(size) 
ball = pygame.image.load("ball.bmp").convert_alpha()
ballrect = ball.get_rect()
speed = 150
clock = pygame.time.Clock()

while True:        
    for event in pygame.event.get():         
        if event.type == QUIT: 
            sys.exit()
    screen.fill((0,0,0))
    screen.blit(ball,(x,100))
    time_passed = clock.tick(30) / 1000.0
    moved = time_passed*speed
    x+= moved
    if  x > 320:
        x -= 320
    pygame.display.update()
