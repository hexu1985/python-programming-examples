# ch17_29.py 
from tkinter import * 
from PIL import Image, ImageTk

root = Tk() 
root.title("ch17_29") 
root.geometry("1000x750")
img = Image.open("bryant.jpg")
myPhoto = ImageTk.PhotoImage(img)

text = Text() 
text.image_create(END,image=myPhoto)
text.insert(END,"\n\n")
text.insert(END,"篮球巨星科比·布莱恩特")
text.pack(fill=BOTH,expand=True)

root.mainloop() 

