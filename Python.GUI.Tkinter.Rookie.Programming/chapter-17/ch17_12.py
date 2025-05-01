# ch17_12.py 
from tkinter import * 

def printIndex():
    print("INSERT :",text.index(INSERT))
    print("CURRENT:",text.index(CURRENT))
    print("END    :",text.index(END))
    print("******************************")

root = Tk()
root.title("ch17_12")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print index",command=printIndex)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song\n") # 插入文字
text.insert(END,"梦醒时分") # 插入文字

root.mainloop()

