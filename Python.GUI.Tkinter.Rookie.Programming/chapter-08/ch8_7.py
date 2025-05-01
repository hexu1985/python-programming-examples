# ch8_7.py
from tkinter import *

root = Tk()
root.title("ch8_7")                      # 窗口标题

msg = "Welcome to Python GUI tkinter Learning System!!!"
myGif = PhotoImage(file="sse.png")   # Logo图像文件
logo = Label(root,image=myGif,text=msg,compound=BOTTOM)
logo.pack()

# 以下是LabelFrame标签框架
labFrame = LabelFrame(root,text="数据验证")        # 创建框架标签
accountL = Label(labFrame,text="Account")         # name标签
accountL.grid(row=0,column=0)                        # 默认是 column=0
pwdL = Label(labFrame,text="Password")    # address标签
pwdL.grid(row=1,column=0)                     # 默认是 column=0

accountE = Entry(labFrame)                      # name文本框
accountE.grid(row=0,column=1)
pwdE = Entry(labFrame,show="*")                   # address文本框
pwdE.grid(row=1,column=1,pady=10)            # 定位address文本框
labFrame.pack(padx=10,pady=5,ipadx=5,ipady=5)

root.mainloop()
