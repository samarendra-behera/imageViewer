from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Simple Image Viewer")
root.iconbitmap('D:/Image Viewer app/images/imgview.ico')

my_image = ImageTk.PhotoImage(Image.open("images/img.jpg"))
my_label = Label(image=my_image)

my_label.pack()



button_quit = Button(root, text="Exit Program", command= root.quit)
button_quit.pack()
root.mainloop()