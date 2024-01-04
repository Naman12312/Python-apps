if __name__ == '__main__':
    from tkinter import *
    root = Tk()
    root.geometry("644x786")
    def func():
        l.config(bg='grey')
    l=Label(root,text="Hello world",font="lucida 40 bold",bg='red')
    l.pack()
    b=Button(root,text="darken",command=func).pack()
    root.mainloop()