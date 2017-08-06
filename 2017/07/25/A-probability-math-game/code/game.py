import sys
import pygame

pygame.init()

size = width, height = 320, 320
black = 0, 0, 0

screen = pygame.display.set_mode(size)

numberpics = [pygame.image.load("{}.bmp".format(i)) for i in range(10)]
picrect = numberpics[0].get_rect()

while True:
	for event in 
