import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Star_sky(object):
	"""docstring for Star_sky"""
	def __init__(self):
		
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption('Blue Sky')

		self.bg_color = (0,168,243)

		self.stars = pygame.sprite.Group()
	

		self._create_rain()

	def _create_rain(self):
		"""Create the fleet of aliens"""
		#create an alien and find the number of aliens ina row
		#spacing between each alien is equal to one alien width
		star = Star(self)
		

		star_width, star_height = star.rect.size
		available_space_x = 1200
		number_stars_x = 1200 // star_width
		#determine the number of rows of aliens that fit on the screen
		available_space_y = 800
		number_rows = available_space_y // star_height + 6

		#create the full flet of aliens

		for row_number in range(number_rows):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)


	def _create_star(self, star_number, row_number):
		"""Create an alien and place it in the row"""
		star = Star(self)
		star_width, star_height = star.rect.size
		star_width = star.rect.width
		star.x = randint(0, 1200) + star_width
		star.rect.x = star.x
		star.rect.y = randint(0, 1200) + star.rect.height
		self.stars.add(star)

	def _check_fleet_edges(self):
		"""Respond appropiately if anyaliens have reached an edge"""
		for star in self.stars.sprites():
			if star.check_edges():
				star.reset_drop()
			


	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet direction"""
		for star in self.stars.sprites():
			star.rect.y += 1
		#star.direction *= -1	

	def run_game(self):
		"""Start main game loop"""
		while True:
			self._check_events()
			self._update_screen()
			self._update_drops()


			# self._update_stars()

	def _update_drops(self):
		self._check_fleet_edges()
		self.stars.update()

	def _check_keydown_events(self, event):
		"""Respond for key presses"""	
		if event.key == pygame.K_q:
			sys.exit()

	def _check_events(self):
		"""Respond for keypress"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.bg_color)
		self.stars.draw(self.screen)


		pygame.display.flip()

	def _check_keydown_events(self, event):
		if event.key == pygame.K_SPACE:
			self._check_fleet_edges()
			self.stars.update()	


class Star(Sprite):
	def __init__(self, ai_game):

		super().__init__()

		self.screen = ai_game.screen
		self.direction = 1

		#load the alien image and set rect atribute
		self.image = pygame.image.load('raindrop.bmp')
		self.rect = self.image.get_rect()

		#Start each alien at top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store th alien exact horozontal possition

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		self.y += 1
		self.rect.y = self.y

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.top >= screen_rect.bottom:
			return True

	def reset_drop(self):
		self.rect.y = self.rect.height
		self.y = float(self.rect.y)






if __name__ == '__main__':
	#Make game instance and run the game
	ai = Star_sky()
	ai.run_game()