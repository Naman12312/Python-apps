import os
import shutil
pi = input("Enter a directory path:\n")
os.chdir(pi)
os.mkdir("Py files")
os.mkdir("Text files")
os.mkdir("Docs files")
os.mkdir("powerpoint files")
os.mkdir("excel files")
os.mkdir("wav files")
os.mkdir("mp3 files")
os.mkdir("exe files")
os.mkdir("Others")
a = os.listdir()
for i in a:
    if os.path.splitext(os.path.join(pi, i))[1] ==".py":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "Py files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".txt":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "Text files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".docx":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "Docs files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".pptx":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "powerpoint files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".wma":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "wma files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".wav":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "wav files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".mp3":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "mp3 files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".exe":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "exe files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".xlsx":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "excel files"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".png":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "images"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".jpg":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "images"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".jpeg":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "images"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".bmp":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "images"))
    if os.path.splitext(os.path.join(pi, i))[1] ==".gif":
        shutil.move(os.path.join(pi, i), os.path.join(pi, "images"))
    else:
        shutil.move(os.path.join(pi, i), os.path.join(pi, "Others"))
print("Folder cleaned!")
        