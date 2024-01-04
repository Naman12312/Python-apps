import time
a,b=0,1
n = int(input())
series = []
t1 = time.perf_counter()
for i in range(0,n):
    a,b=b,a+b
    series.append(a)

t2 = time.perf_counter()
print(t2-t1)
print(series)



