from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Welcome to Pycharm cummunity edition")
root.geometry("733x434")
root.maxsize(733,430)
root.minsize(733,430)
image = Image.open("D:\\bo.png")
photo = ImageTk.PhotoImage(image)
LL = Label(image=photo).pack()
L = Label(text = "Pycharm Community Edition").pack()
L2 = Label(text="1/24/2021").pack()
L3 = Label(text="Create a new project").pack()
L4 = Label(text="Open").pack()
L5 = Label(text="Check out for a new version").pack()
root.mainloop()