# ch6_5.py
from tkinter import *

def callbackW(*args):               # 内容被更改时执行
    # xE.get()
    xL.set(xE.get())                # 更改标签内容

def callbackR(*args):               # 内容被读取时执行
    print("Warning:数据被读取!")

def hit():                          # 读取数据
    print("读取数据:",xE.get())
    # print("类型是：",type(xE.get()))  # 类型是： <class 'str'>
    # print("读取数据2:",xE.get())
    # print("读取数据3:",xE.get())


# def callback(*args):  # 如果是 def callback(): 则会出错
#     xL.set(xE.get())
#     print("data changed: ",xE.get())   # 在命令行输出当前内容

root = Tk()
root.title("ch6_5")                                    # 窗口标题

xE = StringVar()                                       # Entry的变量内容
entry = Entry(root,textvariable=xE)                    # 设定Label内容是变量x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                                # 若是有更改执行callbackW
xE.trace("r",callbackR)                                # 若是有被读取执行callbackR


xL = StringVar()                                       # Label的变量内容
label = Label(root,textvariable=xL)
xL.set("同步显示")
label.pack(pady=5,padx=10)

btn = Button(root,text="读取",command=hit)             # 创建"读取"按钮
btn.pack(pady=5)

root.mainloop()

"""
疑问：
xE.trace("w",callbackW)中callbackW(*args)内部也执行了xE.get(),
为什么不会激发callbackR(*args)函数的运行？
"""

