# ch16_1.py
from tkinter import * 
from tkinter import messagebox 

def hello(): 
    messagebox.showinfo("Hello","欢迎使用菜单") 

root = Tk() 
root.title("ch16_1") 
root.geometry("300x180") 

# 建立最上层菜单 
menubar = Menu(root) 
# menubar.add_command(label="Exit!",command=root.destroy) 
menubar.add_command(label="Hello!",command=hello) 
menubar.add_command(label="Exit!",command=root.destroy) 
root.config(menu=menubar)    # 显示菜单对象 

root.mainloop() 

