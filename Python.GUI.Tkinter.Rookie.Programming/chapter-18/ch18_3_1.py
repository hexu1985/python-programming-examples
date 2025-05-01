# ch18_3_1.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18_3_1")

tuple1 = ("芝加哥","800")              # 以元组方式设置栏内容     
list2 = ["洛杉矶","1000"]             # 以列表方式设置栏内容
list3 = ["南京","900"]                # 以列表方式设置栏内容
# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立栏标题
tree.heading("#0",text="State") # 图标栏
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立内容
tree.insert("",index=END,text="伊利诺",values=tuple1) # 也可以使用元组代替
tree.insert("",index=END,text="加州",values=list2)
tree.insert("",index=END,text="江苏",values=list2)
tree.pack()

root.mainloop()

