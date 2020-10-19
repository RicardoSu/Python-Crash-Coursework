import sys
import pygame
from pygame.sprite import Sprite

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
		self.rect.midleft = self.screen_rect.midleft

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
		self.rect.x = int(self.x)
		#Update rect object from self.x
		self.rect.y = int(self.y)

	def blitme(self):
		"""Draw ship at current location"""
		self.screen.blit(self.image,self.rect)

class Settings:
	"""docstring for Settings"""
	def __init__(self):
		"""Game settings"""
		#Screen Settings
		self.screen_width = 1300
		self.screen_height = 900
		self.bg_color = (230,230,230)

		#ship settings
		self.ship_speed = 5.5

		#bullets settings
		self.bullet_speed = 1.0
		self.bullet_width = 15		
		self.bullet_height = 5
		self.bullet_color = (255,0,0)
		self.bullets_allowed = 300

		
		

class AlienInvasion(object):
	"""Overall class to manage game AlienInvasion"""
	def __init__(self):
		"""Initaialize the game"""
		pygame.init()
		self.settings = Settings()

		#Screen windows mode
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))

		#Makes full screen but ship slower

		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height



		pygame.display.set_caption('Alien Invasion')

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		"""Start main game loop"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()


			
	def _update_bullets(self):
		"""Update  position of bullets and get tid of the old ones"""	
		#Update bullet possitions
		self.bullets.update()

		#Get rid of old bullets
		for bullet in self.bullets.copy():
			if bullet.rect.x > self.settings.screen_width:
				self.bullets.remove(bullet)
		print(len(self.bullets))			

	def _check_events(self):
		"""Respond for keypress"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


	def _check_keydown_events(self, event):
		"""Respond for key presses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		#WASD keyborad to play

		elif event.key == pygame.K_d:
			self.ship.moving_right = True
		elif event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_w:
			self.ship.moving_up = True
		elif event.key == pygame.K_s:
			self.ship.moving_down = True



		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		"""Respond for key releases"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_UP:
			self.ship.moving_up = False	
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False

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
		pygame.display.flip()


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
		self.rect.midright = ai_game.ship.rect.midright

		#store the bullets position as a decimal value

		self.x = float(self.rect.x)

	def update(self):
		"""Move the bullet up the screen"""
		#Update the decimal position of the bullet
		self.x += self.settings.bullet_speed
		#Update the rect position
		self.rect.x = self.x

	def draw_bullet(self):
		"""Draw bullet into  th screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)



if __name__ == '__main__':
	#Make game instance and run the game
	ai = AlienInvasion()
	ai.run_game()