import sys
import pygame
from time import sleep
from pygame.sprite import Sprite
from random import randint
import pygame.font


#I got so exited that I forgot to save 14-2 and 14-3


class AlienInvasion(object):
	"""Overall class to manage game AlienInvasion"""
	def __init__(self):
		"""Initaialize the game"""
		pygame.init()
		self.settings = Settings()

		#Screen windows mode
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))


		pygame.display.set_caption('Alien Invasion')

		#Create instance to store game statistics
		self.stats = GameStats(self)


		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.block = pygame.sprite.Group()


		self._create_block()

		self.play_button = Button(self,"Play")
		self.easy_button = EasyButton(self,"Easy Mode")
		self.medium_button = MediumButton(self,"Normal Mode")
		self.hard_button = HardButton(self,"Hard Mode")

		self.missed = 0


	def _create_block(self):
		"""Create the block"""
		
		block = Block(self)
		self.block.add(block)


	def _check_fleet_edges(self):
		"""Respond appropiately if anyaliens have reached an edge"""
		for block in self.block.sprites():
			if block.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet direction"""
		for block in self.block.sprites():
			block.rect.y += self.settings.block_droop_speed
			self.settings.fleet_direction *= -1


	def run_game(self):
		"""Start main game loop"""
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_block()

			self._update_screen()
			
			
	def _update_bullets(self):
		self.bullets.update()
		self.screen_rect = self.screen.get_rect()

		# find missing bullets and increment the counter for each	  
		for bullet in self.bullets:

			if bullet.rect.left <= 0:
				bullet.kill()
				self.missed += 1
				if self.missed >= 3:
					self.stats.game_active = False
					pygame.mouse.set_visible(True)	

		self._check_bullet_block_collisions()		


	def _check_bullet_block_collisions(self):

		"""Respond t bullet-alien colisions"""	

		#Check forany bullets that have hit aliens
		#if so get hit of the bullet and the alien

		collisions= pygame.sprite.groupcollide(
			self.bullets, self.block, False, True)


		if not self.block:
			#Destroy existing bullets and create new fleet
			self.bullets.empty()
			self._create_block()
			self.settings.increase_speed()
			self.missed = 0	


	def _check_events(self):
		"""Respond for keypress"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				self._check_play_button(pygame.mouse.get_pos())



	def _check_keydown_events(self, event):
		"""Respond for key presses"""
		#WASD keyborad to play

		if event.key == pygame.K_d:
			self.ship.moving_right = True
		elif event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_w:
			self.ship.moving_up = True
		elif event.key == pygame.K_s:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):

		#WASD cursor
		if event.key == pygame.K_d:
			self.ship.moving_right = False
		if event.key == pygame.K_a:
			self.ship.moving_left = False
		if event.key == pygame.K_w:
			self.ship.moving_up = False	
		if event.key == pygame.K_s:
			self.ship.moving_down = False


	def _fire_bullet(self):
		"""Create a new bullet and add it to the group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.block.draw(self.screen)	

		#Draw the play button if the game is incative
		if not self.stats.game_active:
			self.play_button.draw_button()
			self.easy_button.draw_button()
			self.medium_button.draw_button()
			self.hard_button.draw_button()


		pygame.display.flip()


	def _ship_hit(self):
		"""Respond to the ship beinghit by an alien"""
		if self.stats.ships_left > 0:	
			#Decrement ships left
			self.stats.ships_left -= 1

			#get rid of  any remaining aliensand bulets
			self.aliens.empty()
			self.bullets.empty()
	
			#create a new fleet and center ship

			self.ship.center_ship()
			self._create_fleet()
			

			#Pause
			sleep(1)
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _update_block(self):
		"""
		Check if the block hit the edge
		then update sends block up
		"""
		self._check_fleet_edges()
		self.block.update()



	def _check_play_button(self,mouse_pos):

		play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
		medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
		hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)

		if play_button_clicked and not self.stats.game_active:
			#self.settings.initialize_dynamic_settings()
			self._start_game()

		elif easy_button_clicked and not self.stats.game_active:
			#self.settings.initialize_dynamic_settings()
			self.settings.speedup_scale = 1.1
			self._start_game()

		elif medium_button_clicked and not self.stats.game_active:
			#self.settings.initialize_dynamic_settings()
			self.settings.speedup_scale = 1.5		
			self._start_game()

		elif hard_button_clicked and not self.stats.game_active:
			#self.settings.initialize_dynamic_settings()
			self.settings.speedup_scale = 3	
			self._start_game()


	def _start_game(self):
	# Reset the game statistics.
		self.missed = 0
		self.settings.initialize_dynamic_settings()
		self.stats.reset_stats()
		self.stats.game_active = True	

		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)
		#Getrid of any remaning aliens and bullets
		self.block.empty()
		self.bullets.empty()		
        #Create  a new fleet.
		self._create_block()
		self.ship.center_ship()


class GameStats:
	"""docstring for GameStats"""
	def __init__(self, ai_game):

		self.settings = ai_game.settings
		self.reset_stats()

		#Start Alien Invasion in an inactive state
		self.game_active = False
		self.high_score = 0



	def reset_stats(self):
		"""Initializr statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	#Start game in an inactive state
		
