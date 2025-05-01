# ch17_14.py 
from tkinter import * 

root = Tk() 
root.title("ch17_14") 
root.geometry("300x180") 

# 建立Text 
text = Text(root) 

for i in range(1,10): 
    text.insert(END,str(i) + ' Python GUI设计王者归来 \n') 

# 设置书签 
text.mark_set("mark1","5.0") 
text.mark_set("mark2","8.0") 

print(text.get("mark1","mark2")) 
text.pack(fill=BOTH,expand=True) 

root.mainloop() 

