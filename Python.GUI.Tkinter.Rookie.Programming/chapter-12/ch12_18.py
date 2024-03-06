# ch12_18.py
from tkinter import *
def itemSelected(event):           # 列出所选单一项目
    obj = event.widget             # 取得事件的对象,即Listbox控件对象
    indexs = obj.curselection()     # 取得索引
    # print(index)
    # print(type(obj.get(index)))
    # print(obj.get(index))
    # var.set(obj.get(index))        # 设置标签内容
    for index in indexs:
        print(obj.get(index)) 
    print("-------------")

fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_18")        # 窗口标题  
root.geometry("300x250")     # 窗口宽300高210  

var = StringVar() 
# var.set("cxq123") 
lab = Label(root,text="",textvariable=var)
lab.pack(pady=5)

lb = Listbox(root,selectmode=EXTENDED)                 
for fruit in fruits:         # 建立水果项目
    lb.insert(END,fruit)
lb.bind("<<ListboxSelect>>",itemSelected)  # 绑定
lb.pack(pady=5)

root.mainloop()

