from tkinter import *
from tkinter.messagebox import *
root = Tk()
root.title("Naman resturant")
def thanks():
    if c.get()==10:
        showinfo("thanks","Come again in our resturant")
    elif c.get()==5:
        showinfo("Ok","come again in our resturaunt")
    elif c.get()<5:
        showinfo("Ok","We'll try to make our resturaunt")
    with open("experience.txt","w") as f:
        f.write(str(c.get()))
root.geometry("644x300")
Label(text="Welcome to naman resturant please rate how you like our food???",font="comicsansms 10").pack()
c=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=5)
c.pack()
Button(root,text="rate",command=thanks).pack()
root.mainloop()