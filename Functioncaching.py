from functools import lru_cache
import time
n = int(input("How Many values you want to store in cache?:\t"))
@lru_cache(maxsize=n)
def some_work(n1):
    global n
    time.sleep(n)
    return n
# if __name__=="__main__":
#     # print(some_work())
#     print("Now Running Some work...")
#     print(some_work(3))
#     print(some_work(1))
#     print(some_work(9))
#     print(some_work(6))
#     print("Done..., Calling Again...")
#     print(some_work(3))
#     print("Called Again.")
for i in range(n):    
    print(some_work(n))
"""
Next: Else & Finally In Try Except | Python Tutorials For Absolute Beginners In Hindi #76
"""