# ch17_11.py 
from tkinter import * 

def selectedText():
    try:
        selText = text.get(SEL_FIRST,SEL_LAST)
        print("选取文字:",selText)
        # print("SEL_FIRST:",type(SEL_FIRST),"  SEL_LAST:",SEL_LAST)
        print("selectionStart:",text.index(SEL_FIRST))
        print("selectionEnd:",text.index(SEL_LAST))
    except TclError:
        print("没有选取文字")

root = Tk()
root.title("ch17_11")
root.geometry("300x180")

# 建立Button
btn = Button(root,text="Print selection",command=selectedText)
btn.pack(pady=3)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Love You Like A Love Song") # 插入文字

root.mainloop()

