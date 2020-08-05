import pygame, sys
from pygame.locals import *       #load constants

red = [255, 0, 0]

#Initialize Pygame
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

# Set up window
# window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Slither.eat - The Snake Game')

#Set up drawing surface
screen = pygame.display.get_surface()
screen.fill(red)
pygame.display.set_caption("Snake")
pygame.display.flip()


while True:
	# main game loop
	for event in pygame.event.get():
		print(event)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()