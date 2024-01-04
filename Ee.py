from tkinter import *
import random
tk=Tk()
canvas=Canvas(tk,width=800,height=800)
canvas.pack()
canvas.create_rectangle(5,6,78,90)
canvas.create_line(0,0,5000,5000)
def random_rectangle(width, height):
 x1 = random.randrange(width)
 y1 = random.randrange(height)
 x2 = x1 + random.randrange(width)
 y2 = y1 + random.randrange(height)
 canvas.create_rectangle(x1, y1, x2, y2)
for x in range(0, 100):
 random_rectangle(400, 400)
def gh (width, height):
    x45 = random.randrange(height)
    y12 = random.randrange(width)
    y11 = y12 + random.randrange(width)
    x34 = x45 + random.randrange(height)
    x = random.randrange(width)
    canvas.create_rectangle(x45,y12,y11,x34)
for i in range (0, 100):
    gh(800, 600)
def hj (width, height):
    x23 = random.randrange(width)
    y23 = random.randrange(height)
    y32 = x23 + random.randrange(height)
    x32 = y23 + random.randrange(width)
for g in range (0, 200):
    hj(897, 987)
def random_rectangle (width, height):
    c23 = random.randrange(width)
    c45 = random.randrange(height)
    c67 = c45 + random.randrange(width)
    c32 = c23 + random.randrange(height)
    canvas.create_rectangle(c23, c32,c67,c32)
for r in range (100):
    random_rectangle(654, 987,)

tk.mainloop()
