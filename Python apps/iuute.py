# write a function to find the factorial of the given number
def factorial(n):
    p = 1
    for i in range(1,n+1):
        p*=i
    return p

print(factorial(10))
