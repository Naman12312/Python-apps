from tkinter import *
from tkinter.ttk import *
tk=Tk()
style=Style()
style.configure("Tbutton", font=("calibri",10,"bold"),foreground="red")
def g():
    import sys
    import os

    print("give me 5 number")
    our_list=[]
    for z in range(5):
        num=int(input())
        our_list.append(num)

    def acend():
        our_list.sort()   


    def decend():
        our_list.sort(reverse=True)

    print("press a for acent & d for decend")
    order=input()
    if(order== "a"):
        acend()
    elif(order == "d"):
        decend()
    
    print(our_list)
def l():
    exit()
btn=Button(tk,text="start program",command=g)
btn.pack()
btn1=Button(tk,text="Quit",command=l)
btn1.pack()
mainloop()
