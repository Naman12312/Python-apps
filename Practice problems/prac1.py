"""
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of module like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sorts of errors like :            (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!
"""
while True:    
    a = int(input("Enter your age or year of birth: "))
    ab = int(input("Enter current year:"))
    abou = input("Do you want to provide a particular year??? Y/N")
    if abou=='n' or 'N':
        if len(str(a))==4:
            if a>ab:
                print("You are not yet born")
            else:
                yearfor100 = ab+(100-(ab-a))
                print(f"You will turn 100 in {yearfor100}")
        elif len(str(a))<4:
            yearfor100 = ab+(100-a)
            if a>110:
                print("you seem to be the oldest person yet")
            elif a<100:
                print(yearfor100)
            elif a>100:
                print("You are already above 100")
        
    elif abou=="Y" or 'y':
        op = int(input("Enter the year: "))
        if len(str(a)) == 4:
            if op>ab:
                yearfor100 = (ab-a)+op-ab
                print(f"You will turn {yearfor100} in {op}")
            elif op<ab:
                yearfor100 = (ab-a)+op-ab
                print(f"You were {yearfor100} in {op}")
        elif len(str(a))<4:
            yearfor100 = (a+op-ab)
            print(yearfor100)
    else:
        print("Invalid input please enter again")
    yearfor100 = ab+(100-a)

    if len(str(a))==4:
        if a>ab:
            print("You are not yet born")
        else:
            yearfor100 = ab+(100-(ab-a))
            print(f"You will turn 100 in {yearfor100}")
    elif len(str(a))<4:
        yearfor100 = ab+(100-a)
    elif a>110:
        print("you seem to be the oldest person yet")
    elif a<100:
        print(yearfor100)
    elif a>100:
        print("You are already above 100")


