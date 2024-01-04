from tkinter import *
root = Tk()
root.title("Windows resizer")
root.geometry("544x244")
var = StringVar()
var2 = StringVar()
Label(root, text="Width:", font="lucida 19 bold").pack(anchor='nw', side=LEFT)
entry = Entry(root,textvar=var,font="calibri 32 italic")
entry.pack()
Label(root, text="Height:", font="lucida 19 bold").place(x = 0, y = 64)
entry1 = Entry(root, textvar=var2, font="calibri 32 italic")
entry1.pack()
def resize():
    global root
    root.geometry(f"{var.get()}x{var2.get()}")
Button(root,text = "Apply",command=resize, pady=28, padx=45).pack()
root.mainloop()
