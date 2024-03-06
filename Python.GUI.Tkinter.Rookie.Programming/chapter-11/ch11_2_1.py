# ch11_2_1.py
from tkinter import *
def mouseMotion(event):                     # Mouse移动
    x = event.x
    y = event.y
    textvar = "当前鼠标位置 -> x:{}, y:{}".format(x,y)
    var.set(textvar)

root = Tk()
root.title("ch11_2_1")                  # 窗口标题    
root.geometry("300x180")

x, y = "###", "###"
var = StringVar()
text = "当前鼠标位置 -> x:{}, y:{}".format(x,y)
var.set(text)

lab = Label(root,textvariable=var,bg="yellow")  # 建立标签
lab.pack(anchor=S,side=RIGHT,padx=10,pady=10) # lab.pack(anchor=S,side=RIGHT,padx=10,pady=10)
# root.bind("<Motion>",mouseMotion)
root.bind("<Button-1>",mouseMotion)   # 添加事件处理程序  # "<Motion>"
root.bind("<Button-3>",mouseMotion)
# "<B1-Motion>"  
root.mainloop()
