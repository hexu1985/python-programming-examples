from tkinter import * 

cnt=1
def msgShow():
    global cnt
    # label["text"] = "I love Python x" + str(cnt)
    # label["bg"] = "lightyellow"
    # label["fg"] = "blue"
    label.config(text="I love Python x" + str(cnt),
            bg="lightyellow",fg="blue")
    cnt += 1

root = Tk()
root.title("ch4_3")
label = Label(root)
# label["text"] = "I love Java"
btn1 = Button(root,text="打印消息",width=15,command=msgShow)
btn2 = Button(root,text="结束",width=15,command=root.destroy)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)

root.mainloop()


