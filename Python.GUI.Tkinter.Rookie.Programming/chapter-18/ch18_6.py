# ch18_6.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18_6")

stateCity = {"伊利诺":"芝加哥","加州":"洛杉矶",
            "德州":"休斯敦","华盛顿州":"西雅图",
            "江苏":"南京","山东":"青岛",
            "广东":"广州","福建":"厦门"}
# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立栏标题
tree.heading("#0",text="State") # 图标栏
tree.heading("cities",text="City")
# 格式化栏位
tree.column("cities",anchor=CENTER)
# 建立内容,行号从1算起偶数行是用浅蓝色底
tree.tag_configure("evenColor",background="lightblue") # 设置标签
rowCount = 1
for state in stateCity.keys():
    if (rowCount % 2 == 1):
        tree.insert("",index=END,text=state,values=stateCity[state])
    else:
        tree.insert("",index=END,text=state,values=stateCity[state],
                    tags=("evenColor"))   # 建立浅蓝色底
    rowCount += 1                         # 行号数加1
tree.pack()

root.mainloop()

