from tkinter import * 
window = Tk()
window.title("ch3_36")

lab1 = Label(window,text="1明志科技大学",
                bg="lightyellow",width=15)         # 设置标签宽度15

lab2 = Label(window,text="2长庚大学",
                bg="lightgreen",width=15)          # 

lab3 = Label(window,text="3长庚科技大学",
                bg="lightblue",width=15)           # 

lab1.place(x=0,y=0)            # 
lab2.place(x=30,y=50)    #     
lab3.place(x=60,y=100)            # 

window.mainloop()

