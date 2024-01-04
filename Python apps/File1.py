print("Enter first number:")
num1=int(input())
print("Enter second number:")
num2=int(input())
print("What do you want to do options are: \n+\n-\n/\n*\n**")
option=input()
if option=="+":
    print(f"Result is {num1+num2}")
elif option=="-":
    print(f"Result is {num1-num2}")
elif option=="*":
    print(f"Result is {num1*num2}")
elif option=="/":
    print(f"Result is {num1/num2}")
elif option=='**':
    print(f"Result is {num1**num2}")
else:
    print("Wrong input")
# print(f"g{num1}   {num2}")