import turtle
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from PIL import Image, ImageGrab
import time
root = Tk()
root.title("Paint")
root.geometry("1360x978")
canvas = Canvas(root, width = 644, height=374)
canvas.pack(fill = BOTH, expand = True)
canvas.clipboard_clear()
t = turtle.RawTurtle(canvas)
# Main functions
def savefile():
    global file
    file=asksaveasfilename(initialfile = "Untitled.png", defaultextension=".png",
                                                        filetypes=[("PNG image","*.png"),
                                                                ("JPG image","*.jpg"),
                                                                ("BMP picture", "*.bmp")
                                                        ])
    
    image = ImageGrab.grab()
    image.save(file)
    # image.show()
def openfile():
    global file
    file = askopenfilename(defaultextension=".png",
                        filetypes=[("PNG image","*.png"),
                                    ("JPG image","*.jpg"),
                                    ("BMP picture", "*.bmp")
                                                            ])
    image = ImageGrab.Image.open(file)
    image.show()


# Color functions
def blue():
    t.pencolor('blue')
def red():
    t.pencolor('red') 
def green():
    t.pencolor('green')
def black():
    t.pencolor('black')
def brown():
    t.pencolor('brown')
def yellow():
    t.pencolor('yellow')
def pink():
    t.pencolor('pink')
def white():
    t.pencolor('white')
# Width
def width():
    global t
    widthwin = Tk()
    l = Listbox(widthwin)
    l.pack()
    l.insert(END,0)
    l.insert(END,5)
    l.insert(END,10)
    l.insert(END,15)
    l.insert(END,20)
    l.insert(END,25)
    l.insert(END,30)
    l.insert(END,35)
    l.insert(END,40)
    l.insert(END,45)
    l.insert(END,50)
    l.insert(END,55)
    l.insert(END,60)
    l.insert(END,65)
    l.insert(END,70)
    l.insert(END,70)
    l.insert(END,75)
    l.insert(END,80)
    l.insert(END,85)
    l.insert(END,90)
    l.insert(END,95)
    l.insert(END,100)
    def ch():
        t.pensize(l.get(ACTIVE))
        widthwin.destroy()
    Button(widthwin, text="Ok", command=ch).pack()
def new():
    global t
    canvas.delete('all')
    t = turtle.RawTurtle(canvas)
    func2()
# Adding menus
menubar = Menu(root)
Filemenu = Menu(menubar, tearoff = 0)
Filemenu.add_command(label = "New", command = new)
menubar.add_cascade(label = "File", menu = Filemenu)
Filemenu.add_command(label = "Open", command = openfile)
Filemenu.add_command(label = "Save", command = savefile)
# Color menu
Colormenu = Menu(menubar, tearoff = 0)
Colormenu.add_command(label = "Blue", command = blue)
Colormenu.add_command(label = "Red", command = red)
Colormenu.add_command(label = "Green", command = green)
Colormenu.add_command(label = "Black", command = black)
Colormenu.add_command(label = "Brown", command = brown)
Colormenu.add_command(label = "Yellow", command = yellow)
Colormenu.add_command(label = "Pink", command = pink)
Colormenu.add_command(label = "White", command = white)
menubar.add_cascade(label = "Color", menu = Colormenu)
# Width menu
Widthmenu = Menu(menubar, tearoff = 0)
Widthmenu.add_command(label = "Width", command=width)
menubar.add_cascade(label = "Width", menu=Widthmenu)
root.config(menu=menubar)
file = None
def func2():
    t.pencolor("black")    
    t.ondrag(t.goto)
    t.speed('fastest')
    t.screen.onscreenclick(t.goto)
t.screen.onscreenclick(t.goto)
def g():
    image = ImageGrab.grab()
    image.save("F:\\downloads\\File.gif")
    image.show()
func2()
# t.hideturtle()
t.speed('fastest')
root.mainloop()