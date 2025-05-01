# ch13_10.py 
# from tkinter import * 
from tkinter.ttk import *
from tkinter import *     
# 注意这两句导入语句的顺序，颠倒之后会有差异
# tkinter.label和tkinter.ttk.label的参数有差异，bg和background会有不同
def comboSelection(event):    # 打印选择的结果
    labelVar.set(var.get())   # 同步标签内容

root = Tk()
root.title("ch13_10")                              # 窗口标题
root.geometry("300x120")

var = StringVar()
cb = Combobox(root,textvariable=var)              # 创建Combobox
cb["value"] = ("Python","Java","C#","C","C++")    # 设置选项内容
cb.current(0)
cb.bind("<<ComboboxSelected>>",comboSelection)    # 绑定
cb.pack(side=LEFT,padx=10,pady=10)

print("var: ",var.get())

labelVar = StringVar()
label = Label(root,bg="yellow",textvariable=labelVar)
labelVar.set(var.get())
label.pack(side=LEFT)

root.mainloop()

