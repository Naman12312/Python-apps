def program():    
    row=int(input("0=simple,1=inverted"))
    boolean = bool(row)
    if not boolean:
        # print("\n")
        x=int(input("How many rows do you want?\t"))
        x=x+1
        # print("\n")
        for i in range(0,x):
            for i in range(i):
                    print("* ", end="")
            print("\n")

    elif boolean:
        # print("\n")
        v=int(input("How many rows do you want?\t"))
        v=v+1
        # print("\n")
        for b in range(v, 0, -1):
            print("*"*b)


if __name__ == "__main__":
    while True:    
        program()
