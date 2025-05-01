# ch11_8.py
from tkinter import * 
def buttonClicked1():                     # Button按钮事件处理程序1
    print("#1 Command event handler, I like tkinter...")
def buttonClicked2(event):                     # Button按钮事件处理程序2
    print("#2 Bind event handler, I like tkinter...")
def buttonClicked3(event):                     # Button按钮事件处理程序3
    print("#3 Bind event handler, I like tkinter...")
def buttonClicked4(event):                     # Button按钮事件处理程序4
    print("#4 Bind event handler, I like tkinter...")
root = Tk()
root.title("ch11_8")                  # 窗口标题    
root.geometry("300x180")              # 窗口宽300高180

btn = Button(root,text="tkinter",command=buttonClicked1)
btn.pack(anchor=W,padx=10,pady=10)
btn.bind("<Button-1>",buttonClicked2,add="+")
btn.bind("<Button-1>",buttonClicked3,add="+")
btn.bind("<Button-1>",buttonClicked4,add="+")

root.mainloop()
