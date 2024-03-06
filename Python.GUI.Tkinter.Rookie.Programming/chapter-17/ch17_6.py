# ch17_6.py 
from tkinter import * 

root = Tk()
root.title("ch17_6")

xscrollbar = Scrollbar(root,orient=HORIZONTAL)
yscrollbar = Scrollbar(root)
text = Text(root,height=5,width=30,wrap="none",bg="lightyellow")
xscrollbar.pack(side=BOTTOM,fill=X)
yscrollbar.pack(side=RIGHT,fill=Y)
text.pack(fill=BOTH,expand=True) # text.pack(fill=X,expand=True) 
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
text.config(xscrollcommand=xscrollbar.set)
text.config(yscrollcommand=yscrollbar.set)

myString = \
"""Python是一种跨平台的计算机程序设计语言。
是一个高层次的结合了解释性、编译性、互动性
和面向对象的脚本语言。
最初被设计用于编写自动化脚本(shell)，
随着版本的不断更新和语言新功能的添加，
越多被用于独立的、大型项目的开发。"""
text.insert(END,myString)
# text.insert(INSERT,myString)
root.mainloop()

