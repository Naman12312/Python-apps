def main():    
    import datetime
    def getDate():
        return datetime.datetime.now()
    print("Welcome to the health manager who is here???(harry) or (rohan) or (naman)")
    input1=input()
    print("What do you want to lock options are:\nDiet\nExercise")
    input2=input()
    if input2=="diet":
        print("What so you want to do? options are \nlock\nretrive")
        inpute=input()
        if inpute=="lock":
            print("What you ate???")
            input3=input()
            getDate()
            if input1=="harry":
                with open("harry.txt","w") as f:
                    f.write(input3)
                print("Congratulations! we have successfully noticed that! you ate",input3,"on",getDate())
            elif input1=="rohan":
                with open("rohan.txt","w") as f:
                    f.write(input3)
                print("Congratulations! we have successfully noticed that! you ate",input3,"on",getDate())
            elif input1=="naman":
                with open("naman.txt","w") as f:
                    f.write(input3)
                print("Congratulations! we have successfully noticed that! you ate",input3,"on",getDate())
        elif inpute=="retrive":
            if input1=="harry":
                with open("harry.txt","r") as f:
                    harry=f.read()
                print("You ate:",harry)
            if input1=="rohan":
                with open("rohan.txt","r") as f:
                    rohan=f.read()
                print("You ate:",rohan) 
            if input1=="naman":
                with open("naman.txt","r+") as f:
                    naman=f.read()
                print("You ate:",naman)       
    elif input2=="exercise":
        print("What do you want to do? options are\nlock\nretrive")
        input4=input()
        if input4=="lock":
            print("Which exercise you have done???")
            input5=input()
            if input1=="naman":
                with open("naman1.txt","w") as f:
                    naman1=f.write(input5)
                    print("Congratulations! we have successfully noticed that! you done",input5,"on",getDate())
            if input1=="rohan":
                with open("rohan1.txt","w") as f:
                    rohan1=f.write(input5)
                    print("Congratulations! we have successfully noticed that! you done",input5,"on",getDate())
            if input1=="harry":
                with open("harry1.txt","w") as f:
                    harry1=f.write(input5)
                    print("Congratulations! we have successfully noticed that! you done",input5,"on",getDate())
        if input4=="retrive":
            if input1=="naman":
                with open("naman1.txt","r") as f:
                    naman2=f.read()
                print("You done:",input5)  
            if input1=="harry":
                with open("harry1.txt","r") as f:
                    harry2=f.read()
                print("You done:",input5)  
            if input1=="rohan":
                with open("rohan1.txt","r") as f:
                    rohan2=f.read()
                print("You done:",input5)
main()
x=input("Want to do anything or not?\t")
if x=="yes":
    main()
else:
    exit()



