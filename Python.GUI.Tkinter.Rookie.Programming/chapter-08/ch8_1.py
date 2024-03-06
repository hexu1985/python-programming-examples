# ch8_1.py
from tkinter import *

root = Tk()
root.title("ch8_1")

for fm in ["red","green","blue"]: # 建立三个不同底色的框架
    Frame(root,bg=fm,height=50,width=250).pack()

root.mainloop()
