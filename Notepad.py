from tkinter import *
from tkinter.messagebox import showinfo
import pyautogui
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
size = 19
def hit(key):
    pyautogui.keyDown(key)
def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    Textarea.delete(1.0,END)
def openfile():
    global file
    file = askopenfilename(defaultextension='.txt',
                            filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")
                                        ])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Textarea.delete(1.0,END)
        f = open(file,"r")
        Textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension='.txt',
                            filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")
                                        ])
        if file=="":
            file=None
        else:
            f = open(file,"w")
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file,"w")
        f.write(Textarea.get(1.0,END))
        f.close()
def cut():
    Textarea.event_generate(("<<Cut>>"))
def copy():
    Textarea.event_generate(("<<Copy>>"))
def paste():
    Textarea.event_generate(("<<Paste>>"))
def delete():
    hit("delete")
def about():
    showinfo("About Notepad","Notepad by GoldarmGang")
def quitapp():
    root.destroy()
if __name__=="__main__":
    root = Tk()
    root.title("Untitled - Notepad")

    root.geometry("1100x567")
    #Adding textarea
    Textarea = Text(root,font=f"Lucida {size}")
    file = None
    Textarea.pack(expand=True, fill=BOTH)
    #Lets create a menubar
    Menubar = Menu(root)
    #File menu starts


    Filemenu = Menu(Menubar,tearoff=0)
    # To create a new file
    Filemenu.add_command(label="New",command=newfile)

    # To opena file
    Filemenu.add_command(label="Open",command=openfile)

    # To save the current file
    Filemenu.add_command(label="Save",command=savefile)

    Filemenu.add_separator()

    # To quit the app
    Filemenu.add_command(label="Exit",command=quitapp)

    Menubar.add_cascade(label="File",menu=Filemenu)

    # File menu ends

    #Edit menu starts
    Editmenu = Menu(Menubar, tearoff=0)
    # To give a feature of Cut, Copy, Paste
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_separator()
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_separator()
    Editmenu.add_command(label="Paste",command=paste)
    Editmenu.add_separator()
    Editmenu.add_command(label="Delete",command=delete)
    Menubar.add_cascade(label="Edit", menu=Editmenu)

    # Edit menu ends

    # Help menu starts
    Helpmenu = Menu(Menubar, tearoff=0)
    Helpmenu.add_command(label="About Notepad", command=about)

    Menubar.add_cascade(label="Help", menu=Helpmenu)

    # Help menu ends
    scroll = Scrollbar(Textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scroll.set)




    root.config(menu=Menubar)
    root.mainloop()
