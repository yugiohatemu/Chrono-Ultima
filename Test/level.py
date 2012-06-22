import sys, pygame
import math
from pygame.locals import *

from Builder import GameMaster,Level

pygame.init()
size = width, height = 320, 480
pause = False

screen = pygame.display.set_mode(size) 
move_x,move_y = 0,0 
player_info = {'name':'Crono.gif','spawn_point':[140,400],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,-4),'spawn_pattern':(0,-5)}}
new_game = GameMaster(player_info)
level0 = Level()
next_event_time = level0.next_event_time() * 1000
enough_level_info = level0.is_level_info_sufficient()
clock = pygame.time.Clock()

pygame.event.set_blocked(MOUSEMOTION)
pygame.key.set_repeat(1,100)

while 1:        
    for event in pygame.event.get():         
        if event.type == QUIT: 
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT: 
                move_x = -1
            elif event.key == K_RIGHT: 
                move_x = +1                
            elif event.key == K_UP: 
                move_y = -1
            elif event.key == K_DOWN: 
                move_y = +1
            elif event.key == K_z:
                new_game.player.add_bullet()
            elif event.key == K_p:
                pause = not pause
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                move_x = 0             
            elif event.key == K_UP or event.key == K_DOWN: 
                move_y = 0
    
    if enough_level_info:
        if pygame.time.get_ticks() >= next_event_time:
            new_game.add_enemy(level0.create_enemy_batch())# copy or just pointer ?
            next_event_time = level0.next_event_time() * 1000
            enough_level_info = level0.is_level_info_sufficient()
    
    #also paused time does not afftect pygame time...may need to replace this with clock in
    #order to control
    if not pause:
        time_passed = clock.tick(30)
        for enemy in new_game.enemy_batch:
            enemy.add_bullet(time_passed)
        new_game.update_self((move_x,move_y))
    
    new_game.is_collided()
    
    screen.fill((0,0,0))
    #if new_game.is_alive():
    new_game.draw_self(screen)
               
    pygame.display.update()