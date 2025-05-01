# ch19_17.py
from tkinter import * 
import time

tk = Tk()
canvas = Canvas(tk,width=500, height=300)  # 建立画布
canvas.pack()
canvas.create_oval(10,50,60,100,fill="yellow",outline='lightgray')
for x in range(0,80):
    canvas.move(1,5,2)   # ID=1  x轴移动5像素，y轴移动2像素
    tk.update()          # 强制tkinter重绘
    time.sleep(0.05)

# tk.mainloop()

