# ch14_6.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch14_6")
root.geometry("300x160")

notebook = Notebook(root)          # 创建Notebook

frame1 = Frame()                   # 创建Frame1
frame2 = Frame()                   # 创建Frame2

notebook.add(frame1,text="选项卡1") # 创建选项卡1同时插入Frame1
notebook.add(frame2,text="选项卡2") # 创建选项卡2同时插入Frame2
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()

