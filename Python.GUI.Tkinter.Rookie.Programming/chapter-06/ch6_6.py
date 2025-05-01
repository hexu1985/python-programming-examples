# ch6_6.py
from tkinter import *

def callbackW(name,index,mode):               # 内容被更改时执行
    xL.set(xE.get())                # 更改标签内容
    print("name = %r, index = %r, mode = %r" % (name,index,mode))


root = Tk()
root.title("ch6_6")                                    # 窗口标题

xE = StringVar()  

entry = Entry(root,textvariable=xE)                    # 设定Label内容是变量x
entry.pack(pady=5,padx=10)
xE.trace("w",callbackW)                                # 若是有更改执行callbackW

xL = StringVar()                                       # Label的变量内容
label = Label(root,textvariable=xL)
xL.set("同步显示")
label.pack(pady=5,padx=10)

root.mainloop()

