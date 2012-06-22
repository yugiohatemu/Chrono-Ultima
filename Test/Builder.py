import pygame
from pygame.locals import *

class MovePattern:
	def __init__(self,position=[0,0]): #customizing with initialization from reading info later
		self.current_position = position[:]
		self.path_array = [[1.0,(1.0,1.0)],[2.0,(-1.0,-1.0)]] #time, vector
		#tuple or arry?
		#if info is defined, should read from file..or using enum
		
	def update_current_position_with_time(self,time):
		move_x, move_y = self.path_array[0][1]
		self.current_position[0] += move_x 
		self.current_position[1] += move_y 
	
	def get_current_position_at_time(self,time):
		while(1):
			first_path = self.path_array[1]
			self.update_current_position_with_time(time)
			if time < first_path[0]:
				first_path[0] -= time
				break
			elif time == first_path[0]:
				self.path_array.remove(first_path)
				break
			else:
				time -= first_path[0]
				self.path_array.remove(first_path)
			#what if out of bound ????
		return self.current_position
		
	def __str__(self):
		return 'Define the move pattern for NPC'
	
	def build_move_pattern_with_info(self,info):
		pass
	
	
#BounceBullet, BeamBullet, StalkerBullet,VectorBullet, = (0,1,2,3)

class BulletPattern:
	def __init__(self): #add info for customizing initialization
		self.pattern = ((1.0,1.0),(1.0,0.5)) #Vector bullet 

	def build_bullet_pattern_with_info(self,info):
		pass
		
	#the bullet pattern should take care of how to update bullet
	#so need to build the update function based on info
	#or devide that into basic prototype, then the custom class will dervie based on that
	#CHAIN pattern
    
	
	def __str__(self):
		return 'Construct Bullet Pattern for NPC or Player'

class SpreadBullet:
	def __init__(self, info):
		self.image = pygame.image.load(info['name'])
        	self.base_rect = self.image.get_rect()
        	self.attack_pattern = info['attack_pattern']#attack ((5,3),(5,4),(5,5),(x, y))
        	self.spawn_pattern = info['spawn_pattern'] #((5,3),(5,4),(5,5),(x, y))
        	self.bullet_batch = []
    
    	def add_bullet_with_spawn_location(self,spawn_location = self.base_rect.center):
    	    	one_batch = []
    	    	for pattern in self.spawn_pattern:
    	    		new_bullet = self.base_rect.copy()
    	    	    	new_bullet.center = spawn_point
    	    		new_bullet.move_ip(pattern)
    	    		one_batch.append(new_bullet)
    	    	self.bullet_batch.append(one_batch)
    	    #note: append or extend depends on the complexity of attack_patter
    	def draw_self(self,screen = None):
		for one_batch in self.bullet_batch:
			for one_bullet in one_batch:
				screen.blit(self.image, one_bullet)

    	def update_self(self):
    		for one_batch in self.bullet_batch:
    			num_of_bullet = len(one_batch)
    			for i in range(num_of_bullet):
    				one_batch[i].move_ip(self.attack_pattern)
    				if out_of_screen(one_bullet):					
    					one_batch[i].remove(one_bullet)
    			num_of_bullet = len(one_batch)
    			if num_of_bullet == 0:
    				self.bullet_batch.remove(one_batch)

	def is_collided(self,target):
		for one_batch in self.bullet_batch:
			crush_index = target.collidelist(one_batch)
			if crush_index != -1:
				return True
			else:
				return False    	
    	    	    
    	    	    

class WaveBullet: #for only one side... and not randomnized.......
	def __init__(self, info):
		self.image = pygame.image.load(info['name'])
		self.base_rect = self.image.get_rect()
		self.base_rect.center = info['spawn_center'] #bottom middle, left middle , right middle or up middle
		self.attack_pattern = info['attack_pattern']
		self.spawn_pattern = info['spawn_pattern'] #((-5,5),(-3,5),(0,5),(3, 5),(5,5))
		self.bullet_batch = []
	
	def add_bullet(self):
		one_batch = []
		for pattern in self.spawn_pattern:
			new_bullet = self.base_rect.copy()
    	    	    	new_bullet.center = spawn_point
    	    	    	new_bullet.move_ip(pattern)
    	    	    	one_batch.append(new_bullet)
    	    	 self.bullet_batch.append(one_batch)
    	
    	def draw_self(self):
    		for one_batch in self.bullet_batch:
    			for one_bullet in one_batch:
    				screen.blit(self.image, one_bullet)
    	
    	def update_self(self):
    		for one_batch in self.bullet_batch:
    			num_of_bullet = len(one_batch)
    			for i in range(num_of_bullet):
    				one_batch[i].move_ip(self.attack_pattern)
    				if out_of_screen(one_bullet):					
    					one_batch[i].remove(one_bullet)
    			num_of_bullet = len(one_batch)
    			if num_of_bullet == 0:
    				self.bullet_batch.remove(one_batch)

	def is_collided(self,target):
		for one_batch in self.bullet_batch:
			crush_index = target.collidelist(one_batch)
			if crush_index != -1:
				return True
			else:
				return False   
				
				

