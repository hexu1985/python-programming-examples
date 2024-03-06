# ch18_8.py
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

root = Tk()
root.title("ch18_8")

Style().configure("Treeview",rowheight=35)  # 格式化扩充row高度

info = ["凤凰新闻App可以获得中国各地最新消息",
        "瑞士国家铁路App提供全瑞士火车时刻表",
        "可口可乐App是一个娱乐的软件"]

tree = Treeview(root,columns=("说明"))
tree.heading("#0",text="App")              # 图标栏
tree.heading("#1",text="功能说明")
tree.column("#1",width=300)                # 格式化栏标题

img1 = Image.open("凤凰新闻.jpg")           # 插入凤凰新闻App图示
imgObj1 = ImageTk.PhotoImage(img1)
tree.insert("",index=END,text="凤凰新闻",image=imgObj1,values=info[0])

img2 = Image.open("瑞士铁路.jpg")           # 插入瑞士国家铁路App图示
imgObj2 = ImageTk.PhotoImage(img2)
tree.insert("",index=END,text="瑞士铁路",image=imgObj2,values=info[1])

img3 = Image.open("可口可乐.jpg")           # 插入可口可乐App图示
imgObj3 = ImageTk.PhotoImage(img3)         
tree.insert("",index=END,text="可口可乐",image=imgObj3,values=info[2])
tree.pack()

root.mainloop()

