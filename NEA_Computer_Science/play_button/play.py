import pygame, sys
from map_array import *
from debug import debug
from level import Level

class Game:
	def __init__(self):
		# general setup 
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		# name the window
		pygame.display.set_caption("Maths Pursuit")
		self.clock = pygame.time.Clock()

		# create instance of the level class, from level.py
		self.level = Level()

	def run(self):
		while True:
			# event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit() 
					sys.exit()

			self.screen.fill('black')
			# call the run funciton in level.py
			self.level.run()			
			pygame.display.update() 
			self.clock.tick(FPS)

if __name__ == "__main__":
	game = Game()
	game.run()