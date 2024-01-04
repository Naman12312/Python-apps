from sys import *
from os import *
from tkinter import *
canvas=Canvas(width=700,height=700,bg="white")
canvas.pack()
g = PhotoImage(file="F:\\new dip\\python.gif")
canvas.create_image(90, 90, image=g, anchor=NW)
canvas.create_text(90,90,text="Python",fill="Black",font=("calibri",38))

