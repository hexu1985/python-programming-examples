# ch13_9.py 
from tkinter import * 
from tkinter.ttk import *
def printSelection():  # 打印选择的结果
    print(var.get())

root = Tk()
root.title("ch13_9")                              # 窗口标题
root.geometry("300x120")

var = StringVar()
cb = Combobox(root,textvariable=var)              # 创建Combobox
cb["value"] = ("Python","Java","C#","C","C++")    # 设置选项内容
cb.current(0)
cb.pack(pady=10)

btn = Button(root,text="Print",command=printSelection)  # 创建按钮
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()

