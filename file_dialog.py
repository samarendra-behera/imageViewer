from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
root = Tk()

root.title("File opener")
root.iconbitmap('images/imgview.ico')
root.geometry('400x500+400+200')

def openfile():
    global my_img
    filename = fd.askopenfilename(initialdir="images/", title="Select file type", filetypes= (("png file", ".png"), ("all files", "*.*")))
    #view the file 
    my_img = ImageTk.PhotoImage(Image.open(filename).resize((300, 400)))
    Label(image=my_img).pack()

Button(root, text="Open file", pady=5, padx=10, command=openfile).pack()


''' 
tkinter.filedialog.askopenfiles(mode='r', **options)
The above two functions create an Open dialog and return the opened file object(s) in read-only mode.

tkinter.filedialog.asksaveasfile(mode='w', **options)
Create a SaveAs dialog and return a file object opened in write-only mode.

tkinter.filedialog.askopenfilename(**options)
tkinter.filedialog.askopenfilenames(**options)
The above two functions create an Open dialog and return the selected filename(s) that correspond to existing file(s).

tkinter.filedialog.asksaveasfilename(**options)
Create a SaveAs dialog and return the selected filename.

tkinter.filedialog.askdirectory(**options)
Prompt user to select a directory.
Additional keyword option:
mustexist - determines if selection must be an existing directory.
class tkinter.filedialog.Open(master=None, **options)
class tkinter.filedialog.SaveAs(master=None, **options)
The above two classes provide native dialog windows for saving and loading files.

Convenience classes

The below classes are used for creating file/directory windows from scratch. These do not emulate the native look-and-feel of the platform.

class tkinter.filedialog.Directory(master=None, **options)
Create a dialog prompting the user to select a directory.
'''

root.mainloop()
