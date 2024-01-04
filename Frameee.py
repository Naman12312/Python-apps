from tkinter import *
root = Tk()
root.geometry("456x456")
root.title("sublime text")
f = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f.pack(side=LEFT,fill='y')
f1 = Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f1.pack(side=TOP,fill='x')
Label(f,text="Hello, World.",relief=SUNKEN).pack(pady=212)
Label(f1,text="Welcome to sublime text",relief=SUNKEN).pack()
textarea = Text(f1,font="lucida 12 bold").pack()


root.mainloop()