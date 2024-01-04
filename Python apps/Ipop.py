from tkinter import *
def g():
    print("Hello, World!")
if __name__=='__main__':
    root = Tk()
    root.title("GUI")
    root.geometry("644x567")
    Button(root, text="Click me",padx=34, pady=56,command=g).place(x = 300, y = 250)
    root.mainloop()
if __name__=='__main__':
    print("Hello, World!")