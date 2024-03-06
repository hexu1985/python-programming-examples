# ch19_5.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()

canvas.create_line(30,30,500,30,width=50,stipple="gray25")
canvas.create_line(30,130,500,130,width=50,stipple="questhead")
canvas.create_line(30,230,500,230,width=50,stipple="info")
tk.mainloop()

