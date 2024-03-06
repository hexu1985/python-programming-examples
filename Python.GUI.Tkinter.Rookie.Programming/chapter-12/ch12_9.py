# ch12_9.py 
from tkinter import * 
fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_9")                             # 窗口标题    
root.geometry("300x210")                         # 窗口宽300高210

lb = Listbox(root,selectmode=EXTENDED)           # 拖拽可以多选         
for fruit in fruits:                             # 建立水果项目
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.selection_set(0,3)                            # 默认选择第0-3个项目

root.mainloop()

