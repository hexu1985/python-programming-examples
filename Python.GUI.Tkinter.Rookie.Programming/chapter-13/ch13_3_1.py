# ch13_3_1.py
from tkinter import *

root = Tk()
root.title("ch13_3_1")
root.geometry("300x180")

omTuple = ("Python","Java","C")       # 使用元组
# omTuple = ["Python","Java","C"]     # 使用列表
var = StringVar(root)
var.set(omTuple[0])
optionmenu = OptionMenu(root,var,*omTuple)
optionmenu.pack()

root.mainloop()

