import time
a = 0
b = 1
n = int(input())
series = []
def add ():
    global a,b
    a,b=b,a+b
    series.append(a)

t1 = time.perf_counter()
[add() for i in range(0, n)]
t2 = time.perf_counter()
print(t2-t1)
print(series)
