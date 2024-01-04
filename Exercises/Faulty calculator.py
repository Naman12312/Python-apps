print("Welcome to the calculator!!!!")
fn=int(input("Enter first number:\t"))
sn=int(input("Enter second number:\t"))
op=input("What do you want to do??? options are:\n+:plus\n-:minus\n*:multiply\n/:divide\n**:power")
if fn==45 and sn==3 and op=="*":
    print("Result is:",555)
elif fn==56 and sn==9 and op=="+":
    print("Result is:",77)
elif fn==56 and sn==6 and op=="/":
    print("Result is:",44)
elif op=="+":
    print("Result is:",fn+sn)
elif op=="-":
    print("Result is:",fn-sn)
elif op=="*":
    print("Result is:",fn*sn)
elif op=="/":
    print("Result is:",fn/sn)
elif op=="**":
    print("Result is:",fn**sn)
elif op=="%":
    print("Result is:",fn*sn/100)
else:
    print("Wrong input!")