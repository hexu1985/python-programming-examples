# ch12_16_1.py
from tkinter import *
def itemSelected(event):          # 列出所选单一项目
    index = lb.curselection()     # 取得索引
    var.set(lb.get(index))        # 设置标签内容

fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_16")        # 窗口标题  
root.geometry("300x250")     # 窗口宽300高210  

var = StringVar() 
# var.set("cxq123") 
lab = Label(root,text="",textvariable=var,bg="yellow")
lab.pack(pady=5)

lb = Listbox(root)                 
for fruit in fruits:         # 建立水果项目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected)  # 绑定
lb.pack(pady=5)

root.mainloop()

