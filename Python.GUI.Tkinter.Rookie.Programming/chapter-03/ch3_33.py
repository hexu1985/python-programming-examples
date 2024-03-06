from tkinter import *  

window = Tk()
window.title("ch3_31")

lab1 = Label(window,text="明志工专1",relief="raised") 
lab2 = Label(window,bg="yellow",width=20) 
lab3 = Label(window,text="明志科技大学3",relief="raised") 
lab4 = Label(window,bg="aqua",width=20) 


lab1.grid(row=0,column=0,padx=5,pady=5)       # 格状包装
lab2.grid(row=0,column=1,padx=5,pady=5)       # 格状包装
lab3.grid(row=1,column=0,padx=5)       # 格状包装
lab4.grid(row=1,column=1,padx=5)       # 格状包装

window.mainloop()

