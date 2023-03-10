import sys
import math
import numpy as np
import pygame as py
import pygame.draw

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece
def valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def win(board,piece):
    #check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #check verticle location for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check negative sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            py.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+ SQUARESIZE, SQUARESIZE,SQUARESIZE))
            py.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                py.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE  + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                py.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE  + SQUARESIZE / 2)), RADIUS)
    py.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 0

py.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width,height)
RADIUS = int(SQUARESIZE/2 - 5)


screen = py.display.set_mode(size)
draw_board(board)
py.display.update()
myfont = py.font.SysFont("monospace",75)

while not game_over:

    for event in py.event.get():
        if event.type == py.QUIT:
            sys.exit()

        if event.type == py.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK, (0,0, width,SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                py.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                py.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        py.display.update()

        if event.type == py.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            print(event.pos)
             # asks for player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,1)

                    if win(board,1):
                        label = myfont.render("Player 1 Wins!", 1,RED)
                        screen.blit(label, (4,10))
                        game_over = True
             #
             #     #asks for player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if valid_location(board,col):
                    row = get_next_open_row(board,col)
                    drop_piece(board,row,col,2)

                if win(board, 2):
                    label = myfont.render("Player 2 Wins!", 1,YELLOW)
                    screen.blit(label, (4,10))
                    game_over = True


            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2
            if game_over:
                py.time.wait(2000)

