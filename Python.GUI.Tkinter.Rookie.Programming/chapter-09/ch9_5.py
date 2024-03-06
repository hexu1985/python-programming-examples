# ch9_4.py 
from tkinter import * 

def bgUpdade(source): # 注意:这里的参数source是必须的
    ''' 更改窗口背景颜色 '''
    red = rSlider.get()                              # 读取red值
    green = gSlider.get()                            # 读取green值
    blue = bSlider.get()                             # 读取blue值
    print("R=%d, G=%d, B=%d" % (red, green, blue))   # 打印色彩数值
    myColor = "#%02x%02x%02x" % (red,green,blue)     # 将颜色转成十六进制字符串
    print(myColor)                                   # 打印这个代表颜色的字符串
    root.config(bg=myColor)                          # 设置窗口背景颜色

root = Tk()
root.title("ch9_4")
root.geometry("360x240")

rSlider = Scale(root,from_=0,to=255,label="红色分量",command=bgUpdade)
gSlider = Scale(root,from_=0,to=255,label="绿色分量",command=bgUpdade)
bSlider = Scale(root,from_=0,to=255,label="蓝色分量",command=bgUpdade)
gSlider.set(125)                       # 设置green分量的初始值是125
rSlider.grid(row=0, column=0)          # row=0,col=0
gSlider.grid(row=0, column=1)          # row=0,col=1
bSlider.grid(row=0, column=2)          # row=0,col=2

root.mainloop()
