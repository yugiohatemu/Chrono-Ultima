import sys, pygame
from Builder import Player
from pygame.locals import *


pygame.init()
size = width, height = 320, 480
move_x = 0
move_y = 0
screen = pygame.display.set_mode(size) 

info = {'name':'Crono.gif','spawn_point':[140,400],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,-4),'spawn_pattern':(0,-5)}}
Crono = Player(info)

pygame.event.set_blocked(MOUSEMOTION)
pygame.key.set_repeat(1,100) #still need to adjust, based on actual performance
#may need to set non_repeat when pressing the pause??
pause = False # can use this to implement pause menu screen later
while 1:        
    for event in pygame.event.get():         
        if event.type == QUIT: 
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT: 
                move_x = -1
            elif event.key == K_RIGHT: 
                move_x = +1                
            elif event.key == K_UP: 
                move_y = -1
            elif event.key == K_DOWN: 
                move_y = +1
            elif event.key == K_z:
                Crono.add_bullet()
            elif event.key == K_p:
                pause = not pause
                
        elif event.type == KEYUP: 
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0 
            elif event.key == K_UP or event.key == K_DOWN:
                move_y = 0
             
    #update position
    if not pause:
        Crono.update_self((move_x,move_y))
    
    #draw itself
    screen.fill((0,0,0)) 
    Crono.draw_self(screen)
    
    #show to screen
    pygame.display.update()
