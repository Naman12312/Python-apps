from tkinter import *
root = Tk()
root.title("Newspaper")
root.geometry("1294x633")
images = PhotoImage(file="F:\\downloads\\hello.png")
root.minsize(1294,633)
Label(text="Today's news...").pack()
Label(root,text="1/26/2021").pack(anchor="nw",side=LEFT)
l = Label(root,image=images)
l.pack()
Label(root,text='''India is celebrating its 72nd Republic Day on Tuesday across the country, \nalbeit in a muted manner due to the pandemic. Meanwhile, farmers protesting the newly-passed agricultural laws have gathered in Delhi to participate in the tractor rally.

Delhi Police has advised people to watch the live telecast of Republic Day parade at home due to COVID-19 protocols. Invitees attending parade at Rajpath have to comply with the COVID-19 advisory that includes temperature check,\n use of sanitiser, mask and social distancing.

This time, there would not be a chief guest at the Republic Day parade. Additionally, the route of the marching contingent will end at the India Gate C-Hexagon instead of Red Fort.)''',padx=10,pady=10,fg='black',bg='red').pack(fill=X,anchor='nw',side=LEFT)
root.mainloop()