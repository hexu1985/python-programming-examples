# ch17_28.py 
from tkinter import * 
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter.scrolledtext import ScrolledText #as Text

def newFile():
    text.delete("1.0",END)
    root.title("Untitled")
def openFile():
    global filename
    filename = askopenfilename()
    if filename == "":
        return
    with open(filename,"r") as fileObj:
        content = fileObj.read()
    text.delete("1.0",END)
    text.insert(END,content)
    root.title(filename)

def saveAsFile():
    global filename
    textContent = text.get("1.0",END)
    
    filename = asksaveasfilename(defaultextension=".txt")
    print("传递回来的文件路径是:   ",filename)
    if filename == "":
        return
    with open(filename,"w") as output:
        output.write(textContent)
        root.title(filename)
filename = "Untitled"
root = Tk() 
root.title(filename) 
root.geometry("300x180") 

menubar = Menu(root)          # 建立最上层菜单
# 建立菜单类别对象，并将此菜单命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)
# 在File菜单内建立菜单列表
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Open File ...",command=openFile)
filemenu.add_command(label="Save As ...",command=saveAsFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
root.config(menu=menubar)

# 建立Text 
text = ScrolledText(root,undo=True) 
text.pack(fill=BOTH,expand=True)

root.mainloop() 

