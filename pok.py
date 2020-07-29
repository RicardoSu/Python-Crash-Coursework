import sys
import pygame


class Poke:
	"""Overall class to manage game AlienInvasion"""

	def __init__(self,pok):
		self.screen = pok.screen
		self.screen_rect = pok.screen.get_rect()
		self.image = pygame.image.load('pok.bmp')
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom


	def blitme(self):
		self.screen.blit(self.image, self.rect)			