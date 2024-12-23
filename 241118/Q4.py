from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01")
    root.geometry("250x300+100+50")

    label0 = Label(
        root,
        bitmap="error",
        bg="#ccddee",
        text="iSchool, AITA",
        compound=LEFT
    )
    label0.pack()

    label1 = Label(
        root,
        bitmap="info",
        bg="#ffddee",
        text="iSchool, AITA",
        compound=RIGHT
    )
    label1.pack()

    label2 = Label(
        root,
        bitmap="question",
        bg="#ccffdd",
        text="iSchool, AITA",
        compound=TOP
    )
    label2.pack()

    label3 = Label(
        root,
        bitmap="warning",
        bg="#ccccff",
        text="iSchool, AITA",
        compound=BOTTOM
    )
    label3.pack()

    label4 = Label(
        root,
        bitmap="warning",
        bg="#99ffcc",
        text="iSchool, AITA",
        compound=CENTER
    )
    label4.pack()

    root.mainloop()