
#TicTacToe AI game using Python

def new_board():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

board = new_board()

board[0][1] = 'X'
board[1][1] = 'O'

def printBoard(board):
    print(board)

printBoard(board)

