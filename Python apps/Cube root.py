import numpy as np
while True:    
    print("tell me a number i will tell cube root of it")
    c=int(input())
    v=np.cbrt(c)
    if v**3!=c:
        print("it is not a perfect cube")
    print("calculating....")
    print("ｲ",v,"^3")