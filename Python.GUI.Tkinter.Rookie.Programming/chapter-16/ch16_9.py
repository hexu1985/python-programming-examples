# ch16_9.py 
from tkinter import *
from tkinter import messagebox
def minimizeIcon():                            # 缩小窗口为图标
    print("窗口最小化...")
    root.iconify()   # 最小化窗口
def showPopupMenu(event):                      # 显示弹出窗口
    print("窗口弹出...")
    popupmenu.post(event.x_root,event.y_root)  # 在鼠标光标位置处弹出此菜单
    # print(event.x_root," *** ",event.y_root)
    # print(type(event.x_root)," *** ",type(event.y_root))  # int类型
    # popupmenu.post(100,100)  ############ # 窗口固定显示

root = Tk()
root.title("ch16_9")
root.geometry("300x180")

popupmenu = Menu(root,tearoff=False)           # 建立弹出窗口对象
# 在弹出菜单内建立两个指令列表
popupmenu.add_command(label="Minimize",command=minimizeIcon)
popupmenu.add_command(label="Exit",command=root.destroy)
# 单击鼠标右键绑定显示弹出菜单
root.bind("<Button-3>",showPopupMenu)

# root.config(menu=popupmenu) # 这段代码将popupmenu对象固定在窗口菜单栏
root.mainloop()

