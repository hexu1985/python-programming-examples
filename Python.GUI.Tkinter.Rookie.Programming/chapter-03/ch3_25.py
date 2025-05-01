from tkinter import *
window = Tk()
window.title("ch3_25")

lab1 = Label(window,text="1明志科技大学",
                bg="lightyellow",width=15) # 设置标签宽度15

lab2 = Label(window,text="2长庚大学",
                bg="lightgreen",width=15)      # 

lab3 = Label(window,text="3长庚科技大学",
                bg="lightblue",width=15)   #


lab1.grid(row=0,column=0)       # 格状包装
lab2.grid(row=1,column=2)       # 
lab3.grid(row=2,column=1)       # 

window.mainloop()