def BounceBullet: 
	#basically SpreadBullet but change the attack to be bounce and the out of screen function or change the draw function
	def __init__(self, info):
		self.image = pygame.image.load(info['name'])
		#can add animation here after bouncing
		self.base_rect = self.image.get_rect()
		self.attack_pattern = info['attack_pattern']
		self.spawn_pattern = info['spawn_pattern'] #not needed?
		self.bounce_limit = info['bounce_limit']
		'''
		Remeber to define this based on bount limit
		'''
		self.bullet_batch = []
	
	def add_bullet_with_spawn_location(self,spawn_location):
    	    one_batch = []
    	    for pattern in self.spawn_pattern:
    	    	    new_bullet = self.base_rect.copy()
    	    	    new_bullet.center = spawn_point
    	    	    new_bullet.move_ip(pattern)
    	    	    one_batch.append(new_bullet)
    	    self.bullet_batch.append(one_batch)
    	    #note: append or extend depends on the complexity of attack_patter
    	    
    	def draw_self(self,screen = None):
    		for one_batch in self.bullet_batch:
    			for one_bullet in one_batch:
    				screen.blit(self.image, one_bullet)
    				
    	
    	def update_self(self):
    		for one_batch in self.bullet_batch:
    			num_of_bullet = len(one_batch)
    			for i in range(num_of_bullet):
    				'''
    				Remeber to implement the bound function
    				'''
    				if in_the_bound(one_batch[i],self.bounce_limit):
    					one_batch[i].move_ip(self.attack_pattern)
    				if out_of_screen(one_bullet):					
    					one_batch[i].remove(one_bullet)
    			num_of_bullet = len(one_batch)
    			if num_of_bullet == 0:
    				self.bullet_batch.remove(one_batch)

	def is_collided(self,target):
		for one_batch in self.bullet_batch:
			crush_index = target.collidelist(one_batch)
			if crush_index != -1:
				return True
			else:
				return False    	


def in_the_rect(position,bound =[320,480]):
    	x_bound,y_bound = bound
    	x,y = position
    	if x>=0 and x <= x_bound and y >=0 and y <=y_bound:
        	return True
    	else:
        	return False

def out_of_screen(rect,bound=[320,480]):
	topleft = rect.topleft
	bottomleft = rect.bottomleft
	topright = rect.topright 
	bottomright = rect.bottomright
	x_bound,y_bound = bound
	if in_the_rect(topleft) or in_the_rect(topright) or in_the_rect(bottomleft) or in_the_rect(bottomright):
		return False    
	else:
		return True

class VectorBullet:
	def __init__(self, info):
		self.image = pygame.image.load(info['name'])
		self.base_rect = self.image.get_rect()
		self.attack_pattern = info['attack_pattern']
		self.spawn_pattern = info['spawn_pattern'] 
		self.bullet_batch = []
	
	def draw_self(self,screen = None):
		for one_bullet in self.bullet_batch:
			screen.blit(self.image, one_bullet)
	
	def update_self(self):
		for one_bullet in self.bullet_batch:
			one_bullet.move_ip(self.attack_pattern)
			if out_of_screen(one_bullet):					
				self.bullet_batch.remove(one_bullet)
	
	def is_collided(self,target):	
		crush_index = target.collidelist(self.bullet_batch)
		if crush_index != -1:
			return True
		else:
			return False
	
	def add_bullet_with_spawn_location(self,spawn_point):
		new_bullet = self.base_rect.copy()
		new_bullet.center = spawn_point
		new_bullet.move_ip(self.spawn_pattern)
		self.bullet_batch.append(new_bullet)
		
	def __str__(self):
		return 'Basic setting for VectorBullet'
    
			
