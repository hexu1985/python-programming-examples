# ch11_1_1.py
from tkinter import *
def pythonClicked():          # Python复选框事件处理程序
    if varPython.get():
        lab.config(text="Select Python")
    else:
        lab.config(text="Unselect Python")
def javaClicked():          # Java复选框事件处理程序
    if varJava.get():
        lab.config(text="Select Java")
    else:
        lab.config(text="Unselect Java")
def buttonClicked(event):
    lab.config(text="Button clicked")

root = Tk()
root.title("ch11_1_1")                 # 窗口标题    
root.geometry("300x180")             # 窗口宽300高180
 
btn = Button(root,text="Click Me")
btn.pack(anchor=W)
btn.bind("<Button-1>",buttonClicked) # 单击Click Me绑定buttonClicked方法

varPython = BooleanVar()
cbnPython = Checkbutton(root,text="Python",variable=varPython,
                        command=pythonClicked)
cbnPython.pack(anchor=W)
varJava = BooleanVar()
cbnJava = Checkbutton(root,text="Java",variable=varJava,
                        command=javaClicked)
cbnJava.pack(anchor=W)
lab = Label(root,bg="yellow",fg="blue",
            height=2,width=12,
            font="Times 16 bold")
lab.pack()

root.mainloop()
