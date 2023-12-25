
from tkinter import *
import random

def drawBoard(board):
    pass

def nextMove(board, player):
    pass

def checkWinner(board):
    pass

def checkEmptySpaces(board):
    pass

def newGame():
    pass


players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


window = Tk()
window.title("Tic Tac Toe AI")
window.geometry("700x700")
window.mainloop()

