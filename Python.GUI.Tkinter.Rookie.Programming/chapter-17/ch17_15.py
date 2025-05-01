# ch17_15.py 
from tkinter import * 

root = Tk() 
root.title("ch17_15") 
root.geometry("300x180") 
# 建立Text 
text = Text(root) 

for i in range(1,10): 
    text.insert(END,str(i) + ' Python GUI设计王者归来 \n') 

# 设置书签 
text.mark_set("mark1","5.0") # 指定标签mark1
text.mark_set("mark2","8.0") # 指定标签mark2

# 设置书签
text.tag_add("tag1","mark1","mark2") # 将mark1和mark2之间的文字命名为tag1标签
text.tag_config("tag1",foreground="blue",background="lightyellow") # 为标签执行特定的编辑或绑定
text.pack(fill=BOTH,expand=True) 

root.mainloop() 

