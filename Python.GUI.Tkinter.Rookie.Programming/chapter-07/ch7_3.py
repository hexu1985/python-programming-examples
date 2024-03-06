# ch7_2.py
from tkinter import *
def printSelection():
    print(cities[var.get()],"被选中！！！")

root = Tk()
root.title("ch7_3")    # 设置窗口标题
cities = {  0:"北京" ,1:"上海",
            2:"广州",3:"深圳",
            4:"杭州",5:"苏州",
         }



var = IntVar()         # 选项按钮绑定的变量
var.set(-1)             # 默认选项
# var.set(0)           # 默认选项 
label = Label(root,text="选择最喜欢的城市",
                fg="blue",bg="lightyellow",width=30)
label.pack()

for val,city in cities.items():
    Radiobutton(
        root,
        text=city,
        variable=var,value=val,
        command=printSelection
    ).pack()

root.mainloop()

