# ch15_2.py
from tkinter import *
from tkinter.ttk import *
import time

def running():                   # 开始Progressbar动画
    for i in range(100):
        pb["value"] = i + 1      # 每次更新1
        root.update()            # 更新画面
        time.sleep(0.05)

root = Tk()
# root.geometry("300x140")
root.title("ch15_2")

# 使用默认设置创建进度条
pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=20)
pb["maximum"] = 100
pb["value"] = 0

btn = Button(root,text="Running",command=running)
btn.pack(pady=10)

root.mainloop()

