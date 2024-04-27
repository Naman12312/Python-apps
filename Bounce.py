from tkinter import *

from random import *
import time
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
    def draw(self):
        self.canvas.move(self.id,0,-1)
        pos=self.canvas.croods(self.id)
        self.x = 0
        self.y = -1
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y=-3
        self.canvas_height = self.canvas.winfo_height()
        if pos [1]<=0:
            self.y=1
        if pos[3]>=self.canvas_height:
            self.y = -1
        if pos[0]<=0:
            self.x=3
        if pos[2]>self.canvas.width:
            self.x = -3
class Paddle:
    def __init__(self,canvas,color):
        pass
        
tk=Tk()
tk.title("bounce!!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
ball = Ball(canvas,'red')
while 1:
    ball.draw
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
if __name__=='__main__':
    print("Hello World")
