# snake.py

import random
import copy
import pygame # go to command prompt and type "py -m pip install pygame"

from SnakeClass import Snake
from Position import Position
from Food import Food

import constants 

def drawscore(scr, clr):
    font = pygame.font.SysFont("Arial", constants.CELL_WIDTH*3, True, False)
    text = font.render("Score: "+str(score),True,clr)
    screen.blit(text, [constants.FRAME_MAX_X/10,constants.FRAME_MAX_Y/10])


def display_lose_board(score):
    screen.fill(constants.RED)
    drawscore(score,constants.BLACK)
    font = pygame.font.SysFont("Arial", constants.CELL_WIDTH*3, True, False)
    text = font.render("YOU LOSE.",True,constants.BLACK)
    screen.blit(text, [constants.FRAME_MAX_X*1/10,constants.FRAME_MAX_Y/3])
    font2 = pygame.font.SysFont("Arial", constants.CELL_WIDTH*3, True, False)
    text = font2.render("Click ENTER to play again.",True,constants.BLACK)
    screen.blit(text, [constants.FRAME_MAX_X/25,constants.FRAME_MAX_Y*21/25])
    text = font2.render("Click ESC to exit.",True,constants.BLACK)
    screen.blit(text, [constants.FRAME_MAX_X/25,constants.FRAME_MAX_Y*23/25])
    pygame.display.flip()

def display_game_board(snake, food, score):
    screen.fill(constants.BLUE)
    snake.draw(screen)
    food.draw(screen)
    drawscore(score,constants.WHITE)
    pygame.display.flip()

# main program

pygame.init()
screen = pygame.display.set_mode((constants.FRAME_MAX_X,constants.FRAME_MAX_Y))
clock = pygame.time.Clock()

#snake initial position and direction
initialsnakex = constants.FRAME_MAX_X/2 
initialsnakey = constants.FRAME_MAX_Y/2
initialdir = "e"

# loop until hit close button
done = False

score = 0
gamelose = False
gamesnake = Snake([Position(initialsnakex, initialsnakey)], initialdir)
gamefood = Food()

display_game_board(gamesnake,gamefood,score)

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        if gamelose:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #start a new game
                    score = 0
                    gamelose = False
                    gamesnake = Snake([Position(initialsnakex, initialsnakey)], initialdir)
                    gamefood = Food()
                    display_game_board(gamesnake,gamefood,score)
                if event.key == pygame.K_ESCAPE:
                    done = True
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gamesnake.change_direction('w')
                if event.key == pygame.K_RIGHT:
                    gamesnake.change_direction('e')
                if event.key == pygame.K_DOWN:
                    gamesnake.change_direction('s')
                if event.key == pygame.K_UP:
                    gamesnake.change_direction('n')
                if event.key == pygame.K_ESCAPE:
                    done = True
    
    if not gamelose:

        pygame.time.delay(150)
        gamesnake.move()
        display_game_board(gamesnake,gamefood,score)

        if gamesnake.lose_game():
            gamelose = True
            display_lose_board(score)

        if gamesnake.ate_food(gamefood):
            gamesnake.grow()
            score = score + 1
            gamefood = Food()
            display_game_board(gamesnake,gamefood,score)