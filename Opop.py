from tkinter import *
import tkinter.messagebox as tmsg
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("644x465")
        self.title("GUI")
    @staticmethod
    def hello():
        tmsg.showinfo("Help!","I will help you.")
    def but(self):
        self.btn = Button(self,text="Help!",command=GUI.hello)
        self.btn.pack()
    def g(self):
        tmsg.showinfo("Welcome",f"{self.var.get()}")
    def enteryy(self):
        self.var = StringVar()
        self.enter = Entry(self,textvar=self.var,font="lucida 32 bold")
        self.enter.pack()
        self.btn2 = Button(self,text="Print that!",command=self.g)
        self.btn2.pack()
    def menu(self):
        self.me = Menu(self)
        self.me2 = Menu(self.me,tearoff=0)
        self.me2.add_checkbutton(label="This app is good")
        self.me.add_cascade(label="Click",menu=self.me2)
        self.config(menu=self.me)
    def but2(self):
        self.btn3 = Button(self,text="Quit",command=self.destroy)
        self.btn3.pack()
    def textarea(self):
        self.texta = Text(self,font="lucida 32 italic")
        self.texta.insert(END,"You can do some typing practice here..")
        self.texta.pack()
if __name__ == "__main__":
    window = GUI()
    window.but()
    window.enteryy()
    window.menu()
    window.but2()
    window.textarea()
    window.mainloop()