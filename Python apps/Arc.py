from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)
canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)
mainloop()
