import pygame
from map_array import *
from tile import Tile 
from player import Player
from debug import debug

# create level class for all sprites + interactions(player, enemies, etc..)
class Level:
	def __init__(self):

		# get display surface from anywhere i nthe code
		self.display_surface = pygame.display.get_surface()

		# drawn sprites(players, enmies, etc..)
		self.visible_sprites = pygame.sprite.Group()
		# anything in here will collide with the player. but not drawn.
		self.obstables_sprites = pygame.sprite.Group()

		self.create_map()

	# nest for loops
	def create_map(self):
		# use enumerate to find index of each row, to use to multiply with tilesize to get 'y' pos
		for row_index,row in enumerate(WORLD_MAP):
			#print(row_index)
			#print(row)
			# cycle through every item in WORLD_MAP, and find 'x' pos and 'y' pos
			for col_index, col in enumerate(row):
				x = col_index * TILESIZE
				y = row_index * TILESIZE
				if col == 'x':
					# tuple for pos: (x,y). list for all the groups its meant to be in.
					Tile((x,y),[self.visible_sprites, self.obstables_sprites])
				if col == 'p':
					self.player = Player((x,y),[self.visible_sprites])

	def run(self):
		# update + draw the game
		self.visible_sprites.draw(self.display_surface)
		# update sprites
		self.visible_sprites.update()
		debug(self.player.direction)