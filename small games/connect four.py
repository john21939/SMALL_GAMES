import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass
def valid_location():
    pass

board = create_board()
game_over = False
turn = 0

while not game_over:
    #asks for player 1 input
     if turn == 0:
         selection = int(input("Player 1 make your selection (0-6): "))
         #asks for player 2 input
     else:
         selection = int(input("Player 2 make your selection (0-6): "))
     turn += 1
     turn = turn % 2

