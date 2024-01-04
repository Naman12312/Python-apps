from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Friend maker")
root.geometry("644x365")
# x = input("tere dost ka naam kya hai???")
def main():
    if val.get()!="":
        mainmenu = Menu(root)
        def func1():
            tmsg.showwarning("Warning...",f"pakka tu {val.get()} se dosti karna chahtaa hai???")
            h = tmsg.askyesnocancel("tu haar gaya",f"{val.get()} tera dost nahi banegaa dubara try karega???")
            if h:
                tmsg.showerror("Error!","Bhai tu pitne vaala hai...")
            else:
                tmsg._show("bahut badiya!!!","bahut badiya tu pitne se bach gaya...")
        click = Menu(mainmenu,tearoff=0)
        click.add_command(label=f"Befrind {val.get()}",command=func1)
        mainmenu.add_cascade(label=f"Befrind {val.get()}",menu=click)
        root.config(menu=mainmenu)
val = StringVar()
Label(root,text="Tere dost ka naam kya hai??").pack()
Label(root,text="naam likhne ke baad hi tu is app ko chala sakta hai.").pack()
Entry(root,textvar=val).pack()
Button(root,text="OK",command=main).pack()
root.mainloop()