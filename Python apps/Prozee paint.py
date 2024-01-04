from tkinter import *
from turtle import *
tk=Tk()
tk.geometry("1000x1000+100+100")
f=Frame(height=500,width=500,bg="green",takefocus="",relief=SUNKEN)
f.grid(row=2,column=2,sticky=(N,E,W,S))

canvas=Canvas(f,width=1920,height=1080)
canvas.pack()
t=RawTurtle(canvas)
t.color("black")
t.speed(100000)
t.shape("turtle")
def g():
    t.color("red")
def h():
    t.color("green")
def r():
    t.color("blue")
def p():
    t.color("yellow")
def e():
    t.color("black")
def w():
    t.color("white")
def q():
    t.color("brown")
def l():
    t.color("orange")
def o():
    t.color("purple")
def i():
    t.color("grey")
def p1():
    x=int(input("tell the width of the pen"))
    t.width(x)
def drag_handler(x,y):
    t.ondrag(None)
    t.goto(x,y)
    t.ondrag(drag_handler)
t.ondrag(drag_handler)
a = Menu(tk)
m = Menu(a)
m.add_command(label="Color=red",command=g)
m.add_command(label="Color=green",command=r)
m.add_command(label="Color=blue",command=h)
m.add_command(label="Color=yellow",command=p)
m.add_command(label="Color=black",command=e)
m.add_command(label="Color=white",command=w)
m.add_command(label="Color=brown",command=q)
m.add_command(label="Color=orange",command=l)
m.add_command(label="Color=purple",command=o)
m.add_command(label="Color=grey",command=i)
tk.config(menu=a)
a.add_cascade(label="color",menu=m)
m1 = Menu(a)
m1.add_command(label="width",command=p1)
tk.config(menu=a)
a.add_cascade(label="width",menu=m1)
m2=Menu(a)
mainloop()
