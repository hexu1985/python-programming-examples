# ch19_12.py
from tkinter import * 

tk = Tk()
canvas = Canvas(tk, width=640, height=480)
canvas.pack()

myStr = "Ming-Chi Institute of Technology"

canvas.create_text(200, 50, text=myStr)
canvas.create_text(200, 80, text=myStr, fill='blue')
canvas.create_text(300, 120, text=myStr, fill='blue',
                    font=('Old English Text MT',20))

tk.mainloop()

