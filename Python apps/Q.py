import random
num=random.randint(0,100)
while True:
    print ("guess a number between 1 and 100")
    guess=input()
    i=int(guess)
    if i==num:
        print("you guessed right")
        break
    elif i<num:
        print ("try higher")
    elif i>num:
        print("try smaller")
        
