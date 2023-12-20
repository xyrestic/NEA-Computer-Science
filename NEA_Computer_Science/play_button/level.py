import pygame
from map_array import *
from tile import Tile 
from player import Player
from debug import debug
from support import *
from random import choice


# create level class for all sprites + interactions(player, enemies, etc..)
class Level:
	def __init__(self):

		# get display surface from anywhere in the code
		self.display_surface = pygame.display.get_surface()

		# drawn sprites(players, enmies, etc..)
		# self.visible_sprites = pygame.sprite.Group()
		self.visible_sprites = yCameraGroup()
		# anything in here will collide with the player. but not drawn.
		self.obstacles_sprites = pygame.sprite.Group()

		self.create_map()

	# nest for loops
	def create_map(self):
		# dictionary
		layouts = {
			'boundary': import_csv_layout(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\Tiled_csv_files\MAP_FOR_NEA._FloorBlocks.csv"),
			'moreDetails': import_csv_layout(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\Tiled_csv_files\MAP_FOR_NEA._MoreDetails.csv"),
			'largeObjects': import_csv_layout(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\Tiled_csv_files\MAP_FOR_NEA._LargeObjects.csv"),
		}
		graphics = {
			"grass": import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\grass"),
			"sand": import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\sandyArea"),
			"hay": import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\hay"),
			"snow": import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\snow"),
			"poison": import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\poison"),
			"poisonTrees": import_folder(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\deadTrees"),
		}
		#print(graphics)
		# style is going to be boundary, layout will be what in (import_csv_layout)
		for style,layout in layouts.items():
			# use enumerate to find index of each row, to use to multiply with tilesize to get 'y' pos
			for row_index,row in enumerate(layout):
				#print(row_index)
				#print(row)
				# cycle through every item in WORLD_MAP, and find 'x' pos and 'y' pos
				for col_index, col in enumerate(row):
					# if in the csv file, theres a '-1' then do whats in the loop
					if col != "-1":
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						# make the boundary for the map, using the csv file used from the app Tiled
						if style == 'boundary':
							Tile((x,y), [self.obstacles_sprites], "invisible")
						# create more details tile
						if style == "moreDetails":
							# in the array, 180, 181 = light grass/dark grass image (random)
							if col == "180" or col == "181":
								random_grass_image = choice(graphics["grass"])
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "grass", random_grass_image)
							# in the array, 244,214,133 = rock/log/ore/dead tree image (random)
							if col == "244" or col == "214" or col == "133":
								random_sandyArea_image = choice(graphics["sand"])
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "sand", random_sandyArea_image)
							# in the array, 77,78,79,93,94,95,109,110,111 = hay image (random)
							if col == "77" or col == "78" or col == "79" or col == "93" or col == "94" or col == "95" or col == "109" or col == "110" or col == "111":
								random_hay_image = choice(graphics["hay"])
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "hay", random_hay_image)
							# in the array, 199,221 = snowball/snowrock image (random)
							if col  == "199" or col == "221":
								random_snow_image = choice(graphics["snow"])
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "snow", random_snow_image)
							# top left part of tree trunk in poison area
							if col == "128":
								top_left_tree_stump_image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\poison\top_left_tree_trunk.png").convert_alpha()
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "poison", top_left_tree_stump_image)
							# top right part of tree trunk in poison area
							if col == "129":
								top_right_tree_stump_image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\poison\top_right_tree_trunk.png").convert_alpha()
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "poison", top_right_tree_stump_image)
							# bottom left part of tree trunk in poison area
							if col == "144":
								bottom_left_tree_stump_image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\poison\bottom_left_tree_trunk.png").convert_alpha()
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "poison", bottom_left_tree_stump_image)
							# bottom right part of tree trunk in poison area
							if col == "145":
								bottom_right_tree_stump_image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\MoreDetails\poison\bottom_right_tree_trunk.png").convert_alpha()
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "poison", bottom_right_tree_stump_image)
							if col == "148":
								random_dead_tree_image = choice(graphics["poisonTrees"])
								Tile((x,y), [self.visible_sprites, self.obstacles_sprites], "poisonTrees", random_dead_tree_image)

						# create objects tile
						if style == "largeObjects":
							# create objects tile
							pass
		#		if col == 'x':
		#			# tuple for pos: (x,y). list for all the groups its meant to be in.
		#			Tile((x,y),[self.visible_sprites, self.obstacles_sprites])
		#		if col == 'p':
		#			self.player = Player((x,y),[self.visible_sprites], self.obstacles_sprites)
		self.player = Player((3900,2200),[self.visible_sprites], self.obstacles_sprites)

	def run(self):
		# update + draw the game
		#self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.custom_draw(self.player)
		# update sprites
		self.visible_sprites.update()
		#debug(self.player.direction)

class yCameraGroup(pygame.sprite.Group):
	def __init__(self): 

		# general setup
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		# calc the half the screen width + height
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		# creating vector 'offset', by default = 0,0
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surface = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\FLOOR.png").convert()
		self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

	# camera
	def custom_draw(self, player):

		# gettings offset
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawinf the floor
		floor_offset_rect = self.floor_rect.topleft - self.offset
		self.display_surface.blit(self.floor_surface,floor_offset_rect)

		for sprite in self.sprites():
			# gets new offset position from player
			offset_rect = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_rect)
