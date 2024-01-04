import datetime
import time
time1 = datetime.datetime.now().strftime("%H:%M")
date1 = datetime.date.today()
from tkinter import *
if __name__=='__main__':
    root = Tk()
    root.geometry("544x180")
    root.title("Clock")
    v = StringVar()
    v1 = StringVar()
    v2 = StringVar()
    #root.wm_iconbitmap("F:\\downloads\\icon.ico")
    sec = datetime.datetime.now().second
    def timeg():
        global v
        global v2
        time1 = datetime.datetime.now().strftime("%H:%M")
        sec = datetime.datetime.now().second
        v2.set(sec)
        v.set(time1)
        root.after(1000,timeg)
    def dateg():
        global v1
        date1 = datetime.date.today()
        v1.set(date1)
        root.after(1000, dateg)
    root.configure(bg="black")
    root.maxsize(544,180)
    root.minsize(544,180)
    v.set(time1)
    # Label(root, textvar=v, font="Lucida 109 bold", fg="green", bg="black").place(x = 30, y=250)
    # Label(root, textvar=v1, font="Lucida 19 bold", fg="green", bg="black").place(x = 60, y = 400)
    # Label(root, textvar=v2, font="Lucida 22 bold", fg="green", bg="black").place(x = 430, y = 350)
    Label(root, textvar=v, font="Lucida 109 bold", fg="green", bg="black").pack(side=LEFT)
    Label(root, textvar=v1, font="Lucida 19 bold", fg="green", bg="black").pack(anchor=SW, side=BOTTOM)
    Label(root, textvar=v2, font="Lucida 28 bold", fg="green", bg="black").pack(side=LEFT, pady=50, padx=50)
    root.after(1000,timeg)
    root.after(1000,dateg)
    # root.after(1000,dateg)
    root.mainloop()