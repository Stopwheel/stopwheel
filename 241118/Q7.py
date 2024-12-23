from tkinter import *
#from PIL import Image, ImageTk

if __name__ == "__main__":
    root = Tk()
    root.title("GUI_Label_01")
    root.geometry("600x250+100+50")
    
    img = PhotoImage(file="C:\\Users\\user\Downloads\\resized_image.png")
    describe = """To The World, NCT"""
    
    lab0 = Label(
        root,
        image=img,
        text=describe,
        compound=LEFT,
        bg="#ccddff"
    )
    lab0.pack()
    root.mainloop()
