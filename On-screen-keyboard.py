from tkinter import *
import pyautogui
root = Tk()
root.geometry("1134x244")
sval = StringVar()
textarea = Entry(root,textvar=sval,font="comicsansms 32 bold")
textarea.pack(padx=10,pady=10)
def click(event):
    global sval
    text = event.widget.cget("text")
    sval.set(sval.get() + text)
b = Button(root,text="g")
b.bind("<Button-1>",click)
b.pack()

root.mainloop()