# ch12_19.py
from tkinter import *
def itemAdded():
    varAdd = entry.get()
    if (len(varAdd.strip()) == 0):
        return
    lb.insert(END,varAdd)
    entry.delete(0,END)

def itemDeleted():
    index = lb.curselection()
    if (len(index)==0):
        return
    lb.delete(index)

root = Tk()
root.title("ch12_19")        # 窗口标题  
# root.geometry("300x250")     # 窗口宽300高210  

entry = Entry(root)
entry.grid(row=0,column=0,padx=5,pady=5)

# 建立“增加”按钮
btnAdd = Button(root,text="增加",width=10,command=itemAdded)
btnAdd.grid(row=0,column=1,padx=5,pady=5)

# 建立Listbox
lb = Listbox(root)
lb.grid(row=1,column=0,columnspan=2,padx=5,sticky=W)


# 建立“删除”按钮
btnDel = Button(root,text="删除",width=10,command=itemDeleted)
btnDel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

root.mainloop()

