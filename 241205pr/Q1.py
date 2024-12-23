import tkinter as tk
from tkinter import messagebox

users = {
    "Lun": "1111",
    "Ting": "2222",
    "D1345460": "3333"
}

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        messagebox.showinfo("成功", "登入成功！")
        login_frame.pack_forget()
        game_frame.pack()
        reset_game()
    else:
        messagebox.showerror("錯誤", "用戶名或密碼錯誤，請重試！")

def reset_game():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=tk.NORMAL)
    status_label.config(text=f"當前玩家：{current_player}")

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "" or board[0][2] == board[1][1] == board[2][0] != "":
        return board[1][1]
    return None

def check_draw():
    for row in board:
        if "" in row:
            return False
    return True

def on_button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state=tk.DISABLED)
        winner = check_winner()
        if winner:
            messagebox.showinfo("遊戲結束", f"玩家 {winner} 獲勝！")
            reset_game()
        elif check_draw():
            messagebox.showinfo("遊戲結束", "平手！")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"當前玩家：{current_player}")

root = tk.Tk()
root.title("圈圈叉叉遊戲")

login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="用戶名：").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="密碼：").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_frame, text="登入", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

game_frame = tk.Frame(root)

status_label = tk.Label(game_frame, text="當前玩家:X", font=("Arial", 14))
status_label.pack(pady=10)

buttons = [[None for _ in range(3)] for _ in range(3)]
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

grid_frame = tk.Frame(game_frame)
grid_frame.pack()

for row in range(3):
    for col in range(3):
        button = tk.Button(grid_frame, text="", font=("Arial", 20), width=5, height=2,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

reset_button = tk.Button(game_frame, text="重新開始遊戲", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
