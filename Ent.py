from tkinter import *
root = Tk()
root.geometry("655x333")
def getvals():
    print(f"Username: {uservalue.get()}")
    print(f"Password: {passvalue.get()}")
user = Label(root,text="Username:")
password = Label(root,text="Password:")
user.grid()
password.grid(row=1)
# Variables in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
uservalue = StringVar()
passvalue = StringVar()
userentry = Entry(root,textvar = uservalue)
passentry = Entry(root,textvar = passvalue)

userentry.grid(column = 1,row=0)
passentry.grid(column = 1,row=1)
Button(root,text="Submit",command=getvals).grid()


root.mainloop()