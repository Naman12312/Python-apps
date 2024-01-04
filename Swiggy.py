from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Swiggy")
root.geometry("455x433")
var = StringVar()
var.set("Radio")
def order():
    tmsg.showinfo("Pay please..","You need to pay for the order")
    def pay():
        payment.destroy()
        tmsg.showinfo("Success!",f"Order Was successfull for {var.get()}")
    payment = Tk()
    payment.title("Payment mode..")
    Label(payment,text = "How would you want to payment???",font="calibri 19 bold").pack()
    Entry(payment,textvar=var).pack()
    Button(payment,text="Pay!!",command=pay).pack()
Label(root,text = "Welcome to Swiggy",font="lucida 19 bold",
justify=LEFT).pack()
Label(root,text = "What would you like to have sir???",font="lucida 19 bold",fg="Blue",
justify=LEFT).pack()
items = ("Dosa","Samosa","Naan","Chips","Namkeen","Aalu paratha","Chole Chawal","Rajma Chawal","Dal Chawal")
for item,i in enumerate(items):
    radio = Radiobutton(root,text=i,variable=var,value=i)
    radio.pack(anchor='nw')
Button(root,text="Order!",command=order).pack()



root.mainloop()