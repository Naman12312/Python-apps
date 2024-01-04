from tkinter import *
tk=Tk()
tk.geometry("1200x276")
tk.title("label")
f=Label(text='''
In academic terms, a text is anything that conveys a set of meanings to the person who examines it. ...\n You might have thought that texts were limited to written materials, such as books, magazines, newspapers, and 'zines (an informal term for magazine that refers especially to fanzines and webzines'''
)
def g():
    f.pack()
b=Button(tk,text="show label",command=g)
b.pack()
mainloop()