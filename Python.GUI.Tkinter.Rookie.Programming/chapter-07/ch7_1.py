# ch7_1.py
from tkinter import *
def printSelection():
    num = var.get()
    if num == 1:
        label.config(text="你是男生")
    else:
        label.config(text="你是女生")

root = Tk()
root.title("ch7_1")    # 设置窗口标题

var = IntVar()         # 选项按钮绑定的变量
var.set(1)             # 默认选项是男生
# var.set(0)           # 可以设置初始不默认任何选项 
label = Label(root,text="这是预设，尚未选择",bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生",                  # 男生选项按钮
                    variable=var,value=1,              # value用来区分所选择的选项按钮 
                    command=printSelection)            # 女生选项按钮
rbman.pack()
rbwoman = Radiobutton(root,text="女生",
                    variable=var,value=2,
                    command=printSelection)
rbwoman.pack()

root.mainloop()

