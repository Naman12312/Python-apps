import numpy as np 
from matplotlib import pyplot as plt
from numpy.lib.index_tricks import nd_grid 
from numpy.typing import NDArray
equation:str = input("Enter the equation here:\n")
x:NDArray = np.linspace(-10, 10, 10)
part:str = equation.split("=")[1].strip()
if "sin(x)" in part:
    x:NDArray = np.arange(0, 720)
if "cos(x)" in part:
    x:NDArray = np.arange(0, 720)
            
if "tan(x)" in part:
             
    x:NDArray = np.arange(0, 720)

if "cosec(x)" or "csc(x)" in part:
             
    x:NDArray = np.arange(0, 720)

if "sec(x)" in part:
             
    x:NDArray = np.arange(0, 720)

if "cot(x)" in part:
             
    x:NDArray = np.arange(0, 720)

while 1:
    try:
       
        y:NDArray = eval(part)
        break
    except Exception as e:
        globals()[str(e)[6]] = float(input(f"Define {str(e)[6]}:\n"))

plt.plot(x,y) #type: ignore
plt.show()

