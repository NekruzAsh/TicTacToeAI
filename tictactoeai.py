
from tkinter import *
import random

def nextMove(row, col):
    global player

def checkWinner(board):
    pass

def checkEmptySpaces(board):
    pass

def newGame():
    pass

window = Tk()
window.title("Tic Tac Toe AI")

players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]



label = Label(text= player + " turn", font=("Helvetica", 40))
label.pack(side="top")

resetButton = Button(text="New Game", font=("Helvetica", 32), command=newGame)
resetButton.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("Helvetica", 32), width=5, height=2, command=lambda row=row, col=col: nextMove(row, col))
        buttons[row][col].grid(row=row, column=col)

window.geometry("700x700")
window.mainloop()