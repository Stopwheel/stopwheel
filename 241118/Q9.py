from tkinter import *

x = 0

def count(lab):
    global x
    x += 1
    lab.config(text=str(x))
window = Tk()
window.title("Demo 02")
window.geometry("500x400+100+50")
lab0 = Label(
    window,
    width=15,
    height=3,
    bg="#CCBDE0",
    text=str(x),
    justify="center",
    font="Arial 20 bold",
    cursor="bottom_left_corner"
)
lab0.pack()
btnPush = Button(
    window,
    width=15,
    height=2,
    text="Push",
    foreground="#00CACA",
    font="Arial 20 bold",
    command=lambda: count(lab0)
)
btnPush.pack(pady=10)
window.mainloop()
