from tkinter import *

if __name__ == "__main__":
    root = Tk()  
    root.title("GUI_001") 
    root.geometry("500x400+100+50") 
    
    label=Label( root,
                 text="To The Word,NCT",
                 anchor=NW,
                  width=30,
                  height=20,
                  wraplength=500,
                  justify=CENTER,
                  font=("Times new Roman",20,"italic","bold",UNDERLINE),
                  background="#ccddff",
                  foreground="#0000ff",)

   
    label.pack()

    root.mainloop()