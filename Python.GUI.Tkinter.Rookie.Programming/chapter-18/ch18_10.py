# ch18_10.py
from tkinter import *
from tkinter.ttk import *
def removeItem():
    iids = tree.selection()
    for iid in iids:
        tree.delete(iid)

root = Tk()
root.title("ch18_10")

stateCity = {"伊利诺":"芝加哥","加州":"洛杉矶",
                "德克萨斯州":"休斯敦","华盛顿州":"西雅图",
                "江苏":"南京","山东":"青岛",
                "广东":"广州","福建":"厦门"}
# 建立Treeview,可以有多项选择selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立栏标题
tree.heading("#0",text="State")
tree.heading("cities",text="City")
# 格式栏位
tree.column("cities",anchor=CENTER)
# 建立内容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.pack()

rmBtn = Button(root,text="Remove",command=removeItem)
rmBtn.pack(pady=5)

root.mainloop()

