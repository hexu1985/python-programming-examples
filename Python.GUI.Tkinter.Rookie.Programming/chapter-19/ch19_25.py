# ch19_25.py 
from tkinter import * 
from random import * 
import time 

class Ball:#class Ball():#这样写是一样的
    def __init__(self,canvas,color,winW,winH):
        self.canvas = canvas
        self.id = canvas.create_oval(0, 0, 20, 20, fill=color) # 建立球对象
        self.canvas.move(self.id,winW/2,winH/2)   # 设置球最初位置
        startPos = [-4, -3, -2, -1, 1, 2, 3, 4]   # 球最初x轴位移的随机数
        shuffle(startPos)                         # 打乱排序
        self.x = startPos[0]                      # 球最初水平移动单位
        self.y = step                             # 垂直移动单位
    def ballMove(self):
        self.canvas.move(self.id, self.x, self.y)        # step是正值表示往下移动
        ballPos = self.canvas.coords(self.id)
        if ballPos[0] <= 0:          # 侦测球是否超过画布左方
            self.x = step       
        if ballPos[1] <= 0:          # 侦测球是否超过画布上方
            self.y = step
        if ballPos[2] >= winW:       # 侦测球是否超过画布右方
            self.x = -step           
        if ballPos[3] >= winH:       # 侦测球是否超过画布下方
            self.y = -step
class Racket():
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15,fill=color)  # 球拍对象
        self.canvas.move(self.id, 270, 400)

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
racket = Racket(canvas,'purple')        # 定义紫色球拍
while True:
    ball.ballMove()
    tk.update()
    time.sleep(speed)   # 可以控制移动速度

# tk.mainloop()

