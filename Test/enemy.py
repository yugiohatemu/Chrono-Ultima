import sys, pygame
from Builder import Enemy, VectorBullet
from pygame.locals import *

pygame.init()
size = width, height = 320, 480
pause = False

screen = pygame.display.set_mode(size) 
clock = pygame.time.Clock()
info = {'name':'Kitty.gif','spawn_point':[200,100],'move_pattern':[1,0],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,4),'spawn_pattern':(0,5)}}
cat = Enemy(info)
pygame.event.set_blocked(MOUSEMOTION)
time_passed = 0

while 1:        
    for event in pygame.event.get():         
        if event.type == QUIT: 
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_p:
                pause = not pause
               
    if not pause:
        time_passed += clock.tick(30)
        if time_passed >= 1000:
            cat.add_bullet()
            time_passed = 0
        cat.update_self()
   
    #draw itself
    screen.fill((0,0,0)) 
    cat.draw_self(screen)
    
    #show to screen
    pygame.display.update()
