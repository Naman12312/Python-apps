import os
os.startfile("F:\\downloads\\Python apps\\ostut.py")
print(dir(os))
print(os.getcwd())
os.chdir("C:\\")
print(os.getcwd())
f = open("harry.txt")
print(os.listdir("C:\\"))
os.mkdir("This")
os.makedirs("This\\That")
os.rename("harry.txt", "CodeWithHarry.txt")
print(os.environ.get("Path"))
print(os.path.join("C:\\", "/Harry.txt"))
print(os.path.exists("C:\\"))
print(os.path.isfile("F:\\downloads\\icon.ico"))
print(os.path.isdir("F:\\downloads\\"))
print(x)
for i,i1 in enumerate(x):
    er = os.path.splitext((x[i]))[1]
    eer = os.path.splitext((x[i]))[0]
    if er==".jpg":
        # print(eer)
        os.rename(eer, str(i)+".jpg")
os.rename("CodeWithHarry.txt","harry.txt")

