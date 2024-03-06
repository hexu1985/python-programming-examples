# ch11_6.py
from tkinter import * 
def key(event):                     # 处理键盘按a-z键事件
    print("按了 " + repr(event.char) + " 键")

def coordXY(event):
    frame.focus_set()
    print("鼠标坐标：",event.x,event.y)

root = Tk()
root.title("ch11_6")                  # 窗口标题    

frame = Frame(root,width=100,height=100)
frame.bind("<Key>",key)
frame.bind("<Button-1>",coordXY)
frame.pack()

root.mainloop()
