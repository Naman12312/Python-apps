from tkinter import *
import os
# songs = os.listdir("F:\\home pc\\my pandrive data\\songs\\")
# print(songs)
root=Tk()
root.configure(bg='red')
root.geometry("644x656")
root.title("Prosee Mp3 player")
import pygame
pygame.init()
pygame.mixer.init()
f=Frame(root,bg="red",padx=10,pady=78)
var=StringVar()
var.set("F:\\Downloads\\")
area=Entry(root,textvar=var,font="comicsansms 19 italic")
area.pack(fill=X)
f.pack()
def play():
    try:
        songs=pygame.mixer.music.load(var.get())
        pygame.mixer.music.play()
    except Exception as e:
        var.set(e)
def fix():
    var.set("F:\\Downloads\\")
def stop():
    pygame.mixer.music.stop()
x="F:\\home pc\\my pandrive data\\songs"
b=Button(f,text="Play!!!",command=play,padx=10,pady=10)
b.pack(pady=100)
b1=Button(f,text="Reset",command=fix,padx=10,pady=10)
b1.pack()
Button(root, text="Stop", command=stop, padx=10, pady=10).pack()
mainloop()
