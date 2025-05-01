# ch12_20.py
from tkinter import *
def itemsSorted():
    if (var.get() == True):
        revBool = True
    else:
        revBool = False
    listTmp = list(lb.get(0,END))
    sortedList = sorted(listTmp,reverse=revBool)
    lb.delete(0,END)
    for item in sortedList:
        lb.insert(END,item)

fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_20")        # 窗口标题  
# root.geometry("300x250")     # 窗口宽300高210  

lb = Listbox(root)            # 建立Listbox
for fruit in fruits:          # 建立水果项目
    lb.insert(END,fruit)
lb.pack(padx=10,pady=5)

# 建立“排序”按钮
btn = Button(root,text="排序",command=itemsSorted)
btn.pack(side=LEFT,padx=10,pady=5)

# 建立排序设置复选框
var = BooleanVar()
cb = Checkbutton(root,text="从大到小排序",variable=var)
cb.pack(side=LEFT)

root.mainloop()

