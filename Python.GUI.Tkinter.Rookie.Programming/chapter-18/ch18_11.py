# ch18_11.py 
from tkinter import * 
from tkinter.ttk import * 
def removeItem():            # 删除所选项目
    ids = tree.selection()   # 取得所选项目
    for id in ids:           # 所选项目可能很多所以用循环
        tree.delete(id)      # 删除所选项目
def insertItem(): 
    state = stateEntry.get() # 获得stateEntry的输入
    city = cityEntry.get()   # 获得cityEntry的输入
# 如果输入数据不完全不往下执行
    if (len(state.strip())==0 or len(city.strip())==0):
        return
    tree.insert("",END,text=state,values=(city))   # 插入 # tree.insert("",END,text=state,values=city)
    stateEntry.delete(0,END)                       # 删除stateEntry
    cityEntry.delete(0,END)                        # 删除cityEntry

root = Tk()
root.title("ch18_11")

stateCity = {"伊利诺":"芝加哥","加州":"洛杉矶",
                "德州":"休斯敦","华盛顿州":"西雅图",
                "江苏":"南京","山东":"青岛",
                "广东":"广州","福建":"厦门"}
# 以下三行主要是应用在缩放窗口
root.rowconfigure(1,weight=1)       # row1会随窗口缩放1:1变化
root.columnconfigure(1,weight=1)    # column1会随窗口缩放1:1变化
root.columnconfigure(3,weight=1)    # column3会随着窗口缩放1:1变化

stateLab = Label(root,text="State :")   # 建立State:标签
stateLab.grid(row=0,column=0,padx=5,pady=3,sticky=W)
stateEntry = Entry()                    # 建立State:文本框
stateEntry.grid(row=0,column=1,sticky=W+E,padx=5,pady=3)
cityLab = Label(root,text="City : ")
cityLab.grid(row=0,column=2,sticky=E)
cityEntry = Entry()
cityEntry.grid(row=0,column=3,sticky=W+E,padx=5,pady=3)
# 建立Insert按钮
inBtn = Button(root,text="插入",command=insertItem)
inBtn.grid(row=0,column=4,padx=5,pady=3)
# 建立Treeview,可以有多项选择selectmode=EXTENDED
tree = Treeview(root,columns=("cities"),selectmode=EXTENDED)
# 建立栏标题
tree.heading("#0",text="State")      # 图标栏
tree.heading("cities",text="City")
# 格式栏位
tree.column("cities",anchor=CENTER)
# 建立内容
for state in stateCity.keys():
    tree.insert("",index=END,text=state,values=stateCity[state])
tree.grid(row=1,column=0,columnspan=5,padx=5,sticky=W+E+N+S)

rmBtn = Button(root,text="删除",command=removeItem) # “删除”按钮
rmBtn.grid(row=2,column=2,padx=5,pady=3,sticky=W)

root.mainloop()

