from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def sel():
    msg = "Your selected option is "+ str(var.get())
    option.config(text=msg)
    option.pack()


root.title("Learn About Radio Buttons")
root.iconbitmap("images/imgview.ico")
var = IntVar()

R1 = Radiobutton(root, text="Option 1", variable=var, value =1, command=sel)
R2 = Radiobutton(root, text="Option 2", variable=var, value =2, command=sel)
R3 = Radiobutton(root, text="Option 3", variable=var, value =3 ,command=sel)

R1.pack(anchor=W)
R2.pack(anchor=W)
R3.pack(anchor=W)

option = Label(root)



root.mainloop()