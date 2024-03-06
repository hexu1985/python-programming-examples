# ch17_22.py 
from tkinter import * 

def spellingCheck():
    text.tag_remove("spellErr","1.0",END)
    textwords = text.get("1.0",END).split()
    print("字典内容\n",textwords)
    # print("#############dicts##############\n",dicts)
    # print("#############dicts##############")
    startChar = ("(")
    endChar = (".", ",", ":", ";", "?", "!", ")")

    start = "1.0"
    for word in textwords:
        if word[0] in startChar:
            word = word[1:]
        if word[-1] in endChar:
            word = word[:-1]
        if (word not in dicts and word.lower() not in dicts):
            print("error",word)
            pos = text.search(word,start,END)
            text.tag_add("spellErr",pos,"%s+%dc"%(pos,len(word)))
            pos = "%s+%dc" %(pos,len(word))

def clrText():
    text.tag_remove("spellErr","1.0",END)

root = Tk() 
root.title("ch17_22") 
root.geometry("300x180") 

# 建立工具栏
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

chkBtn = Button(toolbar,text="拼写检查",command=spellingCheck)
chkBtn.pack(side=LEFT,padx=5,pady=5)

clrBtn = Button(toolbar,text="清除",command=clrText)
clrBtn.pack(side=LEFT,padx=5,pady=5)

# 建立Text 
text = Text(root,undo=True) 
text.pack(fill=BOTH,expand=True)
text.insert(END,"Five Hundred Miles\n")           # 插入时同时设置Tag
text.insert(END,"If you miss the rain I am on,\n")
text.insert(END,"You will knw that I am gone.\n")
text.insert(END,"You can hear the whistle blw\n")
text.insert(END,"A hunded miles,\n")

text.tag_configure("spellErr", foreground="red")
with open("myDict.txt","r") as dictObj:
    dicts = dictObj.read().split('\n')

root.mainloop() 

