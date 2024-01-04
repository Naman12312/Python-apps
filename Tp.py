from tkinter import *  # from tkinter import *

lst = ['a', 'b', 'c', 'd']

root = Tk()
t = Text(root)
for x in lst:
    t.insert(END, x + '\n')
t.pack()
root.mainloop()
