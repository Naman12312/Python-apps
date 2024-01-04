from tkinter import *
root = Tk()
root.geometry("644x256")
root.title("Scrollbar")
'''
widget = widget(root,yscrollcommand = scrollbar.set)
scrollbar.config(command=widget.yview)
'''
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,fill='y')
text = Text(root,yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
root.mainloop()