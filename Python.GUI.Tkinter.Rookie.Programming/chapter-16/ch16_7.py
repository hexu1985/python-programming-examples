# ch16_7.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File-林祖泉","新建文档-林祖泉")
def controlN(event):
    messagebox.showinfo("New File","新建文档-CONTROL+N")

root = Tk()
root.title("ch16_7")
root.geometry("300x180")

menubar = Menu(root)      # 建立最上层菜单
# 建立菜单类别对象,并将此菜单类别命名为File
filemenu = Menu(menubar)
menubar.add_cascade(label="File 文件-林祖泉",menu=filemenu,underline=0)
# 在File菜单内建立菜单列表
filemenu.add_command(label="New File 新建文件-林祖泉",
                    command=newFile,accelerator="Ctrl+N")
# 经过试验发现 #,accelerator="Ctrl+N") 上一行代码的这部分可以直接删去，而不造成可见的影响
filemenu.add_separator()
filemenu.add_command(label="Exit 退出-林祖泉!",command=root.destroy,underline=0)

root.config(menu=menubar)    # 显示菜单对象
root.bind("<Control-N>",lambda event:messagebox.showinfo("New File","新建文档-lambda函数实现"))
# root.bind("<Control-N>",controlN)


# 注意: <Control-N>对快捷键的大小写敏感 按键的时候要使用大写的N
root.mainloop()

