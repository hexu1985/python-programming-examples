# ch12_21.py
from tkinter import *
def getIndex(event):                 # 处理单击选项
    lb.index = lb.nearest(event.y)   # 目前选项的索引
cnt = 0
def dragJob(event):
    newIndex = lb.nearest(event.y)

    global cnt
    cnt += 1
    print("**********************",cnt)
    if newIndex < lb.index:
        x = lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex+1,x)
        lb.index = newIndex
        print("上调成功...")
    elif newIndex > lb.index:
        x = lb.get(newIndex)
        lb.delete(newIndex)
        lb.insert(newIndex-1,x)
        lb.index = newIndex
        print("下调成功...")


fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_21")        # 窗口标题  
# root.geometry("300x250")     # 窗口宽300高210  

lb = Listbox(root)            # 建立Listbox
for fruit in fruits:          # 建立水果项目
    lb.insert(END,fruit)
    lb.bind("<Button-1>",getIndex)
    lb.bind("<B1-Motion>",dragJob)
lb.pack(padx=10,pady=10)

root.mainloop()

