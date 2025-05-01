# ch5_9.py
from tkinter import *
def cal():
    out.configure(text = "结果:" + str(eval(equ.get())))
    # equ.delete(0,END) # 计算完成后清除输入框

root = Tk()
root.title("ch5_9")
label = Label(root,text="请输入数学表达式:")
label.pack()
equ = Entry(root)
equ.pack(pady=5)
out = Label(root)
out.pack()
btn = Button(root,text="计算",command=cal)
btn.pack(pady=5)

root.mainloop()

