from tkinter import *
from PIL import Image, ImageTk

root = Tk()



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

status = Label(root, text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)


def imgback(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command= lambda: imgforward(img_num+1))
    button_back = Button(root, text="<<", command= lambda: imgback(img_num-1))

    if(img_num ==1):
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="Image "+str(img_num)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=E+W)


def imgforward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command= lambda: imgforward(img_num+1))
    button_back = Button(root, text="<<", command= lambda: imgback(img_num-1))
    if(img_num==len(image_list)):
        button_forward=Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    status = Label(root, text="Image "+str(img_num)+" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=2, column=0, columnspan=3, sticky=E+W)


# create button
button_back = Button(root, text="<<", command=imgback, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: imgforward(2))

# show in the screen
button_back.grid(row=1, column=0)
button_quit.grid(row= 1, column=1)
button_forward.grid(row = 1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=E+W)



root.mainloop()