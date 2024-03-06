# ch19_14.py
from tkinter import * 
from PIL import Image, ImageTk

tk = Tk()
img = Image.open("kobe.jpg")
myPic = ImageTk.PhotoImage(img)

canvas = Canvas(tk, width=img.size[0]+40,
                height=img.size[1]+30, bg='yellow')
canvas.create_image(200,15,anchor=NW,image=myPic)
canvas.pack(fill=BOTH,expand=True)

tk.mainloop()

