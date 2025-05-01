# ch11_9.py
from tkinter import * 
from tkinter import messagebox

def callback():
    print("窗口右上角的叉号被点击...")
    result = messagebox.askokcancel("OK/CANCEL?","结束或则取消？")
    if result:
        root.destroy()
    else:
        # pass
        return

root = Tk()
root.title("ch11_9")                  # 窗口标题    
root.geometry("300x180")              # 窗口宽300高180
root.protocol("WM_DELETE_WINDOW",callback) # 更改协议绑定
root.mainloop()
