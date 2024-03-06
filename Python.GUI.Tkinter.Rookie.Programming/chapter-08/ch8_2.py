# ch8_1.py
from tkinter import *

root = Tk()
root.title("ch8_2")

# 用字典存储框架颜色与光标形状
fms = {
    "red":"cross",
    "green":"boat",
    "blue":"clock"
    }

for fmColor in fms.keys(): # 建立三个不同底色的框架与光标形状
    # Frame(root,bg=fm,height=50,width=250).pack()
    Frame(root,bg=fmColor,cursor=fms[fmColor],
        height=50,width=250).pack(side=LEFT) # 调用构造方法时省略父对象
        
root.mainloop()
