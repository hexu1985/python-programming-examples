# ch15_1.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x140")
root.title("ch15_1")

# 使用默认设置创建进度条
pb1 = Progressbar(root)
pb1.pack(pady=20)
pb1["maximum"] = 100
pb1["value"] = 50

# 使用各参数自定义方式创建进度条
pb2 = Progressbar(root,orient=HORIZONTAL,length=200,mode="determinate")
pb2.pack(pady=20)
pb2["maximum"] = 100
pb2["value"] = 50

root.mainloop()

