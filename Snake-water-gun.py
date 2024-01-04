import random
def main_game():
    x1=0
    x=0
    while True:
        choice=['snake','water','gun']
        you=input("Snake, Water or Gun???\t")
        comp = random.choice(choice)
        print(f"You:{you}")
        print(f"CPU:{comp}")
        if comp=="snake" and you=="water":
            print("you lose!!!")
            x1+=1
        elif comp=="snake" and you=="gun":
            print("you win!!!")
            x+=1
        elif comp=="water" and you=="gun":
            print("you lose!!!")
            x1+=1
        elif comp=="water" and you=="snake":
            print("you win!!!")
            x+=1
        elif comp=="gun" and you=="snake":
            print("you lose!!!")
            x1+=1
        elif comp=="gun" and you=="water":
            print("you win!!!")
            x+=1
        elif you==comp:
            print("tie!!!")
        if you=="exit":
            print(f"Your score:{x}")
            print(f"CPU score:{x1}")
            if x>x1:
                print("You are the winner!!!")
            elif x1>x:
                print("I am the winner!!!")
            break
main_game()
