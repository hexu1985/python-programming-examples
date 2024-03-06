# ch3_7.py
from tkinter import *

window = Tk()
window.title("ch3_7")
lab1 = Label(window, text="明志科技大学",
            bg="lightyellow")
lab2 = Label(window, text="长庚大学",
            bg="lightgreen")
lab3 = Label(window, text="长庚科技大学",
            bg="lightblue")
lab1.pack(fill=X,pady=10)
lab2.pack(pady=10)
lab3.pack(fill=X)

window.mainloop()
