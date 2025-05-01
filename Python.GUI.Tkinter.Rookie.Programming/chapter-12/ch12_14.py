# ch12_14.py
from tkinter import *
def callback():                  # 打印所选的项目
    indexs = lb.curselection()
    for index in indexs:         # 取得索引值
        print(lb.get(index))     # 打印所选的项目
    print(indexs)

fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_14")        # 窗口标题  
root.geometry("300x250")     # 窗口宽300高210  

lb = Listbox(root,selectmode=MULTIPLE)                 
for fruit in fruits:         # 建立水果项目
    lb.insert(END,fruit)
lb.pack(pady=5)
btn = Button(root,text="Print",command=callback)
btn.pack(pady=5)

root.mainloop()

