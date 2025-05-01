# ch18_7.py
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("ch18_7")

asia = {"中国":"北京","日本":"东京","泰国":"曼谷","韩国":"首尔"}
euro = {"英国":"伦敦","法国":"巴黎","德国":"柏林","挪威":"奥斯陆"}

# 建立Treeview
tree = Treeview(root,columns=("capital"))
# 建立栏标题
tree.heading("#0",text="国家") # 图标栏
tree.heading("capital",text="首都")
# 建立id
idAsia = tree.insert("",index=END,text="Asia")
idEuro = tree.insert("",index=END,text="Europe")
# 建立idAsia底下内容
for country in asia.keys():
    tree.insert(idAsia,index=END,text=country,values=asia[country])
# 建立idEuro底下内容
for country in euro.keys():
    tree.insert(idEuro,index=END,text=country,values=euro[country])
tree.pack()

root.mainloop()

