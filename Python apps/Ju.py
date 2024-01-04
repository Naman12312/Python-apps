from tkinter import *
tk=Tk()
def g ():
    import turtle
    t=turtle.Pen()
    t.circle(100)

btn1 = Button(tk, text="make circle", command=g)
btn1.pack()
tk.mainloop()
