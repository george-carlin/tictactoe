from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pygame, sys
from pygame.locals import *

FPS = 30 # The frames per second

# Dimensions of the display:
WINDOWSIZE = 720
LINEWIDTH  = 30
MARGIN     = 10
SQUAREWIDTH = (WINDOWSIZE - 2*LINEWIDTH - 6*MARGIN) / 3

BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
BGCOLOUR  = BLACK
XO_COLOUR = WHITE
BOARDSIZE = 3

mousex = 0 # Used to store x-coord of mouse event
mousey = 0 # Used to store y-coord of mouse event


# Initialise a blank board. (2d Array)
def initialise_board():
    board = []
    for i in range(BOARDSIZE):
        column = []
        for j in range(BOARDSIZE):
            column.append('blank')
        board.append(column)
    return board


# Draw a given game square
def draw_square(boxx, boxy, value):
    HALF = int(ICONWIDTH * 0.5)

    left,top = leftTopCoordsOfBox(boxx, boxy)
    if value == 'x':
        pygame.draw.rect(WINDOW, XO_COLOUR, (left, top, SQUAREWIDTH,
                                             SQUAREWIDTH))
    elif value == 'o':
        pygame.draw.circle(WINDOW, XO_COLOUR, (left+half, top+half), half)
    elif value == 'blank':
        pygame.draw.rect(WINDOW,BGCOLOUR, (left, top, SQUAREWIDTH,
                                           SQUAREWIDTH))



# Find the top left corner of a given game square
def leftTopCoordsOfBox(boxx, boxy):
    x = MARGIN + boxx*(SQUAREWIDTH+MARGIN+LINEWIDTH+MARGIN)
    y = MARGIN + boxy*(SQUAREWIDTH+MARGIN+LINEWIDTH+MARGIN)
    return (x, y)

def main(argv=0):
    global FPS_CLOCK, WINDOW
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()

    # Initialise the display window:
    WINDOW = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))
    pygame.display.set_caption('Tic Tac Toe')
    
    # The game board
    board = initialise_board()

    # The main game loop:
    while True:
       mouse_clicked = False

       WINDOW.fill(BGCOLOUR)

       for event in pygame.event.get(): # event handling loop
           if event.type == QUIT or \
                   (event.type == KEYUP and event.key == K_ESCAPE):
               pygame.quit()
               sys.exit()
           elif event.type == MOUSEMOTION:
               mousex, mousey = event.pos
           elif event.type == MOUSEBUTTONUP:
               mousex, mousey = event.pos
               mouseClicked = True
           elif event.type == KEYDOWN:
               print(mousex, mousey)
       
       pygame.display.update()
       FPS_CLOCK.tick(FPS)       


if __name__ == '__main__':
    exit(main())

