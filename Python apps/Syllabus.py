from tkinter import *
tk=Tk()
tk.title("Syllabus of F.A.2")

canvas = Canvas(width=700, height=710, bg='black')


canvas.pack()
canvas.create_text(200,70,fill="cyan",text="Science:\n\n",font=("calibri",28))
canvas.create_text(200,70,fill="cyan",text="\n\n\n\n\n\nSanskrit:\n\n\n\n",font=("calibri",28))
canvas.create_text(200,70,fill="cyan",text="\n\n\n\n\n\nS.S.T:\n\n\n\n\n\n",font=("calibri",28))
canvas.create_text(200,70,fill="cyan",text="\n\n\n\n\n\n\nHindi:\n\n\n",font=("calibri",28))
canvas.create_text(200,70,fill="cyan",text="\n\n\n\n\n\n\n\n\nEnglish:\n\n",font=("calibri",28))
canvas.create_text(200,70,fill="cyan",text="\n\n\n\n\n\n\n\n\n\n\n\n\Math: Exercise:34 to 42 or 43\n\n",font=("calibri",28))
canvas.create_text(200,70,fill="cyan",text="\n\n\n\n\n\n\n\n\n\n\n\n\n\nGK:\n\n",font=("calibri",28))
mainloop()
