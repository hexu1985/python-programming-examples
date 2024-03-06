# ch10_4.py
from tkinter import *
from tkinter import messagebox

def myMsg():                    # 单击Good Morning按钮时执行
    result = messagebox.showinfo("自定义消息框的标题","欢迎开启 Python Tkinter 的学习之旅!!!")
    print("消息盒子返回的值是: ",result)

root = Tk()
root.title("ch10_4")                 # 窗口标题    
root.geometry("300x160")             # 窗口宽300高160

Button(root,text="打招呼",command=myMsg).pack()

root.mainloop()
