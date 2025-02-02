# ch14_2.py
from tkinter import *

root = Tk()
root.title("ch14_2")
# pw = PanedWindow(root,orient=HORIZONTAL)         # 创建PanedWindow对象
pw = PanedWindow(orient=HORIZONTAL)         # 创建PanedWindow对象

leftframe = LabelFrame(pw,text="Left Pane",width=120,height=150)
pw.add(leftframe)                           # 插入左边LabelFrame
middleframe = LabelFrame(pw,text="Middle Pane",width=120)
pw.add(middleframe)                         # 插入中间LabelFrame
rightframe = LabelFrame(pw,text="Right Pane",width=120)
pw.add(rightframe)                          # 插入右边LabelFrame

pw.pack(fill=BOTH,expand=True,padx=10,pady=10)

root.mainloop()

