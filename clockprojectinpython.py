from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Einstein Says 'Time Is An Illusion'")

def time():
    string = strftime('%I:%M:%S %p') #for 24 hrs format use ('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)


label=Label(root, font=("ds-digital",80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()