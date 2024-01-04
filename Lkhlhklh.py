# from tkinter import *
# root = Tk()
# root.title("Test")
# root.geometry("644x45")
# def hello():
#     tk = Tk()
#     tk.title("Font")
#     tk.geometry("644x644")
#     Button(tk,text="hello").pack()
# Button(root,text = "hello",command = hello,padx=100,pady=100).pack()
# mainloop()
# Creating tkinter window 
import tkinter as tk 
from tkinter import ttk
window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 
# label text for title 
ttk.Label(window, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Select the Month :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 
  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
def g():
    print(monthchoosen.get())
tk.Button(window,text="hello",command=g).grid(row=10,column=10)
window.mainloop() 