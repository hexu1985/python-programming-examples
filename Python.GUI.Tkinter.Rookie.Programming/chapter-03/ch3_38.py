from tkinter import * 
root = Tk()
root.title("ch3_38")
root.geometry("1280x800")

night = PhotoImage(file="snow.png")
label = Label(root,image=night)
label.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

root.mainloop()

