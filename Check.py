from tkinter import *
import pygame
root = Tk()
root.geometry("646x64")
val = IntVar()
check = Checkbutton(root,text="Bye?",var=val)
check.pack()

def g():
    if val.get()==0:
        print("Shaytaan tune check nahi kya!")
    else:
        print("Achha bachha!")
    root.destroy()

Button(root,text="ok",command=g).pack()
root.mainloop()
