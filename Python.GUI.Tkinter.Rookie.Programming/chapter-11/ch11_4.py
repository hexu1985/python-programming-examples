# ch11_4.py
from tkinter import *
from tkinter import messagebox

def leave(event):                     # <Esc>事件处理程序
    ret = messagebox.askyesno("ch11_4对话框...","是否离开？")
    if ret:
        root.destroy()
    else:
        return

root = Tk()
root.title("ch11_4")                  # 窗口标题    

root.bind("<Escape>",leave) #<Enter>    <Return> <Escape> <a>  <A>
lab = Label(root,text="测试Esc键",
            bg="yellow",fg="blue",
            height=4, width=15,
            font="Times 12 bold")

lab.pack(padx=30,pady=30) 
 
root.mainloop()
