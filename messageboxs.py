from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Show the Message boxes")
root.geometry('700x700')
width, height = root.winfo_screenwidth()/2, root.winfo_screenheight()/1.5
print('%dx%d+0+0' % (width,height))

# show information box
def show_info():
    info = messagebox.showinfo(title="your info", message= "Tkinter is good module...")
    print(info)
my_button = Button(root, text="Show Info", command=show_info)
my_button.pack()

#show warning message box
def show_warn():
    warn = messagebox.showwarning(title="you get warning", message="Something is warn you...")
    print(warn)
my_button2 = Button(root, text= "Show Warning", command= show_warn)
my_button2.pack()

#show error message box
def show_error():
    error = messagebox.showerror(title="you get a error", message="goodbye world!")
    print(error)
my_button3 = Button(root, text="Show Error", command=show_error)
my_button3.pack()

# show yes no window
def ask_yes_no():
    res = messagebox.askyesno(title="This is my Popup!", message="Hello World!")
    if(res):
        Label(root, text="You click yes!").pack()
    else:
        Label(root, text="You click no!").pack()

my_button4 = Button(root, text="you proceed", command=ask_yes_no)
my_button4.pack()

# show yes no window
def show_yes_no():
    res = messagebox.askquestion(title="This is my Popup!", message="Hello World!")
    print(res)

my_button4 = Button(root, text="you proceed", command=show_yes_no)
my_button4.pack()

# quit button is create
Button(root, text="Quit", command=root.quit).pack()


#YOu Can use these methos for your requirement

'''

tkinter.messagebox.askokcancel(title=None, message=None, **options)
tkinter.messagebox.askretrycancel(title=None, message=None, **options)
tkinter.messagebox.askyesnocancel(title=None, message=None, **options)

'''


root.mainloop()