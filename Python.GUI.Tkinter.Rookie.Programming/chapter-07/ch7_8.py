# ch7_8.py
from tkinter import *

def printInfo():
    selection = ""
    # print("before iteration:")
    # print(selection)
    for i in checkboxes.keys():           # 检查此字典的关键字,同: for i in checkboxes:
        if checkboxes[i].get() == True:   # 若被选中则执行
            selection = selection + sports[i] + "\t"
            # print(selection)
    # print("after iteration:")
    print(selection)

root = Tk()
root.title("ch7_8")  # 窗口标题

label = Label(root,text="请选择喜欢的运动",fg="blue",bg="lightyellow",width=30)
label.grid(row=0)

sports = {0:"美式足球",1:"棒球",2:"篮球",3:"网球",4:"足球",5:"游泳"}  # 运动项目构成的字典
checkboxes = {}   # 字典,存放被选取项目的BooleanVar变量
for i in range(len(sports)):       # 根据运动字典建立复选框
    checkboxes[i] = BooleanVar()   # 建立布尔变量对象
    Checkbutton(root,text=sports[i],
                variable=checkboxes[i]).grid(row=i+1,sticky=W)

btn = Button(root,text="确定",width=10,command=printInfo)
btn.grid(row=i+2)
# btn.grid()

root.mainloop()

