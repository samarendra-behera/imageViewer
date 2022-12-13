from tkinter import *
from PIL import Image, ImageTk

root = Tk()

def imgback():
    return

def imgforward():
    return

# Add app Icon
root.iconbitmap('D:/Image Viewer app/images/imgview.ico')
root.title("Simple ImageViewer")

# resize the images
size = (400, 600)

# my images
my_img1 = ImageTk.PhotoImage(Image.open("images/img1.jpg").resize(size))
my_img2 = ImageTk.PhotoImage(Image.open("images/img2.jpg").resize(size))
my_img3 = ImageTk.PhotoImage(Image.open("images/img3.jpg").resize(size))


image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

# create button
button_back = Button(root, text="<<", command=imgback)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=imgforward)

# show in the screen
button_back.grid(row=1, column=0)
button_quit.grid(row= 1, column=1)
button_forward.grid(row = 1, column=2)
