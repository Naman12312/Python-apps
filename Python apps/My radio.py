from tkinter import *
from tkinter.messagebox import *
# from Employee import *
root = Tk()
root.title("Naman orders")
root.geometry("544x400")
# print(Employee.officeisopen("Thursday"))
var = StringVar()
var.set("Radio")
def Order():
    ordered=showinfo("Order placed!!!",f"Order was successfull!!! for {var.get()}")
Label(root, text = "What do you want to eat sir????",font="comicsansms 20 italic",
    justify=LEFT,pady=10).pack()
Food=['Samosa','Dosa','Idli','Jalebi',"Aalu Paratha","Chole Chawal",'Dal Makhni','Pizza']
for x,item in enumerate(Food):    
    radio=Radiobutton(root,text=item,padx=2,pady=2,variable=var,value=item).pack(anchor="w")
Button(root,text="Order!!!",command=Order).pack(pady=10,anchor='w')
root.mainloop()