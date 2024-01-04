import os
import shutil
files  = os.listdir("C:\\Users\\NAMANS~1\\AppData\\Local\\Temp\\")
for i in files:
    shutil.rmtree(os.path.join("C:\\Users\\NAMANS~1\\AppData\\Local\\Temp\\"))
    # except Exception as e:
    #     pass
print(os.path.getsize("C:\\Users\\NAMANS~1\\AppData\\Local\\Temp\\"))