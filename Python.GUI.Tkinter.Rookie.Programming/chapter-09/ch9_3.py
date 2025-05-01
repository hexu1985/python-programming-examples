# ch9_3.py
from tkinter import *

def printInfo():
    print("垂直尺度值 = %d, 水平尺度值 = %d" % (sV.get(),sH.get()))

root = Tk()
root.title("ch9_3")                           # 窗口标题 

sV = Scale(root,label="垂直的滑块",from_=0,to=10)   # 建立垂直尺度
sV.set(5)                                     # 设定垂直尺度初始值是5
sV.pack()

sH = Scale(root,label="水平的滑块",from_=0,to=10,
            length=300,orient=HORIZONTAL)
sH.set(3)             
sH.pack()              

Button(root,text="打印两个滑块上的数值",command=printInfo).pack()

root.mainloop()
