# ch12_2.py 
from tkinter import * 

root = Tk()
root.title("ch12_2")                             # 窗口标题    
root.geometry("300x210")                         # 窗口宽300高210

lb = Listbox(root)              

# lb.insert(END,"Banana")
# lb.insert(END,"Watermelon")
# lb.insert(END,"Pineapple")

lb.insert(END,"香蕉")
lb.insert(END,"西瓜")
lb.insert(END,"菠萝")

lb.pack(pady=10)

root.mainloop()

