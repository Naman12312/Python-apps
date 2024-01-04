from tkinter import *
root = Tk()
root.geometry("644x567")
def g():
    print("Hello, World!")
from PIL import Image, ImageTk
img = Image.open("F:\\downloads\\2.ico")
photo = ImageTk.PhotoImage(img)
Button(root, image=photo, command=g).pack()
root.mainloop()
