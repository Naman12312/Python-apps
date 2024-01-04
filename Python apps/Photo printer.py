from sys import *
from os import *
from tkinter import *

canvas = Canvas(width=700, height=710, bg='black')


canvas.pack()

filename=str(input("enter the path of the gif file"))
gif1 = PhotoImage(file=filename)
canvas.create_image(90, 90, image=gif1, anchor=NW)


mainloop()






