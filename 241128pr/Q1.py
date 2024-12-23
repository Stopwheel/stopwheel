import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("猜數字遊戲")
        
        self.range_min = 1
        self.range_max = 100
        self.max_attempts = 10
        self.target = random.randint(self.range_min, self.range_max)
        self.attempts = 0
        self.best_score = None
        
        self.label_title = tk.Label(root, text="歡迎來到猜數字遊戲！", font=("Arial", 16))
        self.label_title.pack(pady=10)
        
        self.label_instruction = tk.Label(root, text="請選擇遊戲難度：", font=("Arial", 12))
        self.label_instruction.pack(pady=5)
        
        self.button_easy = tk.Button(root, text="簡單 (1-100)", command=lambda: self.set_difficulty(1, 100))
        self.button_easy.pack(pady=5)
        
        self.button_medium = tk.Button(root, text="普通 (1-500)", command=lambda: self.set_difficulty(1, 500))
        self.button_medium.pack(pady=5)
        
        self.button_hard = tk.Button(root, text="困難 (1-1000)", command=lambda: self.set_difficulty(1, 1000))
        self.button_hard.pack(pady=5)
    
    def set_difficulty(self, range_min, range_max):
     
        self.range_min = range_min
        self.range_max = range_max
        self.target = random.randint(self.range_min, self.range_max)
        self.attempts = 0
        self.max_attempts = 10
        
        
        self.show_game_interface()
    
    def show_game_interface(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
       
        self.label_range = tk.Label(self.root, text=f"請猜一個 {self.range_min} 到 {self.range_max} 的數字")
        self.label_range.pack(pady=5)
        
        self.entry_guess = tk.Entry(self.root, font=("Arial", 14))
        self.entry_guess.pack(pady=5)
        
        self.button_submit = tk.Button(self.root, text="提交", command=self.check_guess)
        self.button_submit.pack(pady=10)
        
        self.label_feedback = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_feedback.pack(pady=5)
        
        self.label_attempts = tk.Label(self.root, text=f"剩餘次數：{self.max_attempts - self.attempts}")
        self.label_attempts.pack(pady=5)
    
    def check_guess(self):
        try:
            guess = int(self.entry_guess.get())
            self.attempts += 1
            
            if guess < self.target:
                self.label_feedback.config(text="太低了！", fg="blue")
            elif guess > self.target:
                self.label_feedback.config(text="太高了！", fg="blue")
            else:
                self.win_game()
                return
            
            self.entry_guess.delete(0, tk.END)
            self.label_attempts.config(text=f"剩餘次數：{self.max_attempts - self.attempts}")
            
            if self.attempts >= self.max_attempts:
                self.lose_game()
        
        except ValueError:
            messagebox.showerror("錯誤", "請輸入一個有效的數字！")
    
    def win_game(self):
        messagebox.showinfo("恭喜！", f"你猜對了！目標數字是 {self.target}。\n總共用了 {self.attempts} 次。")
        if self.best_score is None or self.attempts < self.best_score:
            self.best_score = self.attempts
            messagebox.showinfo("新紀錄！", f"恭喜！你創下了新的最佳紀錄：{self.best_score} 次！")
        self.reset_game()
    
    def lose_game(self):
        messagebox.showinfo("很可惜！", f"次數用完了！正確答案是 {self.target}。")
        self.reset_game()
    
    def reset_game(self):
      
        self.target = random.randint(self.range_min, self.range_max)
        self.attempts = 0
        self.label_feedback.config(text="")
        self.label_attempts.config(text=f"剩餘次數：{self.max_attempts}")
        self.entry_guess.delete(0, tk.END)

root = tk.Tk()
game = GuessNumberGame(root)
root.mainloop()