# ch14_7.py
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def msg():
    messagebox.showinfo("Notebook","欢迎使用Notebook")

root = Tk()
root.title("ch14_7")
root.geometry("300x160")

notebook = Notebook(root)             # 创建Notebook

frame1 = Frame()        # 创建Frame1 # frame1 = Frame(root) # 没有发现有区别
frame2 = Frame()        # 创建Frame2 # frame2 = Frame(root) # 没有发现有区别

label = Label(frame1,text="Python")   # 在Frame1中创建标签控件
label.pack(padx=10,pady=10)
btn = Button(frame2,text="Help",command=msg)
btn.pack(padx=10,pady=10)

# notebook.add的调用顺序决定了布局的顺序
# notebook.add(frame2,text="页次2") # 创建选项卡2同时插入Frame2
notebook.add(frame1,text="页次1") # 创建选项卡1同时插入Frame1
notebook.add(frame2,text="页次2") # 创建选项卡2同时插入Frame2
notebook.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

root.mainloop()

