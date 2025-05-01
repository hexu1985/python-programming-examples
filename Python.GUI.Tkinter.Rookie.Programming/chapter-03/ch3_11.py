# ch3_11.py
from tkinter import *

window = Tk()
window.title("ch3_11")
lab1 = Label(window, text="明志科技大学",
            bg="lightyellow")
lab2 = Label(window, text="长庚大学",
            bg="lightgreen")
lab3 = Label(window, text="长庚科技大学",
            bg="lightblue")
lab1.pack()
lab2.pack(ipadx=10)
lab3.pack(ipady=10)

window.mainloop()
