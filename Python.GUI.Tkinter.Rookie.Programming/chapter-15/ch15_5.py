# ch15_5.py
from tkinter import *
from tkinter.ttk import *

def run():      # 开始Progressbar动画
    print("run()被执行！！！")
    pb.start()  # 指针每次移动1
def stop():     # 终止Progressbar动画
    print("stop()被执行！！！")
    pb.stop()   # 终止pb对象动画

root = Tk()
root.title("ch15_5")

pb = Progressbar(root,length=200,mode="determinate",orient=HORIZONTAL)
pb.pack(padx=5,pady=10)
pb["maximum"] = 100
pb["value"] = 0 

btnRun = Button(root,text="Run",command=run)     # 创建Run按钮
btnRun.pack(side=LEFT,padx=5,pady=10)

btnStop = Button(root,text="Stop",command=stop)  # 创建Stop按钮
btnStop.pack(side=LEFT,padx=5,pady=10)

root.mainloop()

