# ch14_1.py
from tkinter import *

pw = PanedWindow(orient=VERTICAL)           # 创建PanedWindow对象
pw.pack(fill=BOTH,expand=True)

top = Label(pw,text="Top Pane")             # 创建标签Top Pane
pw.add(top)                                 # top标签插入PanedWindow

bottom = Label(pw,text="Bottom Pane")       # 创建标签Bottom Pane
pw.add(bottom)                              # bottom标签插入PanedWindow

pw.mainloop()

