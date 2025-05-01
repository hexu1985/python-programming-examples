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
root.title("ch4_8")
root.geometry("600x600")
label = Label(root)
# label["text"] = "I love Java"

sunGif = PhotoImage(file="sun.gif")
btn = Button(root,image=sunGif,command=msgShow,
            text="Click Me",compound=CENTER)
label.pack()
btn.pack()

root.mainloop()


