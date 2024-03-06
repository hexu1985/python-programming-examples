# ch6_2.py
from tkinter import *

def btn_hit():                    # 处理按钮事件
    if x.get() == "":             # 如果当前是空字符串
        x.set("I like tkinter")   # 显示文字
    else:
        x.set("")                 # 不显示文字

root = Tk()
root.title("ch6_2")               # 窗口标题

x = StringVar()                   # Label的变量内容

label = Label(root,textvariable=x,             # 设置Label内容是变量x
                fg="blue",bg="lightyellow",    # 浅黄色底蓝色字
                font="Verdana 16 bold",        # 字形设置
                width=25,height=2)             # 标签内容

label.pack()
btn = Button(root,text="Click Me",command=btn_hit)
btn.pack()
root.mainloop()

