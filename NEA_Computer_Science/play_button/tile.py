import pygame
from map_array import *

# 'pygame.sprite.Sprite' for inheritence
class Tile(pygame.sprite.Sprite):
	# pos to know where to place it, groups = spreadgroup it should be apart of
	def __init__(self, pos, groups, sprite_type, surface = pygame.Surface((TILESIZE,TILESIZE))):
		# initiate pygame.sprite.Sprite class
		super().__init__(groups)
		self.sprite_type = sprite_type
		#self.image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\TESTOBSTACLE.png").convert_alpha()
		self.image = surface
		self.rect = self.image.get_rect(topleft = pos)
