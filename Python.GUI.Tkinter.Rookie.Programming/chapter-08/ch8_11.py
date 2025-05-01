# ch8_11.py
from tkinter import *
import random
cnt = 0
root = Tk()
root.title("ch8_11")  
root.geometry("300x180")
msgYes, msgNo, msgExit = 1,2,3
def MessageBox():
    msgType = random.randint(1,3) # 随机产生一个整数，范围在1和3之间，包括1和3
    if msgType == msgYes:
        labTxt = "Yes"
    elif msgType == msgNo:
        labTxt = "No"
    elif msgType == msgExit:
        labTxt = "Exit"
    tl = Toplevel()
    tl.geometry("300x180")
    global cnt
    tl.title("Message Box"+str(cnt))
    cnt += 1
    Label(tl,text=labTxt).pack(fill=BOTH,expand=True)


btn = Button(root,text="Click Me",command = MessageBox)
btn.pack()

root.mainloop()
