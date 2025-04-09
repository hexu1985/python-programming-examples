from tkinter       import *
from GUICommon_7_2 import *

import string

class TestColors(Frame, GUICommon):
    def __init__(self, parent=None):

        Frame.__init__(self)
        self.base = "#848484"
        self.pack()
        self.set_colors()
        self.make_widgets()

    def set_colors(self):
        # 确保设置有效的十六进制颜色值
        self.vdbase = "#5a5a5a"  # 非常暗的灰色
        self.dbase = "#6a6a6a"   # 暗灰色
        self.base = "#848484"     # 基础灰色
        self.lbase = "#9e9e9e"   # 亮灰色
        self.vlbase = "#b8b8b8"  # 非常亮的灰色

    def make_widgets(self):
        for tag in ['VDBase', 'DBase', 'Base', 'LBase', 'VLBase']:
            Button(self, text=tag, bg=eval('self.%s' % tag.lower()), 
                     fg='white', command=self.quit).pack(side=LEFT)

if __name__ == '__main__':
    TestColors().mainloop()
