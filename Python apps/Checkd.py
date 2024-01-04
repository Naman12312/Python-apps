from tkinter import *
root = Tk()
bg = Tk()
root.geometry("644x789")
def g():
    print(var.get())
var = IntVar(bg)
Entry(bg,textvar=var, font="lucida 19 bold").pack()
Button(root, text="Print That!", command=g).pack()
root.mainloop()