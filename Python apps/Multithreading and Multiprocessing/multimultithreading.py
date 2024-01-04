import time
import threading
t1 =time.perf_counter()
def main():
    a = []
    for i in range(100000000):
        a.append(i)

thread = threading.Thread(target=main)
thread.start()
thread.join()
t2 = time.perf_counter()
print(t2-t1)