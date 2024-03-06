# ch12_7.py 
from tkinter import * 
fruits = [
    "Banana","Watermelon","Pineapple",
    "Orange","Grapes","Mango"
]

root = Tk()
root.title("ch12_7")                             # 窗口标题    
root.geometry("300x210")                         # 窗口宽300高210

lb = Listbox(root,selectmode=EXTENDED)              
for fruit in fruits:
    lb.insert(END,fruit)
lb.pack(pady=10)
print("items数字:",lb.size())  # 列出选项数量

root.mainloop()

