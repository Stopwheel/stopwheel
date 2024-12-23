from tkinter import *              
#from PIL import Image, ImageTk        

if __name__ == "__main__":          
    root = Tk()                       
    root.title("GUI_Label_01")        
    root.geometry("350x250+100+50")  
    img = PhotoImage(file="C:\\Users\\user\\Downloads\\download.png")  
                                        
    lab0 = Label(root, image=img, bg="#ccddff") 
                                        
    lab0.pack()                         
    root.mainloop()                   