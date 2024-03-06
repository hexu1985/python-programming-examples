# ch18_12.py 
from tkinter import * 
from tkinter import messagebox 
from tkinter.ttk import * 
def doubleClick(event):                             
    e = event.widget                                  # 取得事件控件
    iid = e.identify("item",event.x,event.y)          # 取得双击项目id
    state = e.item(iid,"text")                        # 取得state
    city = e.item(iid,"values")[0]                    # 取得city
    outputStr = "{0} : {1}".format(state,city)        # 格式化
    messagebox.showinfo("Double Clicked",outputStr)   # 输出

root = Tk()
root.title("ch18_12")

stateCity = {"伊利诺":"芝加哥","加州":"洛杉矶",
                "德州":"休斯敦","华盛顿州":"西雅图",
                "江苏":"南京","山东":"青岛",
                "广东":"广州","福建":"厦门"}

# 建立Treeview
tree = Treeview(root,columns=("cities"))
# 建立栏标题
tree.heading("#0",text="State")   # 图标栏
tree.heading("cities",text="City")
# 格式栏位
tree.column("cities",anchor=CENTER)
# 建立内容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.bind("<Double-1>",doubleClick)  # 双击绑定doubleClick方法
tree.pack()

root.mainloop()

