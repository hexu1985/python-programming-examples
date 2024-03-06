# ch18_3.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18_3")

# 建立Treeview
tree = Treeview(root,columns=("cities","populations"))
# 建立栏标题
tree.heading("#0",text="State") # 图标栏
tree.heading("#1",text="City")
tree.heading("#2",text="Populations")
# 建立内容
tree.insert("",index=END,text="伊利诺",values=("芝加哥","800")) 
# tree.insert("",index=END,text="伊利诺",values=("芝加哥","800","9999"))# 多余信息
tree.insert("",index=END,text="加州",values=("洛杉矶","1000"))# 
# tree.insert("",index=END,text="加州",values=("洛杉矶"))# 缺少信息
tree.insert("",index=END,text="江苏",values=("南京","900"))# 信息正常
tree.pack()

root.mainloop()



