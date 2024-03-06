# ch19_6.py
from tkinter import * 
from random import * 

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
for i in range(20):
    x1, y1 = randint(1,640), randint(1,480)
    x2, y2 = randint(1,640), randint(1,480)
    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2: 
        y1,y2 = y2,y1
    canvas.create_rectangle(x1,y1,x2,y2)
    # canvas.create_line(x1,y1,x2,y2)

tk.mainloop()

