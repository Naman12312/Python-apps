from tkinter import *
tk=Tk()
def g():
    print ("g")
def h():
    import turtle
    t=turtle.Pen()
    r=int(input("tell me the size of circle"))
    t.circle(r)
btn1=Button(tk,text="click me", command=g)
btn1.pack()          
btn2=Button(tk,text="maker circle", command=h)
btn2.pack()
tk.mainloop()
