from tkinter import *
root = Tk()
root.geometry("644x546")
menubar = Menu(root)
yess = False
noo = False
x = 0
def click(event):
    global yess
    global noo
    global x
    x = 0
    text = event.widget.cget('text')
    if text=="Yes":
        x +=0.1
        yess = True
    elif text=="No":
        x = 0
        noo = True

def check():
    var = StringVar()
    Entry(root,textvar = var, font="calibri 19 bold").pack(fill = X)
    yes = Button(root,text = "Yes",padx = 20)
    yes.pack()
    yes.bind("<Button-1>",click)
    no = Button(root,text="No" ,padx = 20)
    no.pack()
    no.bind("<Button-1>",click)
    var.set("क्या आप किसी covid-19 से संक्रमित आदमी के पास गए है?")
    var.set("क्या आपको कोई बिमारी हुई है?")

Check = Menu(menubar, tearoff = 0)
Check.add_command(label="Check of covid-19", command = check)
menubar.add_cascade(label="Check", menu = Check)
root.config(menu = menubar)
root.mainloop()