while True:
    try:
        input1=input("Enter Your choice: \t")
        x=eval(input1)
        print(f"Result is: {x}")
    except Exception as e:
        print(e)
        print("Error!")