# ch10_5.py
from tkinter import *
from tkinter import messagebox

def myMsg1():                    # 单击Good Morning按钮时执行
    ret = messagebox.askretrycancel("Test1","安装失败，再试一次？")
    print("安装失败",ret)

def myMsg2():                    # 单击Good Morning按钮时执行
    ret = messagebox.askyesnocancel("Test2","编辑完成，是或否或取消？")
    print("编辑完成",ret)

root = Tk()
root.title("ch10_5")                 # 窗口标题    

Button(root,text="安装失败",command=myMsg1).pack()
Button(root,text="编辑完成",command=myMsg2).pack()

root.mainloop()
