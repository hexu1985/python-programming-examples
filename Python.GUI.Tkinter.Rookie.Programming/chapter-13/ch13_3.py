# ch13_3.py
from tkinter import *

root = Tk()
root.title("ch13_3")
root.geometry("300x180")

omTuple = ("Python","Java","C")       # 使用元组
# omTuple = ["Python","Java","C"]     # 使用列表
var = StringVar(root)
var.set("Python")
optionmenu = OptionMenu(root,var,*omTuple)
optionmenu.pack()

root.mainloop()

