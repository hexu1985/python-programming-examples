# ch9_2.py
from tkinter import *

root = Tk()
root.title("ch9_2")                         # 窗口标题 

slider = Scale(
                root,
                from_=0,                    # 起点值
                to=20,                      # 终点值
                troughcolor="yellow",       # 槽的颜色
                width="30",                 # 槽的高度
                tickinterval=2,             # 刻度
                label="My Scale",           # Scale标签
                length=300,                 # Scale长度
                orient=HORIZONTAL           # 水平
            )
slider.pack()

root.mainloop()
