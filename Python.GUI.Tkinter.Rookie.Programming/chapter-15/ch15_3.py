# ch15_3.py
from tkinter import *
from tkinter.ttk import *

def load():                     # 启动Progressbar
    # global bytes 
    # bytes = 0
    pb["value"] = 0             # Progressbar初始值
    pb["maximum"] = maxbytes    # Progressbar最大值
    loading()
def loading():                  # 仿真下载数据
    global bytes
    bytes += 500                # 模拟每次下载500B
    pb["value"] = bytes         # 设置指针
    if bytes < maxbytes:
        pb.after(50,loading)    # 经过0.05秒继续执行loading

root = Tk()
root.title("ch15_3")
bytes = 0                   # 设置初值
maxbytes = 10000            # 假设下载文件大小

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=10,pady=10)
pb["value"] = 0  # Progressbar初始值

btn = Button(root,text="Load",command=load)
btn.pack(pady=10)

root.mainloop()

