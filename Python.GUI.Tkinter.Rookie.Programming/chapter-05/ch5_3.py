from tkinter import *

root = Tk()
root.title("ch5_3")                      # 窗口标题

msg = "Welcome to Python GUI tkinter Learning System!!!"
myPic = PhotoImage(file="sse.png")
logo = Label(root,image=myPic,text=msg,compound=BOTTOM)

accountL = Label(root,text="Account")         # name标签
accountL.grid(row=1)                        # 默认是 column=0
pwdL = Label(root,text="Password")    # address标签
pwdL.grid(row=2)                     # 默认是 column=0


logo.grid(row=0,column=0,columnspan=2,pady=10,padx=10)
accountE = Entry(root)                      # name文本框
pwdE = Entry(root,show="*")                   # address文本框
accountE.grid(row=1,column=1)               # 定位name文本框
pwdE.grid(row=2,column=1,pady=10)            # 定位address文本框

root.mainloop()

