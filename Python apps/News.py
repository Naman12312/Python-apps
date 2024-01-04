from tkinter import *
canvas=Canvas(width=800,height=800)
canvas.pack()
v=PhotoImage(file="F:\\new dip\\cool pic.png")
canvas.create_image(100,80,image=v,anchor=NW)
canvas.create_text(300,50,text="date:\t27:11:2020\n#today's good news\nmy daddy made such a beautiful painting.\n which had a tree on the beach. this painting was made in 1996.\nwhich means this was made 24 years ago\nthis is too precious to me but not more than my daddy.#today's news ended",font=("calibri",10))
mainloop()
