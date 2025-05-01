# ch3_15.py
from tkinter import *

window = Tk()
window.title("ch3_15")
lab1 = Label(window, text="明志科技大学",
            bg="lightyellow")
lab2 = Label(window, text="长庚大学",
            bg="lightgreen")
lab3 = Label(window, text="长庚科技大学",
            bg="lightblue")
lab1.pack(fill=X)
lab2.pack(fill=Y)
lab3.pack(fill=X)

window.mainloop()
