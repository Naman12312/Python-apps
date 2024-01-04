from tkinter import *
tk=Tk()
tk.title("Tank Game")
canvas=Canvas(tk,width=1300,height=700,bg="white")
canvas.pack()
#My first game "Tank"
#this is the best game in the world
#There are two teams cyan and red
m=canvas.create_rectangle(109,194,50,50,fill="cyan")
m1=canvas.create_rectangle(109,194,50,50,fill="red")
m2=canvas.create_oval(10,10,25,25,fill="red")
m3=canvas.create_oval(10,10,25,25,fill="cyan")
for p1 in range(80):    
    canvas.move(m3,0,5)
for z in range(6):
    canvas.move(m,5,0)
for u in range(20):
    canvas.move(m3,5,0)
for t in range(30):
    canvas.move(m2,0,12)
    canvas.move(m2,5,0)

for x in range(7):
    canvas.move(m,0,5)
def g(event):
        if event.keysym=="Up":
            for i in range(7):
                canvas.move(m,0,-5)
                canvas.move(m3,0,-5)
        if event.keysym=="Down":
            for x in range(7):
                canvas.move(m3,0,5)
                canvas.move(m,0,5)
        if event.keysym=="Right":
            for c in range(7):
                canvas.move(m3,5,0)
                canvas.move(m,5,0)
        if event.keysym=="Left":
            for v in range(7):
                canvas.move(m3,-5,0)
                canvas.move(m,-5,0)
        if event.keysym=="w":
            for q in range(7):
                canvas.move(m1,0,-5)
                canvas.move(m2,0,-5)
        if event.keysym=="s":
            for x in range(7):
                canvas.move(m1,0,5)
                canvas.move(m2,0,5)
        if event.keysym=="d":
            for c in range(7):
                canvas.move(m1,5,0)
                canvas.move(m2,5,0)
        if event.keysym=="a":
            for c in range(7):
                canvas.move(m1,-5,0)
                canvas.move(m2,-5,0)
        if event.keysym=="i":
            for c in range(7):
                canvas.move(m2,0,-5)
        if event.keysym=="k":
            for c in range(7):
                canvas.move(m2,0,5)
        if event.keysym=="j":
            for c in range(7):
                canvas.move(m2,-5,0)
        if event.keysym=="l":
            for c in range(7):
                canvas.move(m2,5,0)
        if event.keysym=="5":
            for c in range(7):
                canvas.move(m3,0,-5)
        if event.keysym=="2":
            for c in range(7):
                canvas.move(m3,0,5)
        if event.keysym=="1":
            for c in range(7):
                canvas.move(m3,-5,0)
        if event.keysym=="3":
            for c in range(7):
                canvas.move(m3,5,0)
        if event.keysym=="Return":
            for c in range(7):
                canvas.move(m3,0,5)
        if event.keysym=="z":
            canvas.create_text(200,90,text="Game over",font=("calibri",70))
        
    
canvas.bind_all("<KeyPress-Up>",g)
canvas.bind_all("<KeyPress-Down>",g)
canvas.bind_all("<KeyPress-Right>",g)
canvas.bind_all("<KeyPress-Left>",g)
canvas.bind_all("<KeyPress-w>",g)
canvas.bind_all("<KeyPress-s>",g)
canvas.bind_all("<KeyPress-a>",g)
canvas.bind_all("<KeyPress-d>",g)
canvas.bind_all("<KeyPress-Return>",g)
canvas.bind_all("<KeyPress-Q>",g)
canvas.bind_all("<KeyPress-z>",g)
canvas.bind_all("<KeyPress-i>",g)
canvas.bind_all("<KeyPress-k>",g)
canvas.bind_all("<KeyPress-j>",g)
canvas.bind_all("<KeyPress-l>",g)
canvas.bind_all("<KeyPress-5>",g)
canvas.bind_all("<KeyPress-2>",g)
canvas.bind_all("<KeyPress-1>",g)
canvas.bind_all("<KeyPress-3>",g)
tk.update()
mainloop()
