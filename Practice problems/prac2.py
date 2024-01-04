"""
Harry Potter has got the “n” number of apples. Harry has some students among whom he wants to distribute the apples. These “n” number of apples is provided to harry by his friends, and he can request for few more or a few less apples.

You need to print whether a number is in range mn to mx, is a divisor of “n” or not.


Input:

Take input n, mn, and mx from the user.

Output:
Print whether the numbers between mn and mx are divisors of “n” or not. If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.

Example:
If n is 20 and mn=2 and mx=5

2 is a divisor of20

3 is not a divisor of 20

…

5 is a divisor of 20
"""
n = int(input("Enter how many apples do you have?\t"))
mn = int(input("Enter minimum no of apples each student can get:\t"))
mx = int(input("Enter the maximum no of apples each student can get\t"))
for i in range(mn,mx+1):
    if mn==mx:
        print("This is not a range mn is equal to mx")
    if n%i == 0:
        print(f"{i} is a divisor of {n}")
    else:
        print(f"{i} is not a divisor of {n}")