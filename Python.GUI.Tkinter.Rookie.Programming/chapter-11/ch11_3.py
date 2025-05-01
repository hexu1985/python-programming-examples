# ch11_3.py
from tkinter import *
def enter(event):                     # Enter事件处理程序  
    x.set("鼠标进入Exit功能按钮")
def leave(event):                     # Leave事件处理程序
    x.set("鼠标离开Exit功能按钮")
def myExit(event):
    print("程序退出cxq")
    root.destroy()

root = Tk()
root.title("ch11_3")                  # 窗口标题    
root.geometry("900x540")
# btn = Button(root,text="Exit",command=root.destroy)
btn = Button(root,text="Exit")  
btn.bind("<Button-1>",myExit)
btn.pack(pady=30)
btn.bind("<Enter>",enter)     # 进入绑定enter
btn.bind("<Leave>",leave)     # 离开绑定leave

x = StringVar()
x.set("初始状态...")
lab = Label(root,textvariable=x,
            bg="yellow",fg="blue",
            height=4,width=50,
            font="Times 12 bold")  # 建立标签
lab.pack(pady=30) 
 
root.mainloop()
