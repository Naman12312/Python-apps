import time
x=int(input("Enter a big Number:\t"))
t1=time.time()
for i in range(0,x):
    print(i)
print(x)
t2=time.time()
print(f"This took:{t1-t2}")