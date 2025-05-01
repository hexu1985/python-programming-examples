# ch9_4_1.py 
from tkinter import * 
from tkinter.colorchooser import * 

def bgUpdade():
    ''' 更改窗口背景颜色 '''
    myColor = askcolor()              # 列出色彩对话框
    print(type(myColor),myColor)      # 打印传递回来的值
    root.config(bg=myColor[1])        # 设置窗口背景颜色

root = Tk()
root.title("ch9_4_1")
root.geometry("360x240")

btn = Button(root,text="Select Color",command=bgUpdade)
btn.pack(pady=5)

root.mainloop()
