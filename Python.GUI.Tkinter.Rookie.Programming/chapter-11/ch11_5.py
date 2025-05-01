# ch11_5.py
from tkinter import *
def key(event):                     # 处理键盘按a-z键事件
    print("按了 " + repr(event.char) + " 键")

root = Tk()
root.title("ch11_5")                  # 窗口标题    

root.bind("<Key>",key) # <Key>键绑定key函数

root.mainloop()
