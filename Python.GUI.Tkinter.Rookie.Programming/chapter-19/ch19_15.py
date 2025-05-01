# ch19_15.py
from tkinter import * 
def paint(event):              # 拖曳可以绘图
    x1,y1 = (event.x,event.y)  # 设置左上角坐标
    x2,y2 = (event.x,event.y)  # 设置右下角坐标

    x1,y1 = (event.x-1,event.y-1)  # 设置左上角坐标
    x2,y2 = (event.x+1,event.y+1)  # 设置右下角坐标

    canvas.create_oval(x1,y1,x2,y2,fill="blue")
def cls():                     # 清除画面
    canvas.delete("all")

tk = Tk()
lab = Label(tk,text='拖曳鼠标可以绘图')      # 建立标题
lab.pack()
canvas = Canvas(tk,width=640, height=300)  # 建立画布
canvas.pack()

btn = Button(tk,text="清除",command=cls)    # 建立“清除”按钮
btn.pack(pady=5)

canvas.bind("<B1-Motion>",paint)            # 鼠标拖曳绑定paint

tk.mainloop()

