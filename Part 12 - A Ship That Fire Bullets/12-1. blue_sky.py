import sys
import pygame


class AlienInvasion:
	"""Overall class to manage game AlienInvasion"""

	def __init__(self):
		"""Initaialize the game"""
		pygame.init()

		self.screen = pygame.display.set_mode((1200,800))
		pygame.display.set_caption('Blue Sky')

		self.bg_color = (0,0,255)


	def run_game(self):
		"""Start main game loop"""
		while True:
            # Watch for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.bg_color)
			pygame.display.flip()

		

if __name__ == '__main__':
	#Make game instance and run the game
	ai = AlienInvasion()
	ai.run_game()