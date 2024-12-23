from tkinter import *

player = 0 
board = [["" for _ in range(3)] for _ in range(3)]  
buttons = []  

def btn_click(row, col):
    global player
    btn = buttons[row][col]
    if btn["text"] == "":  
        if player == 0:
            btn.config(text="X", fg="blue")
            board[row][col] = "X"
        else:
            btn.config(text="O", fg="red")
            board[row][col] = "O"
        if check_winner():
            winner = "Player X" if player == 0 else "Player O"
            result_label.config(text=f"{winner} Wins!")
            disable_buttons()
        elif all(cell != "" for row in board for cell in row):
            result_label.config(text="It's a Draw!")
        else:
            player = 1 - player  
            turn_label.config(text=f"Player {'X' if player == 0 else 'O'}'s Turn")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def disable_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    root.title("Tic Tac Toe")
    root.geometry("400x450+200+100")
    for i in range(3):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)
    turn_label = Label(root, text="Player X's Turn", font=("Arial", 16))
    turn_label.grid(row=3, column=0, columnspan=3, pady=10)
    result_label = Label(root, text="", font=("Arial", 16))
    result_label.grid(row=4, column=0, columnspan=3, pady=10)
    for i in range(3):
        row_buttons = []
        for j in range(3):
            btn = Button(root, text="", font=("Arial", 20), height=2, width=5,
                         command=lambda row=i, col=j: btn_click(row, col))
            btn.grid(row=i, column=j, sticky=NSEW, pady=5, padx=5)
            row_buttons.append(btn)
        buttons.append(row_buttons)

    root.mainloop()