# ch16_5.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File-林祖泉","新建文档-林祖泉")
def openFile():
    messagebox.showinfo("New File-林祖泉","打开文档-林祖泉")
def saveFile():
    messagebox.showinfo("New File-林祖泉","保存文档-林祖泉")
def saveAsFile():
    messagebox.showinfo("New File-林祖泉","另存为文档-林祖泉")
def aboutMe():
    messagebox.showinfo("New File-林祖泉","代码由cxq重现...")


root = Tk()
root.title("ch16_5")
root.geometry("300x180")

menubar = Menu(root)      # 建立最上层菜单
# 建立菜单类别对象,并将此菜单类别命名为File
filemenu = Menu(menubar)
menubar.add_cascade(label="File 文件-林祖泉",menu=filemenu)
# 在File菜单内建立菜单列表
filemenu.add_command(label="New File 新建文件-林祖泉",command=newFile)
filemenu.add_command(label="Open File 新建文件-林祖泉",command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Save File 新建文件-林祖泉############",command=saveFile)
# filemenu.add_separator()########################
filemenu.add_command(label="Save As File 新建文件-林祖泉",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit 退出-林祖泉!",command=root.destroy)
# 建立菜单类别对象,并将此菜单类别命名为Help
helpmenu = Menu(menubar)
menubar.add_cascade(label="Help-帮助-林祖泉",menu=helpmenu)
# 在Help菜单内建立菜单列表
helpmenu.add_command(label="About Me-关于我",command=aboutMe)

root.config(menu=menubar)    # 显示菜单对象

root.mainloop()

