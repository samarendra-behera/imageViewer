from tkinter import *
from tkinter import ttk
root = Tk()

root.geometry('200x150+200+400')

def wish():
    msg = "Happy Birth Day!"
    my_label = Label(f1, text=msg,  pady=10)
    my_label.pack()



# Creating tab control
tabControl = ttk.Notebook(root)

#creting tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# define contents in tab1 and tab2
f1=LabelFrame(tab1, text="Hello World!", padx=50, pady=20)
f1.pack(padx=10, pady=10)
Label(f1, text="Today is Rimjhimi Barth Day!").pack()
Button(f1, text="wish her", padx=5, pady= 10, command=wish).pack()

f2= LabelFrame(tab2, text="Hello World!2", padx=50, pady=20)
f2.pack(padx=10, pady=10)
Label(f2, text="Do work day to night is good for Helth!").pack()


# add the tabs 
tabControl.add(tab1, text="tab 1")
tabControl.add(tab2, text="tab 2")

tabControl.pack(expand=1, fill="both")

root.mainloop()