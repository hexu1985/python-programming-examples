# ch12_17.py
from tkinter import *
def itemSelected(event):           # 列出所选单一项目
    obj = event.widget             # 取得事件的对象,即Listbox控件对象
    index = obj.curselection()     # 取得索引
    print(index)
    print(type(obj.get(index)))
    print(obj.get(index))
    var.set(obj.get(index))        # 设置标签内容

fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_17")        # 窗口标题  
root.geometry("300x250")     # 窗口宽300高210  

var = StringVar() 
# var.set("cxq123") 
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root)                 
for fruit in fruits:         # 建立水果项目
    lb.insert(END,fruit)
lb.bind("<Double-Button-1>",itemSelected)  # 绑定
lb.pack(pady=5)

root.mainloop()

