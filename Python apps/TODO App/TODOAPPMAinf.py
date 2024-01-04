import datetime
from plyer import notification
R_Time = open("TIME.txt", "r")
TTTask = open("Task.txt", "r")
mtime = datetime.datetime.now().strftime("%H:%M")
a = R_Time.read()
while True: 
    mtime = datetime.datetime.now().strftime("%H:%M")   
    if a==mtime:
        notification.notify(
            title = "TODO",
            message = f"Time to {TTTask.read()}!",
            timeout = 5
        )
        break
