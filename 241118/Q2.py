from tkinter import *

if __name__ == "__main__":
    root = Tk()  
    root.title("GUI_001") 
    root.geometry("500x400+100+50") 
    
    label=Label( root,
                 text="NORTH WEST",
                 anchor=NW,
                  width=30,
                  height=20,
                  background="#ccddff",
                  foreground="#0000ff",)

   
    label.pack()

    root.mainloop()