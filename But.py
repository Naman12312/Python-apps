from tkinter import *
root = Tk()
root.geometry("644x456")
# def hello():
#     print("Hello")
# f = Frame(root,borderwidth=6,bg="grey",relief = SUNKEN)
# f.pack(side=LEFT,anchor='nw')
# for i in range(0,6):
#     b = Button(f,fg = "red",text="Print Now",command=hello)
#     b.pack(side=LEFT)
def f1():
    print("Challenge")
def f2():
    print("Accepted")
def f3():
    print("Harry")
def f4():
    print("Sir")
Label(root,text="Welcome! press all the buttons",font="lucida 32 bold").pack()
b1 = Button(root,text="Click me",command=f1)
b1.pack(anchor='sw',side=LEFT,padx=50)
b2 = Button(root,text="Click me",command=f2)
b2.pack(anchor='sw',side=LEFT,padx=50)
b3 = Button(root,text="Click me",command=f3)
b3.pack(anchor='sw',side=LEFT,padx=50)
b4 = Button(root,text="Click me",command=f4)
b4.pack(anchor='sw',side=LEFT,padx=50)




root.mainloop()