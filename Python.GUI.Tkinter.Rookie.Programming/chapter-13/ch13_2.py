# ch13_2.py
from tkinter import *

root = Tk()
root.title("ch13_2")
root.geometry("300x180")

omTuple = ("Python","Java","C")       # 使用元组
# omTuple = ["Python","Java","C"]     # 使用列表
var = StringVar(root)
optionmenu = OptionMenu(root,var,*omTuple)
optionmenu.pack()

root.mainloop()

