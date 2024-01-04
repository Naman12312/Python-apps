from tkinter import *
from tkinter.ttk import *
style=Style()
style.configure("TButton",font=("calibri",10,"bold"),foreground="red")
def g():
    print("g")
btn=Button(text="print g",command=g)
btn.pack()
mainloop()
