# SnakeClass.py

import pygame

import constants
from Position import Position
from Food import Food

class Snake():

    #constructor
    def __init__(self, initial_cell):
        #check for valid parameters
        if not isinstance(initial_cell, tuple):
            raise TypeError("Argument initial_cell must be type tuple")
        if not len(initial_cell) == 2:
            raise ValueError("initial_cell len must be 2")
        cell_pos, cell_dir = initial_cell
        if not isinstance(cell_pos, Position):
            raise TypeError("Argument initial_cell[0] must be type Position")
        if not cell_dir in ["n","s","e","w"]:
            raise ValueError("Argument initial_cell[1] must be must be n,s,e, or w.")
        self.body = [initial_cell]

    def __str__(self):
        string_value = 'snake:'
        string_value = string_value +'\n  body:'
        for i in range(len(self.body)):
            string_value = string_value + "\n    " + str(self.body[i][0])
        string_value = string_value + "\n  direction:" + self.body[0][1]
        return string_value 

    def draw(self,screen):
        #check for valid parameters
        if not isinstance(screen, pygame.Surface):
            raise TypeError(f"Argument screen must be of type pygame.Surface, not {type(screen)} screen:{screen}")
        for i in range(0,len(self.body)):
            pygame.draw.rect(screen, constants.GREEN,[self.body[i][0].x, self.body[i][0].y,constants.CELL_WIDTH,constants.CELL_WIDTH])

    # appends a new body part to the snake
    def grow(self):
        last_cell_pos, last_cell_dir = self.body[len(self.body)-1]
        if (last_cell_dir == "e"):
            self.body.append((Position(last_cell_pos.x - constants.CELL_WIDTH, last_cell_pos.y), last_cell_dir))
        if (last_cell_dir == "w"):
            self.body.append((Position(last_cell_pos.x + constants.CELL_WIDTH, last_cell_pos.y), last_cell_dir))
        if (last_cell_dir == "s"):
            self.body.append((Position(last_cell_pos.x, last_cell_pos.y + constants.CELL_WIDTH), last_cell_dir))
        if (last_cell_dir == "n"):
            self.body.append((Position(last_cell_pos.x, last_cell_pos.y - constants.CELL_WIDTH), last_cell_dir))

    def move(self):
        # append a cell to beginning of body
        cell0_pos, cell0_direction = self.body[0]
        if cell0_direction == "e":
            new_body_cell = (Position(cell0_pos.x + constants.CELL_WIDTH, cell0_pos.y), cell0_direction)
        if cell0_direction == "w":
            new_body_cell = (Position(cell0_pos.x - constants.CELL_WIDTH, cell0_pos.y), cell0_direction)
        if cell0_direction == "s":
            new_body_cell = (Position(cell0_pos.x, cell0_pos.y + constants.CELL_WIDTH), cell0_direction)
        if cell0_direction == "n":
            new_body_cell = (Position(cell0_pos.x, cell0_pos.y - constants.CELL_WIDTH), cell0_direction)
        self.body.insert(0, new_body_cell)
        # remove the last cell in body
        self.body.pop()

    def change_direction(self, direction):
        #check for valid parameters
        if not direction in ["n","s","e","w"]:
            raise ValueError(f"Argument direction must be n,s,e, or w. direction is {direction}.")
        new_cell_0 = (self.body[0][0], direction)
        self.body[0] = new_cell_0

    def ate_food(self, food):
        #check for valid parameters
        if not isinstance(food, Food):
            raise TypeError(f"Argument screen must be of type Food, not {type(food)} food:{food}")
        return food.position == self.body[0][0]

    def lose_game(self):
        cell0_pos = self.body[0][0]

        return (cell0_pos.x == constants.FRAME_MAX_X or cell0_pos.y == constants.FRAME_MAX_Y or 
                cell0_pos.x == -constants.CELL_WIDTH or cell0_pos.y == -constants.CELL_WIDTH)
