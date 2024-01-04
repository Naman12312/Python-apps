import numpy as np 

import pyaudio
from tkinter import *
from tkinter.ttk import *
tk=Tk()
style=Style()
style.configure("w.TButton",font=("calibri",10,"bold"),foreground="red")
def h():
    class animals():
        def elephant(self):
            print ("i'm an elephant")
        def lion(self):
            print ("i'm a lion")
        def gorilla(self):
            print ("i'm a gorilla")
        def rabbit(self):
            print ("i'm a rabbit")

    import turtle
    def a():
        elephant=turtle.Pen()
        elephant.forward(100)
    def b():
        lion=turtle.Pen()
        lion.left(90)
        lion.forward(100)
    def c():
        gorilla=turtle.Pen()
        gorilla.right(90)
        gorilla.forward(100)
    def d():
        rabbit=turtle.Pen()
        rabbit.left(180)
        rabbit.forward(100)
    def e():
        elephant=turtle.Pen()
        elephant.forward(100)
        lion=turtle.Pen()
        lion.left(90)
        lion.forward(100)
        gorilla=turtle.Pen()
        gorilla.right(90)
        gorilla.forward(100)
        rabbit=turtle.Pen()
        rabbit.left(180)
        rabbit.forward(100)
    print("tell which animal you want to move")
    t=str(input())
    if t=="elephant":
        a()
    elif t=="lion":
        b()
    elif t=="gorilla":
        c()
    elif t=="rabbit":
        d()
    elif t=="all":
        e()
btn=Button(tk,style="w.TButton",text="start",command=h)
btn.pack()
mainloop()
