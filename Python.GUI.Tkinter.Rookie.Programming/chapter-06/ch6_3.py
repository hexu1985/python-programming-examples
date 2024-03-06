# ch6_3.py
from tkinter import *

def callback(*args):  # 如果是 def callback(): 则会出错
    print("data changed: ",xE.get())   # 在命令行输出当前内容

root = Tk()
root.title("ch6_3")                    # 窗口标题

xE = StringVar()                       # Entry的变量内容
entry = Entry(root,textvariable=xE)    
entry.pack(pady=5,padx=10)
xE.trace("w",callback)                 # 若有更改则执行callback

root.mainloop()

