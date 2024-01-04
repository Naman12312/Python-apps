from tkinter import *
root = Tk()
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
    print(lbx.get(ACTIVE))
i = 0
root.geometry("644x345")
var = StringVar()
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"Calibri")
lbx.insert(END,"Comicsansms")
lbx.insert(END,"Lucida")
lbx.insert(END,"Monotype corsiva")
Button(root,text="Add item",command=add).pack()



root.mainloop()