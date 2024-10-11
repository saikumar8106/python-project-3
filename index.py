
import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("650x560")
root.config(bg="#99ff99")
root.resizable(0, 0)

#================= Load Images =================
blank_img = tk.PhotoImage(file="images/blank.png")
img_rock = tk.PhotoImage(file="images/player_rock.png").subsample(2,2)
img_paper = tk.PhotoImage(file="images/player_paper.png").subsample(2, 2)
img_scissors = tk.PhotoImage(file="images/player_scissor.png").subsample(2, 2)
com_rock = tk.PhotoImage(file="images/com_rock.png").subsample(2,2)
com_paper = tk.PhotoImage(file="images/com_paper.png").subsample(2,2)
com_scissors = tk.PhotoImage(file="images/com_scissor.png").subsample(2,2)

#================== Game Logic ==================
def play(choice):
    player_img.config(image=[img_rock, img_paper, img_scissors][choice])
    
    com_choice = random.randint(0, 2)
    com_img.config(image=[com_rock, com_paper, com_scissors][com_choice])
    
    result = check_winner(choice, com_choice)
    status_lbl.config(text=result)

def check_winner(player, computer):
    if player == computer:
        return "Game Tie"
    elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        return "Player Wins"
    else:
        return "Computer Wins"

#================= Widgets Layout =================
player_img = tk.Label(root, image=blank_img, bg="#99ff99")
player_img.grid(row=2, column=1, padx=20, pady=30)

com_img = tk.Label(root, image=blank_img, bg="#99ff99")
com_img.grid(row=2, column=3, padx=30, pady=30)

status_lbl = tk.Label(root, text="", bg="#99ff99", font=('arial', 12))
status_lbl.grid(row=2, column=2)

tk.Label(root, text="PLAYER",bg="#99ff99").grid(row=1, column=1)
tk.Label(root, text="COMPUTER", bg="#99ff99").grid(row=1, column=3)

# Buttons for Rock, Paper, Scissors
tk.Button(root, image=img_rock, command=lambda: play(0)).grid(row=4, column=1, pady=30)
tk.Button(root, image=img_paper, command=lambda: play(1)).grid(row=4, column=2, pady=30)
tk.Button(root, image=img_scissors, command=lambda: play(2)).grid(row=4, column=3, pady=30)

# Quit button
tk.Button(root, text="Quit", command=root.quit).grid(row=5, column=2)

#================= Run the Application ==================
root.mainloop()
