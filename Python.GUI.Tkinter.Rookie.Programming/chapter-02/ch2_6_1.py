# ch2_6.py
from tkinter import *

root = Tk()
root.title("ch2_6")
label=Label(root, text="I like tikinter",
            fg="blue", bg="yellow",
            height=3, width=15,
            anchor=SE)
label.pack()

root.mainloop()
