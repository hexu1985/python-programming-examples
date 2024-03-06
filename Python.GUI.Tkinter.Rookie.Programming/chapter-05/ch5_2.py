from tkinter import *

root = Tk()
root.title("ch5_2")                      # 窗口标题

accountL = Label(root,text="Account")         # name标签
accountL.grid(row=0)                        # 默认是 column=0
pwdL = Label(root,text="Password")    # address标签
pwdL.grid(row=1)                     # 默认是 column=0

accountE = Entry(root)                      # name文本框
pwdE = Entry(root,show="*")                   # address文本框
accountE.grid(row=0,column=1)               # 定位name文本框
pwdE.grid(row=1,column=1)            # 定位address文本框

root.mainloop()


