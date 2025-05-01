# ch2_10.py
from tkinter import *

root = Tk()
root.title("ch2_10")
label=Label(root, text="abcdefghijklmnopqrstuvwy",
            fg="blue", bg="lightyellow",
            wraplength=80,
            justify="center")
label.pack()

root.mainloop()
