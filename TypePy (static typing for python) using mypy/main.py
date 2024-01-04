import numpy as np


def avg(*args:int) -> float:
    return sum(args)/len(args)
def advanced_avg(argndarray:np.ndarray | list | tuple)->int:
    new_arr = arr.copy()
    if type(new_arr)==np.ndarray:
        return sum(new_arr)/new_arr.shape[0] # type:ignore
    
    else:
        return sum(new_arr)/len(new_arr)
    
    

# print(avg(1,2,3,4,5,6))

arr:np.ndarray = np.array([1,2,3,4,5,6])
# avg(arr)


avg_of_arr:int = advanced_avg(arr)
print(avg_of_arr)

my_var:str = "Hello, World!"

print(my_var)