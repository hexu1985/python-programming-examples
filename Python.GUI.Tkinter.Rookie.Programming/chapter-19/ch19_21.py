# ch19_21.py
from tkinter import * 
from random import * 
import time 

class Ball:#class Ball():#这样写是一样的
    def __init__(self,canvas,color,winW,winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color) # 建立球对象
        self.canvas.move(self.id,winW/2,winH/2)   # 设置球最初位置
    def ballMove(self):
        self.canvas.move(self.id, 0, step)        # step是正值表示往下移动

winW = 640      # 定义画布宽度
winH = 480      # 定义画布高度
step = 3        # 定义速度可想成位移步长
speed = 0.03    # 设置移动速度

tk = Tk()
tk.title("Bouncing Ball")                    # 游戏窗口标题
tk.wm_attributes('-topmost',1)               # 确保游戏窗口在屏幕最上层
canvas = Canvas(tk,width=winW, height=winH)  # 建立画布
canvas.pack()
tk.update()   

ball = Ball(canvas,'yellow',winW,winH)  # 定义球对象

while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)   # 可以控制移动速度

# tk.mainloop()

