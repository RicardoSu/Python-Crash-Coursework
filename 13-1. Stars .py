import sys
import pygame
from pygame.sprite import Sprite

class Star_sky(object):
	"""docstring for Star_sky"""
	def __init__(self):
		
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption('Blue Sky')

		self.bg_color = (0,168,243)

		self.stars = pygame.sprite.Group()
		
	

		self._create_fleet()

	def _create_fleet(self):
		"""Create the fleet of aliens"""
		#create an alien and find the number of aliens ina row
		#spacing between each alien is equal to one alien width
		star = Star(self)
		

		star_width, star_height = star.rect.size
		available_space_x = 1200 - (2 * star_width)
		number_stars_x = (available_space_x //(2 * star_width) + 1)

		#determine the number of rows of aliens that fit on the screen
		available_space_y = (800 -
							(3 * star_height) - star_height)
		number_rows = (available_space_y // (2 * star_height)) 

		#create the full flet of aliens

		for row_number in range(number_rows):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)


	def _create_star(self, star_number, row_number):
		"""Create an alien and place it in the row"""
		star = Star(self)
		star_width, star_height = star.rect.size
		star_width = star.rect.width
		star.x = star_width + 2 * star_width * star_number
		star.rect.x = star.x
		star.rect.y = star.rect.height + 2 * star.rect.height * row_number
		self.stars.add(star)

	def run_game(self):
		"""Start main game loop"""
		while True:
			self._check_events()
			self._update_screen()

	def _check_keydown_events(self, event):
		"""Respond for key presses"""	
		if event.key == pygame.K_q:
			sys.exit()

	def _check_events(self):
		"""Respond for keypress"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen"""
		self.screen.fill(self.bg_color)
		self.stars.draw(self.screen)


		pygame.display.flip()


class Star(Sprite):
	def __init__(self, ai_game):

		super().__init__()

		self.screen = ai_game.screen

		#load the alien image and set rect atribute
		self.image = pygame.image.load('star.bmp')
		self.rect = self.image.get_rect()

		#Start each alien at top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store th alien exact horozontal possition

		self.x = float(self.rect.x)



if __name__ == '__main__':
	#Make game instance and run the game
	ai = Star_sky()
	ai.run_game()