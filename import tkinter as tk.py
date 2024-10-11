import tkinter as tk
import random
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("775x700")
root.config(bg="#99ff99")
root.resizable(0, 0)
blank_img = tk.PhotoImage(file="bg.png").subsample(1,1)
img_rock = tk.PhotoImage(file="leftrock.png").subsample(3, 3)
img_paper = tk.PhotoImage(file="leftpaper.png").subsample(3, 3)
img_scissors = tk.PhotoImage(file="leftscissors.png").subsample(3, 3)
com_rock = tk.PhotoImage(file="rightrock.png").subsample(3, 3)
com_paper = tk.PhotoImage(file="rightpaper.png").subsample(3, 3)
com_scissors = tk.PhotoImage(file="rightscissors.png").subsample(3, 3)
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
player_img = tk.Label(root, image=blank_img, bg="#99ff99")
player_img.grid(row=2, column=1, padx=10, pady=10)
com_img = tk.Label(root, image=blank_img, bg="#99ff99")
com_img.grid(row=2, column=3, padx=20, pady=30)
status_lbl = tk.Label(root, text="", bg="#99ff99", font=('arial', 16))
status_lbl.grid(row=2, column=2)
tk.Label(root, text="PLAYER",bg="#99ff99").grid(row=1, column=1)
tk.Label(root, text="COMPUTER", bg="#99ff99").grid(row=1, column=3)
tk.Button(root, image=img_rock, command=lambda: play(0)).grid(row=3, column=1, pady=10)
tk.Button(root, image=img_paper, command=lambda: play(1)).grid(row=3, column=2, pady=10)
tk.Button(root, image=img_scissors, command=lambda: play(2)).grid(row=3, column=3, pady=10)
tk.Button(root, text="Quit", command=root.quit).grid(row=5, column=2)
root.mainloop()