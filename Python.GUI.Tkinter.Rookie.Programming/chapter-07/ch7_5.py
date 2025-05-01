# ch7_5.py
from tkinter import *
def printSelection():
    label.config(text="You have chosen "+var.get()+".gif.")

root = Tk()
root.title("ch7_5")

img_chuckle = PhotoImage(file="chuckle.gif")
img_shock = PhotoImage(file="shock.gif")
img_snap = PhotoImage(file="snap.gif")

var = StringVar()         # 选项按钮绑定的变量
var.set(" ")             # 默认全不选
# var.set("")             # 默认全选
label = Label(root,text="This is a defult option, please choose...",bg="lightyellow",width=35)
label.pack()

rb_chuckle = Radiobutton(root,image=img_chuckle,
                    variable=var,value="chuckle",
                    command=printSelection)
rb_chuckle.pack()

rb_shock = Radiobutton(root,image=img_shock,
                    variable=var,value="shock",
                    command=printSelection)
rb_shock.pack()

rb_snap = Radiobutton(root,image=img_snap,
                    variable=var,value="snap",
                    command=printSelection)
rb_snap.pack()

root.mainloop()

