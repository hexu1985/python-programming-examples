# ch16_10.py 
from tkinter import *

def status():
    if demoStatus.get():
        statusLabel.pack(side=BOTTOM,fill=X)
    else:
        statusLabel.pack_forget() # 隐藏标签状态栏

root = Tk()
root.title("ch16_10")
root.geometry("300x180")

menubar = Menu(root)           # 建立最上层菜单
# 建立菜单类别对象，并将此菜单类别命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)
# 在File菜单内建立菜单列表Exit
filemenu.add_command(label="Exit",command=root.destroy)
# 建立菜单类别对象，并将此菜单类别命名为View
viewmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="View",menu=viewmenu)
# 在View菜单内创建Check menu button
demoStatus = BooleanVar()
demoStatus.set(True)
viewmenu.add_checkbutton(label="Status",command=status,
                            variable=demoStatus) # demoStatus状态改变时会调用status函数
root.config(menu=menubar)

statusVar = StringVar()
statusVar.set("显示")
statusLabel = Label(root,textvariable=statusVar,relief="raised")
statusLabel.pack(side=BOTTOM,fill=X)

root.mainloop()

