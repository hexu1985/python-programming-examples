# ch18_14.py 
from tkinter import * 
from tkinter.ttk import * 
def treeview_sortColumn(col):
    global reverseFlag                         # 定义排序标识全局变量
    lst = [(tree.set(st,col),st)
            for st in tree.get_children("")]
    print(lst)                                 # 打印列表
    lst.sort(reverse=reverseFlag)              # 排序列表
    print(lst)                                 # 打印列表
    for index, item in enumerate(lst):         # 重新移动项目内容
            tree.move(item[1],"",index)
    reverseFlag = not reverseFlag              # 更改排序标识

root = Tk()
root.title("ch18_14")
reverseFlag = False       # False              # 排序标识注明是否反向排序

myStates = {"Illinois","California","Texas","Washington",
                "Jiangsu","Shandong","Guangdong","Fujian",
                "Mississippi","Kentucky","Florida","Indiana"}

tree = Treeview(root,columns=("states"),show="headings")
yscrollbar = Scrollbar(root)             # y轴scrollbar对象
yscrollbar.pack(side=RIGHT,fill=Y)       # y轴scrollbar包装显示
tree.pack()
yscrollbar.config(command=tree.yview)    # y轴scrollbar设置
tree.configure(yscrollcommand=yscrollbar.set)
# 建立栏标题
tree.heading("states",text="State")
# 建立内容
for state in myStates:
    tree.insert("",index=END,values=state) # tree.insert("",index=END,values=(state,))
# 单击标题栏将启动treevi_sortColumn
tree.heading("#1",text="State",
                command=lambda c="states": treeview_sortColumn(c))
# tree.heading("#1",text="State",command=lambda : treeview_sortColumn("states"))
root.mainloop()

