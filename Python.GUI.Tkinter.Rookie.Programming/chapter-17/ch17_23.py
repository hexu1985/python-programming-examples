# ch17_23.py 
from tkinter import * 

def saveFile():
    textContent = text.get("1.0",END)
    filename = "ch17_23.txt"
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)

root = Tk() 
root.title("Untitled") 
root.geometry("300x180") 

menubar = Menu(root)          # 建立最上层菜单
# 建立菜单类别对象，并将此菜单命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)
# 在File菜单内建立菜单列表
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)

# 建立Text 
text = Text(root,undo=True) 
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")           # 插入时同时设置Tag
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")

root.mainloop() 

