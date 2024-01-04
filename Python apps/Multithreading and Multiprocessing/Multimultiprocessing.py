import multiprocessing
import time
def sum1(a):
    b = []
    for i in range(a):
        b.append(i)

if __name__ == "__main__":
    # manager = multiprocessing.Manager()
    # a = manager.dict(10000000)
    
    t1 = time.perf_counter()
    process = multiprocessing.Process(target=sum1, args=(100000000,))
    process.start()
    process.join()
    t2 = time.perf_counter()


    print(t2-t1)