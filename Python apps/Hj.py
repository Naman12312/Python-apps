from turtle import *
c=['red','purple','blue','cyan','green','yellow','magenta']
t=Pen()
bgcolor("black")
for i in range(363):
    t.pencolor(c[i%7])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)

print("Hello, World!")