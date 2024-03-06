# ch13_4.py 
from tkinter import * 
def printSelection(): 
    print("The selection is : ",var.get()) 

root = Tk()
root.title("ch13_4")
root.geometry("300x180")

omTuple = ("Python","Java","C")       # 使用元组
# omTuple = ["Python","Java","C"]     # 使用列表
var = StringVar(root)
var.set("Python")
optionmenu = OptionMenu(root,var,*omTuple)
optionmenu.pack(pady=10)

btn = Button(root,text="Print",command=printSelection)
btn.pack(pady=10,anchor=S,side=BOTTOM)

root.mainloop()

