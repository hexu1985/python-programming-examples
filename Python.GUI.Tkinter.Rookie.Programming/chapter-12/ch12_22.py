# ch12_22.py
from tkinter import *


root = Tk()
root.title("ch12_22")        # 窗口标题  

scrollbar = Scrollbar(root)  # 创建滚动条
scrollbar.pack(side=RIGHT,fill=Y)

# 创建Listbox,yscrollcommand指向scrollbar.set方法
lb = Listbox(root,yscrollcommand=scrollbar.set)            # 建立Listbox
for i in range(50):
    lb.insert(END,"Line " + str(i))
lb.pack(side=LEFT,fill=BOTH,expand=True)

scrollbar.config(command=lb.yview)

root.mainloop()

