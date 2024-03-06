# ch19_1.py
from tkinter import *
import math

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()
x_center, y_center, r = 320, 240, 100
x, y = [], []
for i in range(12):    # 建立圆外围12个点
    x.append(x_center + r * math.cos(30*i*math.pi/180))   # x = x0 + r * cos(A)
    y.append(y_center + r * math.sin(30*i*math.pi/180))   # y = y0 + r * sin(A)
for i in range(12):    # 将12个点彼此连线
    for j in range(12):
        canvas.create_line(x[i],y[i],x[j],y[j])

tk.mainloop()