class Player:
	def __init__(self, info):	
		animationInfo =  {'up':'Crono.gif','left':'Crono-Left.gif','right':'Crono-Right.gif'}
		self.animation = {}
		#for event, frame in info['anmiation'].items():
		for event, frame in animationInfo.items():
			self.animation[event] = pygame.image.load(frame)
		self.current_image = self.animation['up']
		self.base_rect = self.current_image.get_rect() 
		
		
		self.base_rect = self.image.get_rect()
		self.base_rect.center = info['spawn_point']
		self.bullets = VectorBullet(info['bullet'])				
	
	def update_self(self,move_point):
		move_x = move_point[0]
		self.base_rect.move_ip(move_point)
		if move_x < 0:
			self.current_image = self.animation['left']
		elif move_x == 0:
			self.current_image = self.animation['up']
		else:
			self.current_image = self.animation['right']

	
	def add_bullet(self):
		self.bullets.add_bullet_with_spawn_location(self.base_rect.center)	
	
	def draw_self(self,screen = None):
		screen.blit(self.current_image, self.base_rect)
		self.bullets.draw_self(screen)
						
						
	def is_collided(self,target):
		if self.base_rect.colliderect(target) or self.bullets.is_collided(target):
			return True
		else:
			return False
	
	def __str__(self):
		return 'Construc basic player info' 


class Enemy:
	def __init__(self, info):
		self.image = pygame.image.load(info['name'])
		self.base_rect = self.image.get_rect()
		self.base_rect.center = info['spawn_point']
		self.move_pattern = info['move_pattern']
		self.bullets = VectorBullet(info['bullet'])
		self.inner_timer = 0
		self.shoot_timer = 1000 #info
		
	def update_self(self):
		topright = self.base_rect.topright 
		topleft = self.base_rect.topleft
		if not in_the_rect(topright) or not in_the_rect(topleft):
			self.move_pattern[0] = -self.move_pattern[0] 
			self.move_pattern[1] = -self.move_pattern[1]
		self.base_rect.move_ip(self.move_pattern)
		
		self.bullets.update_self()
	
	def draw_self(self,screen = None):
		screen.blit(self.image, self.base_rect)
		self.bullets.draw_self(screen)
		
	def add_bullet(self,passed_time=0):
		self.inner_timer += passed_time
		if self.inner_timer > self.shoot_timer:
			self.bullets.add_bullet_with_spawn_location(self.base_rect.center)
			self.inner_timer = 0
		
	def is_collided(self,target):
		if self.base_rect.colliderect(target) or self.bullets.is_collided(target):
			return True
		else:
			return False
		
	def __str__(self):
		return 'Construct basic enemy info'



class Level:
	def __init__(self): #again, should be initialize by info builder
		
		self.inc_order = [(5.0, ( {'name':'Kitty.gif','spawn_point':[100,100],'move_pattern':[1,0],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,4),'spawn_pattern':(0,5)}}, \
		{'name':'Kitty.gif','spawn_point':[200,150],'move_pattern':[1,0],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,4),'spawn_pattern':(0,5)}} ) ),\
				(15.0,({'name':'Kitty.gif','spawn_point':[200,250],'move_pattern':[1,0],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,4),'spawn_pattern':(0,5)}} ,\
		{'name':'Kitty.gif','spawn_point':[200,200],'move_pattern':[1,0],\
        'bullet':{'name':'Masamune.gif','attack_pattern':(0,4),'spawn_pattern':(0,5)}}))]																
		
	def create_enemy_batch(self):
		enemy_info = self.inc_order[0][1]
		enemy_batch = []
		for info in enemy_info:
			enemy = Enemy(info)			
			enemy_batch.append(enemy)
			
		self.inc_order.remove(self.inc_order[0])
		return enemy_batch
	
	def __str__(self):
		return 'Costruct basic level info'

	def next_event_time(self):
		if not self.is_level_info_sufficient():
			return 0
		else:
			return self.inc_order[0][0]
	
	def is_level_info_sufficient(self):
		if len(self.inc_order) >0:
			return True
		else:
			return False

class GameMaster:
	def __init__(self,info):
		self.player = Player(info)
		self.enemy_batch = []
	
	def is_game_over(self):
		if self.player == None: #check for life later
			return True
		else:
			return False
	
	def add_enemy(self,add_enemy):
		self.enemy_batch.extend(add_enemy)
                                                
	def draw_self(self,screen):
		if self.player !=None:
			self.player.draw_self(screen)
			for enemy in self.enemy_batch:
				enemy.draw_self(screen)
	
	def update_self(self,move_point):
		if self.player != None:
			self.player.update_self(move_point)
		for enemy in self.enemy_batch:
			enemy.update_self()
			if out_of_screen(enemy.base_rect):
				self.enemy_batch.remove(enemy)
	
	def is_alive(self):
		if self.player == None:
			return False
		else:
			return True
	
	def is_collided(self):
		if self.player != None:
			for enemy in self.enemy_batch:
				if enemy.is_collided(self.player.base_rect):
					self.player = None #inform game over or lose one life
					print 'Player dead'
					return 
				
			for enemy in self.enemy_batch:
				if self.player.bullets.is_collided(enemy.base_rect):
					self.enemy_batch.remove(enemy)
					print 'enemy dead'
				
	
	def __str__(self):
		return 'Control screen updating'

