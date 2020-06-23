
from tkinter import *
import random

counter1 = 0

def counter_fun():
    global counter1
    counter1 += 1
    counter.set(str(counter1))

master = Tk()

counter = StringVar()
counter.set(str(0))
btn=Button(master, text="This is Button widget", fg='blue',command= counter_fun)
btn.place(x=80, y=100)
btn.pack()

text = Label(master, textvariable = counter)
text.pack()

master.title('Magic Conch')
master.geometry("300x200+10+10")
master.mainloop()

