# Oh Soldier! prettify my folder!
import os
inr = input("Enter a path:\t")
iner = input("Enter the format of the files which you want to rename by numbers:\t")
file = input("Enter the name of the file where are name of the files which you don't want to change:\t")
os.chdir(inr)
# print(os.getcwd())
x = os.listdir()

name = os.path.join(inr, file)
for i, i1 in enumerate(x):
        if os.path.splitext(x[i])[1]==iner:
            os.rename(i1, str(i)+iner)
            # os.rename(file, file.capitalize())
        with open(file) as f:
            a = f.read()
        if a not in i1:
            os.rename(i1, i1.capitalize())
        if a=="":
            os.rename(i1, i1.capitalize())
        else:
            continue    
        # elif os.path.splitext(x[i])[1]==".jpeg":
        #     os.rename(i1, "Image"+str(i)+iner)
        # elif os.path.splitext(x[i])[1]==".jpg":
        #     os.rename(i1, "Image"+str(i)+iner)
        # else:    
            

x = os.listdir()
for t,i2 in enumerate(x):
    if os.path.isdir(x[t]):
        pass   
    # elif a not in x:
    #     os.rename(i2, i2.capitalize())
    # else:
    #     pass
print("Folder prettified!")
