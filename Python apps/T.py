from tkinter import *
from random import *
canvas=Canvas(width=900,height=900)
canvas.pack()
def g(height,width):
    e=randrange(height)
    f=e+randrange(height)
    g=randrange(width)
    h=g+randrange(width)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
    canvas.create_line(e,f,g,h)
for i in range(48594):
    g(500,500)
mainloop()
