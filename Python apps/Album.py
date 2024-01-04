from  tkinter import *
import os
# os.read()
from PIL import Image,ImageTk
root = Tk()
root.title("Album of 1 Image")
root.geometry("644x683")
photo = PhotoImage(file="F:\\new dip\\python.gif")
Label(image=photo).pack()
root.mainloop()
