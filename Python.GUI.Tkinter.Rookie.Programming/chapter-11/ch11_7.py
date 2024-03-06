# ch11_7.py
from tkinter import * 
def buttonClicked(event):                     # Button按钮事件处理程序
    print("I like tkinter...")

# 所传递的对象onoff是btn对象
def toggle(onoff):         # 切换绑定
    if var.get():          # 如果True绑定
        onoff.bind("<Button-1>",buttonClicked)
        cbtn.config(text="已绑定")
    else:                  # 如果False不绑定
        onoff.unbind("<Button-1>")
        cbtn.config(text="已解绑")

root = Tk()
root.title("ch11_7")                  # 窗口标题    
root.geometry("300x180")              # 窗口宽300高180

btn = Button(root,text="tkinter")
btn.pack(anchor=W,padx=10,pady=10)

var = BooleanVar()
# var.set(True)
cbtn = Checkbutton(root,text="bind/unbind",variable=var,
                    command=lambda:toggle(btn))
cbtn.pack(anchor=W,padx=10)
# var.set(True)
root.mainloop()
