from tkinter import *
from datetime import date, datetime
import os

os.chdir("F:\\Downloads\\Python apps\\TODO App")
root = Tk()
_time = datetime.now()
Time = datetime.strftime(_time, "%H:%M:%S")
print(Time)
root.title("TODO Application")
root.geometry("400x400")
Enter_task = Label(root, text="Enter your task", anchor=CENTER)
Enter_task.pack(pady=10)
T_TODO = Entry(root)
T_TODO.pack()
Enter_Time = Label(root, text="Enter the time you want to do the work.")
Enter_Time.pack()
Task_name = Entry(root)
Task_name.pack()

TTime = StringVar()
def Remind():
    Task = open("Task.txt", "w")
    Task.write(T_TODO.get())
    Time_ = open("TIME.txt", "w")
    Time_.write(Task_name.get())
    R_Time = open("TIME.txt", "r")
    TTime.set(R_Time.read())
    os.startfile("TODOAPPMAinf.py")

Submit_Bt = Button(root, text="Submit", padx=10, pady=10, bg="Red", command=Remind)

Submit_Bt.pack(pady=10)

root.mainloop()