class Ship(object):
	"""Am class for the Ship"""
	def __init__(self, ai_game):
		"""Ship and starting possition"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#load ship image and get its rect
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()

		#Start each ship at the bottom center
		self.rect.midright = self.screen_rect.midright

		#store adecimal value for the ship horizontal possition
		self.x = float(self.rect.x)

		#store a decimal value for the ship vertical position
		self.y = float(self.rect.y)

		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship position based on the movement flag"""
		#Update the ship x value not the rect 
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0 :
			self.x -= self.settings.ship_speed
		if self.moving_up and self.rect.top > 0 :
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
			self.y += self.settings.ship_speed
		#Update rect object from self.x
		self.rect.x = round(self.x)
		#Update rect object from self.x
		self.rect.y = round(self.y)

	def blitme(self):
		"""Draw ship at current location"""
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.rect.x = round(self.rect.x)
		self.y = float(self.rect.y)

class Settings:
	"""docstring for Settings"""
	def __init__(self):
		"""Game settings"""
		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#ship settings
		self.ship_speed = 5.5
		self.ship_limit = 3

		#bullets settings
		self.bullet_speed = 2
		self.bullet_width = 50
		self.bullet_height = 15
		self.bullet_color = (255,0,0)
		self.bullets_allowed = 3

		#block settings
		self.block_speed = 0.3
		self.block_droop_speed = 5


		# fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

		#How quicly the game speeds up

		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):

		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.block_speed = 1.0
        
        # fleet_direction of 1 represents right, -1 represents left.
		self.fleet_direction = 1

		#Scoring
		self.block_points = 50		

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.block_speed *= self.speedup_scale

		# self.block_points = int(self.block_points * self.score_scale)
		# print(self.block_points)	


class Bullet(Sprite):
	"""A class to manage Bullets from the Ship"""
	def __init__(self,ai_game):
		"""Create a bullet object at the ship current possition"""

		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings		
		self.color = self.settings.bullet_color

		#create a bullet rect at (0,0) and them set correct possition

		self.rect = pygame.Rect(0,0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midleft = ai_game.ship.rect.midleft

		#store the bullets position as a decimal value

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""Move the bullet up the screen"""
		#Update the decimal position of the bullet
		self.x -= self.settings.bullet_speed
		#Update the rect position
		self.rect.x = round(self.x)

	def draw_bullet(self):
		"""Draw bullet into  th screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)

class GameStats:
	"""docstring for GameStats"""
	def __init__(self, ai_game):

		self.settings = ai_game.settings
		self.reset_stats()

		#Start Alien Invasion in an inactive state
		self.game_active = False
		self.high_score = 0



	def reset_stats(self):
		"""Initializr statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	#Start game in an inactive state

class Block(Sprite):
	"""A class to manage the movable block"""
	def __init__(self,ai_game):
		"""Create a bullet object at the ship current possition"""

		super().__init__()

		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#load the Block image and set rect atribute
		self.image = pygame.image.load('rectangle.bmp')
		self.rect = self.image.get_rect()
		#Start each Block at top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#store th Block exact horozontal possition

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)	

	def _update_block(self):
		"""Move the block to the right"""
		self.y -= self.settings.block_speed
		self.rect.y = self.y

	def check_edges(self):
		"""Return True if block is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.bottom:
			return True
		elif self.rect.bottom <= 0:
			return True

	def update(self):
		"""Move block right or left"""
		self.y += (self.settings.block_speed *
						self.settings.fleet_direction)	
		self.rect.y = round(self.y)	


class Button:
	"""docstring for Button"""
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
	
		#SET THE DIMENSIONS FOR THE BUTTON

		self.width, self.height = 200,50
		self.button_color = (0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,48)

		#Built the button rect object and center it

		self.rect = pygame.Rect(500,200, self.width,self.height)

		#the  button message needs tobe preppedonly once

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image, and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Draw blank button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

class EasyButton:
	"""docstring for Button"""
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
	
		#SET THE DIMENSIONS FOR THE BUTTON

		self.width, self.height = 250,50
		self.button_color = (0,255,0)
		self.text_color = (196,255,14)
		self.font = pygame.font.SysFont(None,48)

		#Built the button rect object and center it


		self.rect = pygame.Rect(500,300, self.width,self.height)


		#the  button message needs tobe preppedonly once

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image, and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Draw blank button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

class MediumButton:
	"""docstring for Button"""
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		#SET THE DIMENSIONS FOR THE BUTTON

		self.width, self.height = 250,50
		self.button_color = (0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,48)

		#Built the button rect object and center it


		self.rect = pygame.Rect(500,375, self.width,self.height)


		#the  button message needs tobe preppedonly once

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image, and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Draw blank button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

class HardButton:
	"""docstring for Button"""
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
	
		#SET THE DIMENSIONS FOR THE BUTTON

		self.width, self.height = 250,50
		self.button_color = (0,255,0)
		self.text_color = (236,28,36)
		self.font = pygame.font.SysFont(None,48)

		#Built the button rect object and center it


		self.rect = pygame.Rect(500,450, self.width,self.height)


		#the  button message needs tobe preppedonly once

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image, and center text on the button."""
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		#Draw blank button and then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)

if __name__ == '__main__':
	#Make game instance and run the game
	ai = AlienInvasion()
	ai.run_game()