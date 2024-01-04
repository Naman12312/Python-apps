from tkinter import *
tk=Tk()
def h ():
    canvas=Canvas(tk,width=500,height=500,bg="green")
    canvas.pack()
    canvas.create_text(90,90,fill="black",text="g",font=('calibri',10))
def g():
    for x in range(1000):
        print(x)
btn=Button(tk,text="c",command=h)
btn.pack()
mainloop()