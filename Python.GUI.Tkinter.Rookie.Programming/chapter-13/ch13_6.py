# ch13_6.py 
from tkinter import * 
from tkinter.ttk import *

root = Tk()
root.title("ch13_6")                              # 窗口标题
root.geometry("300x120")

var = StringVar()
cb = Combobox(root,textvariable=var)              # 创建Combobox
cb["value"] = ("Python","Java","C#","C","C++")    # 设置选项内容
cb.pack(pady=10)

root.mainloop()

