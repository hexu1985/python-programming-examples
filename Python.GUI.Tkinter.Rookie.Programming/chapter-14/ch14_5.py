# ch14_5.py
from tkinter import *

pw = PanedWindow(orient=HORIZONTAL)  # 建立外层PanedWindow
pw.pack(fill=BOTH,expand=True)

entry = Entry(pw,bd=3)
pw.add(entry)

# 创建PanedWindow对象pwin,这是外层PanedWindow的子对象
pwin = PanedWindow(pw,orient=VERTICAL)
pw.add(pwin)
# 创建Scale,这是pwin对象的子对象
scale = Scale(pwin,orient=HORIZONTAL)
pwin.add(scale)

pw.mainloop()

