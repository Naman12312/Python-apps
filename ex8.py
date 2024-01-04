import os
inr = input("Enter a path:\t")
iner = input("Enter the format of the files:\t")
file = input("Enter the name of the file:\t")
os.chdir(inr)
print(os.getcwd())
x = os.listdir()
name = os.path.join(inr, file)
for i, i1 in enumerate(x):
        if os.path.splitext(x[i])[1]==".jpeg":
            os.rename(i1, "Image"+str(i)+".jpeg")
        elif os.path.splitext(x[i])[1]==".jpg":
            os.rename(i1, "Image"+str(i)+".jpg")
        os.rename(file, file.capitalize())
x = os.listdir()
for t in x:
    if os.path.isdir():
        pass   
    else:
        os.rename(t, t.capitalize())
    