from tkinter import *
from tkinter.messagebox import showinfo
import tkinter.ttk as ttk
import pyautogui
root=Tk()
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter import font
vt = StringVar(root)
# style = ttk.Style()
def st():
    global x
    global vt
    vt.set("Ready!")
    x.pack(anchor="s", fill="x")
def Font():
    global vt
    fontwin = Tk()
    fontwin.geometry("654x545")
    fontwin.title("Font")
    fontwin.wm_iconbitmap("F:\\downloads\\Python apps\\1.ico")
    var1 = IntVar(fontwin)
    var1.set(19)
    Label(fontwin, text="Size:", font="lucida 14").place(x = 10 , y=140)
    c1 = ttk.Combobox(fontwin, textvar=var1)
    c1['values']=(
        8,
        9,
        10,
        11,
        12,
        14,
        16,
        18,
        20,
        24,
        28,
        36,
        48,
        72
    )
    c1.place(x = 80, y = 140)
    c1.current()
    Label(fontwin, text="Note: the last element of font style is blank. So, it means regular.").place(x = 180, y = 390)
    Label(fontwin, text="Style:", font="lucida 14").place(x = 200, y = 280)
    Label(fontwin, text="Font:", font="lucida 14").place(x = 200, y = 50)
    var2 = StringVar(fontwin)
    var2.set("Calibri")
    c = ttk.Combobox(fontwin, textvar=var2)
    c['values']=(
        "Calibri",
        "Comicsansms",
        "Lucida",
        "Ariel",
        "Century",
        "Monotype",
        "Cambria",
        "Monospaced",
        "Times New Roman",
        "Monotype Corsiva"

        
    )
    c.place(x = 300, y=60)
    c.current()
    var3 = StringVar(fontwin)
    var3.set("")
    c2 = ttk.Combobox(fontwin, textvar=var3)
    c2['values']=(
        "bold",
        "italic",
        "bold italic",
        ""

    )
    c2.current()
    c2.place(x = 270, y = 280)
    def chst():   
        textarea.configure(font=(var2.get(), var1.get(), var3.get()))
        var2.set(var2.get())
        var1.set(var1.get())
        var3.set(var3.get())
        # print(var1.get())
        fontwin.destroy()
        vt.set("Ready!")
    Button(fontwin, text="Ok", command=chst, padx=34).place(x = 534, y = 300)
    vt.set("Busy...")
def hit(key):
    pyautogui.keyDown(key)
def newfile():
    global file
    root.title("Untitled - Notepad++")
    file=None
    textarea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension='.txt',
                        filetypes=[("All Files","*.*"),
                                ("Text Documents","*.txt")
                        ])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad++")
        f = open(file,"r")      
        textarea.delete(1.0,END)        
        textarea.insert(1.0,f.read())     
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
            f = open(file, 'w')
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad++")
    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad++")
def saveas():
    global file
    file=asksaveasfilename(initialfile="Untitled.txt",defaultextension='.txt',
                            filetypes=[("All Files","*.*"),
                                    ("Text Documents","*.txt")
                            ])
    if not os.path.exists(file):
        try:    
            f = open(file, "w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad++")
        except Exception as e:
            pass
    else:
        try:    
            f = open(file, "w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad++")
        except Exception as e:
            pass
def quitapp():
    root.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def delete():
    hit("delete")
def undo():
    textarea.event_generate(("<<SelectAll>>"))
    hit('delete')
def sel():
    textarea.event_generate(("<<SelectAll>>"))
def about():
    showinfo("About Notepad++","Notepad++ by Naman Sharma.")
def Helpee():
    showinfo("Get Help","We will help you.")
if __name__=="__main__":
    root.geometry("1044x567")
    x = Label(root,textvar=vt , relief=SUNKEN)
    root.title("Untitled - Notepad++")
    root.wm_iconbitmap("F:\\Downloads\\Python apps\\1.ico")
    # adding text area
    textarea = Text(root,font="calibri 19")
    file = None
    textarea.pack(expand = True,fill=BOTH)
    #adding menubar
    menubar = Menu(root)
    #File menu starts
    Filemenu = Menu(menubar,tearoff=0)
    Filemenu.add_command(label="New",command=newfile)
    Filemenu.add_command(label="Open...",command=openfile)
    Filemenu.add_command(label="Save",command=savefile)
    Filemenu.add_command(label="Save as...", command=saveas)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quitapp)
    menubar.add_cascade(label="File",menu=Filemenu)
    #File menu ends
    #Edit menu starts
    Editmenu = Menu(menubar,tearoff=0)
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_separator()
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_separator()
    Editmenu.add_command(label="Paste",command=paste)
    Editmenu.add_separator()
    Editmenu.add_command(label="Delete",command=delete)
    Editmenu.add_separator()
    Editmenu.add_command(label="Undo", command=undo)
    Editmenu.add_separator()
    Editmenu.add_command(label="Select All", command=sel)
    menubar.add_cascade(label="Edit",menu=Editmenu)
    #Edit menu ends

    # Format menu starts
    Formenu = Menu(menubar, tearoff=0)
    Formenu.add_checkbutton(label="Word Wrap")
    Formenu.add_command(label="Font...", command=Font)
    menubar.add_cascade(label="Format", menu=Formenu)
    # Format menu ends

    # View menu starts
    View = Menu(menubar, tearoff=0)
    View.add_checkbutton(label="Status bar", command=st)
    menubar.add_cascade(label="View", menu=View)
    # View menu ends

    #Help menu starts
    Helpmenu = Menu(menubar,tearoff=0)
    Helpmenu.add_command(label="Get Help", command=Helpee)
    Helpmenu.add_separator()
    Helpmenu.add_command(label="About Notepad++", command=about)
    menubar.add_cascade(label="Help",menu=Helpmenu)
    #Help menu ends
    #adding scrollbar
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill='y')
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    root.config(menu=menubar)
    root.mainloop()