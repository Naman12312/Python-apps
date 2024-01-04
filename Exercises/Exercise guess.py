num=25
life=5
for i in range(9):
    print("Lives left:",life)
    x=int(input("Guess a number"))
    if x>num:
        print("Try lesser")
        life=life-1
    elif x<num:
        print("Try higher")
        life=life-1
    if life==0:
        print("Game over!")
        break
    elif x==num:
        print("You guessed right!")
        break