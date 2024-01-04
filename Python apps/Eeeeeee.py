from time import *
from turtle import *
t=Pen()
def function(max):
    a=time()
    for i in range(max):
        t.begin_fill()
        for x in range(1, 38):
            t.forward(100)
            t.left(175)




        t.end_fill()

    v=time()
    print('it took about %s'%(a-v))
function(1)
