from tkinter import *
canvas=Canvas(width=700,height=700,bg="white")
canvas.pack()
c=str(input("enter the path"))
g=PhotoImage(file=c)
canvas.create_image(90,90,image=g,anchor=NW)
mainloop()
