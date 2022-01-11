# Food.py

import pygame
import random

import constants
from Position import Position

class Food():

	def __init__(self, color=constants.RED):
		x = random.randint(0, round((constants.FRAME_MAX_X-1)/constants.CELL_WIDTH,0))*constants.CELL_WIDTH
		y = random.randint(0, round((constants.FRAME_MAX_Y-1)/constants.CELL_WIDTH,0))*constants.CELL_WIDTH
		self.position = Position(x,y)
		self.color = color

	def draw(self, screen):
	    #check for valid parameters
		if not isinstance(screen, pygame.Surface):
			raise TypeError(f"Argument screen must be of type pygame.Surface, not {type(screen)} screen:{screen}")
		pygame.draw.rect(screen, self.color, [self.position.x, self.position.y,constants.CELL_WIDTH,constants.CELL_WIDTH])

