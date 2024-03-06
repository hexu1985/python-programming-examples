from tkinter import *

root = Tk()
root.title("ch5_1")                      # 窗口标题

nameL = Label(root,text="Name ")         # name标签
nameL.grid(row=0)                        # 默认是 column=0
addressL = Label(root,text="Address")    # address标签
addressL.grid(row=1)                     # 默认是 column=0

nameE = Entry(root)                      # name文本框
addressE = Entry(root)                   # address文本框
nameE.grid(row=0,column=1)               # 定位name文本框
addressE.grid(row=1,column=1)            # 定位address文本框

root.mainloop()


