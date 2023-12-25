from tkinter import *
import random

def nextMove(row, col):
    global player
    if buttons[row][col]["text"] == "" and checkWinner() is False:
        if player == players[0]:
            buttons[row][col]["text"] = player
            if checkWinner() is False:
                player = players[1]
                label.config(text=players[1] + " turn")

            elif checkWinner() is True:
                label.config(text=players[0] + " wins!")

            elif checkWinner() == "Tie!":  # Updated comparison
                label.config(text="Tie!")

        else:
            buttons[row][col]["text"] = player
            if checkWinner() is False:
                player = players[0]
                label.config(text=players[0] + " turn")

            elif checkWinner() is True:
                label.config(text=players[1] + " wins!")

            elif checkWinner() == "Tie!":  # Updated comparison
                label.config(text="Tie!")

def checkWinner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True
        
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif checkEmptySpaces() is False:

        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="red")
        return "Tie!"
    
    else:
        return False


def checkEmptySpaces():
    numOfSpaces = 9

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                numOfSpaces -= 1 
    
    if numOfSpaces == 0:
        return False
    
    else:
        return True

def newGame():
    
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="white")

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
resetButton.pack(side="bottom", pady=70)

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("Helvetica", 32), width=5, height=2, command=lambda row=row, col=col: nextMove(row, col))
        buttons[row][col].grid(row=row, column=col)

window.geometry("700x700")
window.mainloop()