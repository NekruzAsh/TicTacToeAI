from tkinter import *
import random

def nextMove(row, col):
    global player
    if buttons[row][col]["text"] == "" and checkWinner() is False:
        buttons[row][col]["text"] = player
        if checkWinner() is False:
            if player == players[0]:
                player = players[1]
                label.config(text=players[1] + " turn")
                if mode.get() == "AI":
                    makeAIMove()
            else:
                player = players[0]
                label.config(text=players[0] + " turn")
        
def makeAIMove():
    global player
    global ai_player
    row, col = findBestMove(ai_player)

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = ai_player
        if checkWinner() is False:
            player = players[0] if player == players[1] else players[1]  # Update player turn
            label.config(text=player + " turn")
        elif checkWinner() is True:
            label.config(text=ai_player + " wins!")
        elif checkWinner() == "Tie!":
            label.config(text="Tie!")

        # Update button colors for AI mode
        updateButtonColors()

def updateButtonColors():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == players[0]:
                buttons[row][col].config(bg="green")
            elif buttons[row][col]["text"] == players[1]:
                buttons[row][col].config(bg="blue")
            else:
                buttons[row][col].config(bg="white")


def findBestMove(current_player):
    bestScore = -float('inf')
    bestMove = (-1, -1)

    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                buttons[row][col]["text"] = current_player
                score = minimax(0, False, current_player)
                buttons[row][col]["text"] = ""

                if score > bestScore:
                    bestScore = score
                    bestMove = (row, col)

    return bestMove



def minimax(depth, isMaximizing, current_player):
    global ai_player
    opponent = players[0] if current_player == ai_player else ai_player

    if checkWinner():
        if checkWinner() == "Tie!":
            return 0
        return -1 if isMaximizing else 1

    if isMaximizing:
        bestScore = -float('inf')
        for row in range(3):
            for col in range(3):
                if buttons[row][col]["text"] == "":
                    buttons[row][col]["text"] = current_player
                    score = minimax(depth + 1, False, opponent)
                    buttons[row][col]["text"] = ""
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for row in range(3):
            for col in range(3):
                if buttons[row][col]["text"] == "":
                    buttons[row][col]["text"] = current_player
                    score = minimax(depth + 1, True, opponent)
                    buttons[row][col]["text"] = ""
                    bestScore = min(score, bestScore)
        return bestScore


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
    global ai_player
    player = random.choice(players)
    ai_player = players[1] if player == players[0] else players[0]  # Set ai_player opposite of player
    label.config(text=player + " turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="white")

window = Tk()
window.title("Tic Tac Toe AI")

players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=("Helvetica", 40))
label.pack(side="top")

resetButton = Button(text="New Game", font=("Helvetica", 32), command=newGame)
resetButton.pack(side="bottom", pady=70)

frame = Frame(window)
frame.pack()

mode = StringVar()
mode.set("Player")

modeMenu = OptionMenu(window, mode, "Player", "AI")
modeMenu.config(font=("Helvetica", 20)) 
modeMenu.pack(side="bottom", pady=20) 

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("Helvetica", 32), width=5, height=2,
                                    command=lambda row=row, col=col: nextMove(row, col))
        buttons[row][col].grid(row=row, column=col)

window.geometry("700x700")
window.mainloop()