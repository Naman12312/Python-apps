from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=500,height=500,bg="green")
canvas.create_text(90,90,fill="black",text="g",font=('calibri',10))
def h ():
    canvas.pack()
    
def g():
    for x in range(1000):
        print(x)
btn=Button(tk,text="c",command=h)
btn.pack()
mainloop()
