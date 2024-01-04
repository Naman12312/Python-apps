from numba import jit #type:ignore
import numpy as np
import time
x = np.arange(100).reshape(10, 10)
@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def fast_():
    a = []
    for i in range(0, 100000000):
        a.append(i)
    return a
t1 = time.perf_counter()
fast_()


t2 = time.perf_counter()
print(t2-t1)