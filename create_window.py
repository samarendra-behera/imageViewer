from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Learn the creation of new window...")
root.iconbitmap("images/imgview.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("My second window is ...")
    top.iconbitmap('images/imgview.ico')
    my_img = ImageTk.PhotoImage(Image.open('images/img1.jpg').resize((400, 700)))
    Label(top, image=my_img).pack()

    #create the close new window btn
    Button(top, text="Close", command=top.destroy).pack()


frame = LabelFrame(root, text="my frame" , padx=50, pady=50 )
frame.pack(padx=10, pady=10)
Button(frame, text="click me", command=open).pack()

root.mainloop()
