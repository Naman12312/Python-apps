# a = input("What is Your name?\n")
# b = input("How much do you earn?\n")
# if int(b)==0:
#     raise ZeroDivisionError("B is 0 so stoppping the program.")
# if a.isnumeric():
#     raise Exception("Numbers are not allowed.")
# print(f"Hello, {a}.")
# a = input("Enter A number:\n")
# if a.isspace() or a=="":
#     raise NameError("Spaces are not allowed.")
# elif not a.isnumeric():
#     raise ValueError("Strings are not allowed.")
# b = input("Enter a floating point number:\n")
# if b.isnumeric():
#     raise ArithmeticError("Integers are not allowed.")

c = input("Enter Your Name:\n")
try:
    print(a)
except Exception as e:
    if c=="Harry" or c=="harry":
        raise ValueError("Harry is not allowed. He is blocked")
    # else:
    print("Exception handled.")
