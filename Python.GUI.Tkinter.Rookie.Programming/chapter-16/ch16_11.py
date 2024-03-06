# ch16_11.py 
from tkinter import *

root = Tk()
root.title("ch16_11")
root.geometry("300x180")

menubar = Menu(root)           # 建立最上层菜单
# 建立菜单类别对象，并将此菜单类别命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)
# 在File菜单内建立菜单列表Exit
filemenu.add_command(label="Exit",command=root.destroy)

# 建立工具栏
toolbar = Frame(root,relief=RAISED,borderwidth=3)
# 在工具栏内创建按钮
myGif = PhotoImage(file="chuckle.gif")
exitBtn = Button(toolbar,image=myGif,command=root.destroy)
exitBtn.pack(side=LEFT,padx=3,pady=3)                          # 包装按钮
toolbar.pack(side=TOP,fill=X)                                  # 包装工具栏
root.config(menu=menubar)                                      # 显示菜单对象

root.mainloop()

