# ch17_21.py 
from tkinter import * 

def mySearch():
    text.tag_remove("found","1.0",END)
    start = "1.0"
    key = entry.get()
    
    if (len(key.strip()) == 0):
        return
    while True:
        pos = text.search(key,start,END)
        # print("pos= ",pos) # pos=  3.0  pos=  4.0  pos=     
        if (pos == ""):
            break
        text.tag_add("found",pos,"%s+%dc" %(pos,len(key)))
        start = "%s+%dc" % (pos,len(key))
        # print("start= ",start) # start=  3.0+3c  start=  4.0+3c

root = Tk() 
root.title("ch17_21") 
root.geometry("300x180") 

root.rowconfigure(1,weight=1) 
root.columnconfigure(0,weight=1) 

entry = Entry() 
entry.grid(row=0,column=0,padx=5,sticky=W+E) 

btn = Button(root,text="查找",command=mySearch)
btn.grid(row=0,column=1,padx=5,pady=5)

# 建立Text 
text = Text(root,undo=True) 
text.grid(row=1,column=0,columnspan=2,padx=3,
                pady=5,sticky=N+S+W+E)
text.insert(END,"Five Hundred Miles\n")           # 插入时同时设置Tag
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

text.tag_configure("found", background="yellow")

root.mainloop() 

