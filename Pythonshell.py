from turtle import *
c=['red','purple','blue','cyan','green','yellow']
t=Pen()
bgcolor("black")
for i in range(360):
    t.pencolor(c[i%6])
    # t.width(i/100+i%100)
    t.forward(i)
    t.left(59)
