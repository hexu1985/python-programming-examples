# ch16_8.py 
from tkinter import *
from tkinter import messagebox
def findNext():
    messagebox.showinfo("Find Next","查找下一个")
def findPrevious():
    messagebox.showinfo("Find Previous","查找前一个")

root = Tk()
root.title("ch16_8")
root.geometry("300x180")

menubar = Menu(root)      # 建立最上层菜单
# 建立菜单类别对象,并将此菜单类别命名为File
filemenu = Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File菜单内建立菜单列表
# 首先在File菜单内建立find子菜单对象
findmenu = Menu(filemenu,tearoff=False)  # 取消分隔线 False
# filemenu.add_cascade(label="Find",menu=findmenu) ############## 可以提前到这 
findmenu.add_command(label="Find Next",command=findNext)
findmenu.add_separator() ########################################
findmenu.add_command(label="Find Previous",command=findPrevious)
filemenu.add_cascade(label="Find",menu=findmenu) ############## 提前 

# 下面是增加分隔线和建立Exit!子菜单
filemenu.add_separator()
filemenu.add_separator()############################################
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)

root.mainloop()

