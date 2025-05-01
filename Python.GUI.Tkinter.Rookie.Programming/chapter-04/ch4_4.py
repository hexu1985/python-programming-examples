from tkinter import *

counter = 0                                # 计数的全局变量
def run_counter(digit):                    # 数字变量内容的更新   
    def counting():                        # 更新数字方法
        global counter                     # 定义全局变量
        counter += 1                       
        digit.config(text=str(counter))    # 列出数字内容
        # counter += 1
        digit.after(1000,counting)         # 隔一秒后调用counting
    counting()                             # 持续调用

root = Tk()
root.title("ch4_4")

digit = Label(root,bg="yellow",fg="blue",
                height=3,width=10,
                font="Helvetic 20 bold") 
digit.pack()   
run_counter(digit)   
Button(root,text="结束",width=15,command=root.destroy).pack(pady=10)  
root.mainloop()

