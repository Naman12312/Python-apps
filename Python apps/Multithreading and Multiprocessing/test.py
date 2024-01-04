def sum1(a):
    b = []
    for i in range(a):
        b.append(i)

import time
t1 = time.time()
sum1(100000000)

t2 = time.time()
print(t2-t1)
# print(arr)
# if only one argument is given in shape of array, then it would be row but if 2 arguments are given, then the first argument is column.