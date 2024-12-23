from tkinter import *

count = 0

def countFun(lbl, type):
    global count
    count += 1 if type == "add" else -1
    lbl.config(text=str(count))

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Button")
    root.geometry("375x140+100+50")

    lbl = Label(root, width=8, height=2, bg="#ccddef",
                font=("Times New Roman", 20, "bold"),
                text="0", justify=CENTER)
    lbl.grid(row=0, column=1, sticky=NSEW, pady=5, padx=3)

    addBtn = Button(root, text="Add", bg="#ffc989",
                    font=("Times New Roman", 20, "bold"),
                    width=8, height=2, fg="blue",
                    command=lambda: countFun(lbl, "add"))
    addBtn.grid(row=1, column=0, sticky=W, pady=5, padx=3)

    subBtn = Button(root, text="Sub", bg="#ffc989",
                    font=("Times New Roman", 20, "bold"),
                    width=8, height=2, fg="orange",
                    command=lambda: countFun(lbl, "sub"))
    subBtn.grid(row=1, column=1, sticky=W, pady=5, padx=3)

    exitBtn = Button(root, text="Exit", bg="#ffaa66",
                     font=("Times New Roman", 20, "bold"),
                     width=8, height=2, fg="red",
                     command=root.destroy)
    exitBtn.grid(row=1, column=2, sticky=W, pady=5, padx=3)

    root.mainloop()