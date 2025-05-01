# ch18_2.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18_2")

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立栏标题
tree.heading("#0",text="State") # 图标栏
tree.heading("cities",text="City林祖泉") # tree.heading("#1",text="City下施")
# 建立内容
tree.insert("",index=END,text="伊利诺",values="芝加哥")
tree.insert("",index=END,text="加州",values="洛杉矶")
tree.insert("",index=END,text="江苏",values="南京")
tree.pack()

root.mainloop()

