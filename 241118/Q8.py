from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01")
    root.geometry("600x400+100+50")

    lab00 = Label(
        root,
        width=10,
        height=3,
        bg="#ccddef",
        text="(0,0)",
        justify=CENTER,
        font=("Times New Roman", 20, "bold")
    )
    lab00.grid(row=0, column=0, sticky=W, pady=5, padx=3)

    lab01 = Label(
        root,
        width=10,
        height=3,
        bg="#ffddef",
        text="(0,1)",
        justify=CENTER,
        font=("Times New Roman", 20, "bold")
    )
    lab01.grid(row=0, column=1, sticky=W, pady=5, padx=3)

    lab02 = Label(
        root,
        width=10,
        height=3,
        bg="#ccffee",
        text="(0,2)",
        justify=CENTER,
        font=("Times New Roman", 20, "bold")
    )
    lab02.grid(row=0, column=2, sticky=W, pady=5, padx=3)

    lab10 = Label(
        root,
        width=10,
        height=3,
        bg="#ccdfff",
        text="(1,0)",
        justify=CENTER,
        font=("Times New Roman", 20, "bold")
    )
    lab10.grid(row=1, column=0, sticky=W, pady=5, padx=3)

    lab11 = Label(
        root,
        width=10,
        height=3,
        bg="#ccff99",
        text="(1,1)",
        justify=CENTER,
        font=("Times New Roman", 20, "bold")
    )
    lab11.grid(row=1, column=1, sticky=W, pady=5, padx=3)

    root.mainloop()