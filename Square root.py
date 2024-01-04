import math
while True:
    print("tell me a number i will tell you the square root of it\t")
    v=int(input(""))
    print("calculating.....")
    m=math.isqrt(v)
    if m**2!=v:
        print("it is not a perfect square")
        break
    print("√",m,"^2")
    print("calculated successfully!!!")

