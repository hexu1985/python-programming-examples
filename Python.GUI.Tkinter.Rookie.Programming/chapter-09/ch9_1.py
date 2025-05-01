# ch9_1.py
from tkinter import *

window = Tk()
window.title("ch9_1")  
# window.geometry("300x180")
slider1 = Scale(window,from_=0,to=10).pack()
slider2 = Scale(window,from_=0,to=100,
            length=300,orient=HORIZONTAL).pack()

window.mainloop()
