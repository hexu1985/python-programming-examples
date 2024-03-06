# ch9_9.py
from tkinter import *

def printInfo():       # 打印显示的值
    print(sp.get())

root = Tk()
root.title("ch9_9")
# cities = ("北京","上海","广州","深圳")       # 以元组形式存储数值
cities = ["北京","上海","广州","深圳"]       # 以列表形式存储数值

sp = Spinbox(
                root,
                values=cities,   # 以元组形式存储数值
                command=printInfo
            )
sp.pack(pady=10,padx=10)

root.mainloop()
