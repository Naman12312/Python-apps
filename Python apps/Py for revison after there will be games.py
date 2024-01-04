from time import *
from tkinter import *
tk=Tk()
canvas = Canvas(tk,width=500,height=500)
canvas.pack()
q=canvas.create_rectangle(10,10,25,25)
for i in range(100):
    canvas.move(1,1,3)
def functon(event):
    if event.keysym == 'Up':
         for vi in range(7):
            canvas.move(1,0,-5)
    if event.keysym =='Down':
        for b in range(7):
            canvas.move(1,0,5)
    if event.keysym =='Left':
        for h in range(7):
            canvas.move(1,-5,0)
    if event.keysym =='Right':
        for k in range(7):
            canvas.move(1,5,0)
canvas.bind_all('<KeyPress-Up>',functon)
canvas.bind_all("<KeyPress-Down>",functon)
canvas.bind_all("<KeyPress-Left>",functon)
canvas.bind_all("<KeyPress-Right>",functon)
tk.update()
mainloop()
