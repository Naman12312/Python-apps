from tkinter import *
from tkinter.ttk import *
import sys
import os
style=Style()
style.configure("TButton",font=("calibri",10,'bold'),foreground='red')
tk=Tk()
def i ():
                c=int(input("enter a number"))
                v=int(input("enter another number"))
                print ("what do you want to do options are \n-:Minus\n+:Plus\n*:Multiply\n/:Divide\n%:Persentage\n**=power")
                g=str(input(""))
                if g== '-':
                    print ("result is",c-v)
                elif g== '+':
                    print ("result is", c+v)
                elif g== '*':
                    print("result is",c*v)
                elif g== '/':
                    print ("result is",c/v)
                elif g=="%":
                    print ("result is",c*v/100)
                elif g=="**":
                    print("result is",c**2)

                else:
                    print ("wrong input")
                return
def g():
    exit()    
btn = Button (tk, text="open calculator",command=i)
btn.pack()
print("to calculate again click the button")
#gfdfghdfdjhjdhjddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
mainloop()
