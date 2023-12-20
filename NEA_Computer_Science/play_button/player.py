import pygame
from map_array import *

# 'pygame.sprite.Sprite' for inheritence
class Player(pygame.sprite.Sprite):
	# pos to know where to place it, groups = spreadgroup it should be apart of
	def __init__(self, pos, groups, obstacles_sprites):
		# initiate pygame.sprite.Sprite class
		super().__init__(groups)
		self.image = pygame.image.load(r"C:\Users\Dylan\OneDrive\Documents\NEA_Computer_Science\images\TESTPLAYER.png").convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		
		self.direction = pygame.math.Vector2()
		self.speed = 5

		self.obstacles_sprites = obstacles_sprites

	def input(self):
		keys = pygame.key.get_pressed()

		# movement
		if keys[pygame.K_w]:
			self.direction.y = -1
		elif keys[pygame.K_s]:
			self.direction.y = 1
		else:
			self.direction.y = 0 
		if keys[pygame.K_a]:
			self.direction.x = -1
		elif keys[pygame.K_d]:
			self.direction.x = 1
		else:
			self.direction.x = 0

	# speed as an argument, so its the same for the enemies as well as players
	def move(self, speed):
		# vector of 0 cant be normalised
		# if statement - this means that the characters speed is always the same. instead of faster when doing diagonally
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		# change old movement so that is collides with obstacles
		self.rect.x += self.direction.x*speed
		self.collision("horizontal")
		self.rect.y += self.direction.y*speed
		self.collision("vertical")
		# * speed means the character actually moves.
		#self.rect.center += self.direction*speed

	def collision(self, direction):
		if direction == "horizontal":
			# look in all the sprites in obstable sprites(all obstacles)
			for sprite in self.obstacles_sprites:
				# checking the rectable with the rectangle of the player(is there a collision or not)
				if sprite.rect.colliderect(self.rect):
					if self.direction.x > 0: # moving right
						# moves the right side of the player to the left side of the obstacle so it doesnt collide
						self.rect.right = sprite.rect.left
					if self.direction.x < 0: # moving right
						# moves the left side of the player to the right side of the obstacle so it doesnt collide
						self.rect.left = sprite.rect.right

		# same as horizontal
		if direction == "vertical":
			for sprite in self.obstacles_sprites:
				if sprite.rect.colliderect(self.rect):
					if self.direction.y < 0: # moving up
						self.rect.top = sprite.rect.bottom
					if self.direction.y > 0: # moving down
						self.rect.bottom = sprite.rect.top

	def update(self):
		self.input()
		self.move(self.speed)