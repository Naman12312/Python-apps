from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("644x342")
statusvar = StringVar()
def func():
    # global statusvar
    statusvar.set("busy...")
    import time
    sbar.update()
    time.sleep(2)
    statusvar.set("Ready!")
    
statusvar.set("Ready!")
sbar = Label(root,textvar = statusvar,relief=SUNKEN,anchor='nw')
sbar.pack(side = "bottom",fill = X)
Button(root,text="Upload", command = func).pack()
root.mainloop()