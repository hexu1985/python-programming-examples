# ch12_8.py 
from tkinter import * 
fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_8")                             # 窗口标题    
root.geometry("300x210")                         # 窗口宽300高210

lb = Listbox(root)              
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=10)
lb.selection_set(0) # 默认选择第0个项目

root.mainloop()

