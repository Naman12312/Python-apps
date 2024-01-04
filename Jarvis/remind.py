import datetime
from plyer import notification
import os
os.chdir("F:\\Downloads\\Python apps\\Jarvis")
R_Time = open("TTime.txt", "r")
TTTask = open("Task23.txt", "r")
mtime = datetime.datetime.now().strftime("%H:%M")
a = R_Time.read()
while True: 
    mtime = datetime.datetime.now().strftime("%H:%M")   
    if a==mtime:
        notification.notify(
            title = "Jarvis",
            message = f"Time to {TTTask.read()}!",
            timeout = 5
        )
        break
    
   

