# ch12_6.py 
from tkinter import * 
fruits = [
    "Banana","Watermelon","Pineapple",
]

root = Tk()
root.title("ch12_6")                             # 窗口标题    
root.geometry("300x210")                         # 窗口宽300高210

lb = Listbox(root,selectmode=EXTENDED)              
for fruit in fruits:
    lb.insert(END,fruit)
lb.insert(ACTIVE,"Orange","Grapes","Mango")
lb.pack(pady=10)

root.mainloop()

