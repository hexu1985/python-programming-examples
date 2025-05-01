# ch7_2.py
from tkinter import *
def printSelection():
    label.config(text="你是"+var.get())

root = Tk()
root.title("ch7_2")    # 设置窗口标题

var = StringVar()         # 选项按钮绑定的变量
var.set("男生")             # 默认选项是男生
# var.set("生")             # 默认选项是空
# var.set(0)           # 可以设置初始不默认任何选项 
label = Label(root,text="这是预设，尚未选择",bg="lightyellow",width=30)
label.pack()

rbman = Radiobutton(root,text="男生-吴彦祖",                  # 男生选项按钮
                    variable=var,value="男生",              # value用来区分所选择的选项按钮 
                    command=printSelection)            # 女生选项按钮
rbman.pack()
rbwoman = Radiobutton(root,text="女生-刘亦菲",
                    variable=var,value="女生",
                    command=printSelection)
rbwoman.pack()

root.mainloop()

