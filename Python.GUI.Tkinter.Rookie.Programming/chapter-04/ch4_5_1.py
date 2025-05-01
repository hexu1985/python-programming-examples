
from tkinter import *

def bColor(bgColor):
    root.config(bg=bgColor)

root = Tk()
root.title("ch4_5_1")
root.geometry("300x200")
# 以此新建三个按钮
exitbtn = Button(root,text="Exit",command=root.destroy)
bluebtn = Button(root,text="Blue",command=lambda : bColor("blue"))
yellowbtn = Button(root,text="Yellow",command=lambda : bColor("yellow"))
# 将三个按钮包装定位在右下方
exitbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
bluebtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)
yellowbtn.pack(anchor=S,side=RIGHT,padx=5,pady=5)

root.mainloop()

