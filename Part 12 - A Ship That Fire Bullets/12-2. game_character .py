import sys
import pygame

from pok import Poke


class AlienInvasion:
	"""Overall class to manage game AlienInvasion"""

	def __init__(self):
		"""Initaialize the game"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption('Pok')

		self.bg_color = (255,255,255)

		self.pok = Poke(self)



	def run_game(self):
		"""Start main game loop"""
		while True:
            # Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			self.pok.blitme()
			self.screen.fill(self.bg_color)
			pygame.display.flip()


		

if __name__ == '__main__':
	#Make game instance and run the game
	ai = AlienInvasion()
	ai.run_game()