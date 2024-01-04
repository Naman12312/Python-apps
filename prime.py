

def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        isprime = True
        for j in range(2, i):
            if i%j == 0:
                isprime=False   
                break
            else:
                primes.append(i)
              # Only appends if the inner loops has ended.

                
    return primes

prime_list = prime_numbers(50)
print(prime_list)


"""

i = 2
j = i-1 = 1
the loop will iterate from 2 to 1 and will not execute any code.

i = 3
j = 2

3%2 = 1

appended,

i = 4
j = 2

4%2 = 0
loop breaks
not appended,


i = 5
j = 2

5%2=1 isprime is still True
5%3=2 isprime is still True
5%4=1 isprime is still True

appended


and so on...


"""


"""
the problem with the previous program:
i = 9
j = 2
i%j = 9%2!=0 so it appends it and moves on to the next iteration


but then it checks it for 3 and it seems to be composite, 
but the last number was already appended.
"""