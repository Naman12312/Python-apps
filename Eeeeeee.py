import numpy as np
import time
t1 = time.perf_counter()
my_arr = np.arange(0, 100000000, dtype="int64")
for i in np.nditer(my_arr):
    print(i**2)
t2 = time.perf_counter()
print(t2-t1)