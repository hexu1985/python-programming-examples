# ch9_8.py
from tkinter import *

def printInfo():       # 打印显示的值
    print(sp.get())

root = Tk()
root.title("ch9_8")

sp = Spinbox(
                root,
                # values=(10,38,170,101),   # 以元组形式存储数值
                values=[10,38,170,101],   # 以列表形式存储数值
                command=printInfo
            )
sp.pack(pady=10,padx=10)

root.mainloop()
