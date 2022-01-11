# SnakeClass.py

import pygame

import constants
from Position import Position
from Food import Food

class Snake():

    #constructor
    def __init__(self, body, direction):
        #check for valid parameters
        if not direction in ["n","s","e","w"]:
            raise ValueError(f"Argument direction must be n,s,e, or w. direction is {direction}.")
        #check that body is a list of Position
        self.body = body
        self.direction = direction

    def __str__(self):
        string_value = 'snake:'
        string_value = string_value +'\n  body:'
        for i in range(len(self.body)):
            string_value = string_value + "\n    " + str(self.body[i])
        string_value = string_value + "\n  direction:" + self.direction
        return string_value 

    def draw(self,screen):
        #check for valid parameters
        if not isinstance(screen, pygame.Surface):
            raise TypeError(f"Argument screen must be of type pygame.Surface, not {type(screen)} screen:{screen}")
        for i in range(0,len(self.body)):
            pygame.draw.rect(screen, constants.GREEN,[self.body[i].x, self.body[i].y,constants.CELL_WIDTH,constants.CELL_WIDTH])

    # appends a new body part to the snake
    def grow(self):
        if (self.direction == "e"):
            self.body.append(Position(self.body[len(self.body)-1].x - constants.CELL_WIDTH, self.body[len(self.body)-1].y))
        if (self.direction == "w"):
            self.body.append(Position(self.body[len(self.body)-1].x + constants.CELL_WIDTH, self.body[len(self.body)-1].y))
        if (self.direction == "s"):
            self.body.append(Position(self.body[len(self.body)-1].x, self.body[len(self.body)-1].y + constants.CELL_WIDTH))
        if (self.direction == "n"):
            self.body.append(Position(self.body[len(self.body)-1].x, self.body[len(self.body)-1].y - constants.CELL_WIDTH))

    def move(self):
        # append a cell to beginning of body   
        if self.direction == "e":
            new_body_cell = Position(self.body[0].x + constants.CELL_WIDTH, self.body[0].y)
        if self.direction == "w":
            new_body_cell = Position(self.body[0].x - constants.CELL_WIDTH, self.body[0].y)
        if self.direction == "s":
            new_body_cell = Position(self.body[0].x, self.body[0].y + constants.CELL_WIDTH)
        if self.direction == "n":
            new_body_cell = Position(self.body[0].x, self.body[0].y - constants.CELL_WIDTH)
        self.body.insert(0, new_body_cell)
        # remove the last cell in body
        self.body.pop()

    def change_direction(self, direction):
        #check for valid parameters
        if not direction in ["n","s","e","w"]:
            raise ValueError(f"Argument direction must be n,s,e, or w. direction is {direction}.")
        self.direction = direction
        if self.direction == "e":
            for i in range(1, len(self.body)):
                self.body[i].x = self.body[0].x - constants.CELL_WIDTH*i
                self.body[i].y = self.body[0].y
        if self.direction == "w":
            for i in range(1, len(self.body)):
                self.body[i].x = self.body[0].x + constants.CELL_WIDTH*i
                self.body[i].y = self.body[0].y
        if self.direction == "s":
            for i in range(1, len(self.body)):
                self.body[i].x = self.body[0].x
                self.body[i].y = self.body[0].y - constants.CELL_WIDTH*i
        if self.direction == "n":
            for i in range(1, len(self.body)):
                self.body[i].x = self.body[0].x
                self.body[i].y = self.body[0].y + constants.CELL_WIDTH*i

    def ate_food(self, food):
        #check for valid parameters
        if not isinstance(food, Food):
            raise TypeError(f"Argument screen must be of type Food, not {type(food)} food:{food}")
        return food.position == self.body[0]

    def lose_game(self):
        return (self.body[0].x == constants.FRAME_MAX_X or self.body[0].y == constants.FRAME_MAX_Y or 
                self.body[0].x == -constants.CELL_WIDTH or self.body[0].y == -constants.CELL_WIDTH)
