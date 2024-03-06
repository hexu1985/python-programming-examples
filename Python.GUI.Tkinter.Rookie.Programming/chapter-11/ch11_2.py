# ch11_2.py
from tkinter import *
def callback(event):                     # 事件处理程序
    print("Clicked at",event.x,event.y)  # 打印坐标

root = Tk()
root.title("ch11_2")   # 窗口标题    
frame = Frame(root,width=300,height=180,bg="yellow")
frame.bind("<Button-1>",callback)   # 绑定callback
frame.pack()

root.mainloop()

