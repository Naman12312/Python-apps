from tkinter import *
from PIL import Image, ImageTk
x = 0
root = Tk()
root.title("TheChosenOne")
scene1 = ImageTk.PhotoImage(Image.open("TheChosenOne.png"))
scene2 = ImageTk.PhotoImage(Image.open("Scene1.png"))
scene3 = ImageTk.PhotoImage(Image.open("TheChosenOne.png"))
scene1_blit = Label(root, image=scene1)
scene1_blit.pack()
def exitgame():
    # exit()
    root.destroy()
def move():
    global x
    if x==0:
        scene1_blit.config(image=scene1)
    if x==1:
        scene1_blit.config(image=scene2)
    if x==2:
        scene1_blit.config(image=scene1)
    elif x>2:
        x=0
    x+=1
    print(x)
    root.after(10, move)
root.wm_attributes('-fullscreen',True)
root.geometry("600x600")
a = root.bind("<Escape>", lambda event:exitgame())
move()
root.mainloop()