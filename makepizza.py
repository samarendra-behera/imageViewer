from tkinter import *

root = Tk()
root.title("Pizza Maker")
root.iconbitmap("images/imgview.ico")

pizza = StringVar()
pizza.set("Pepproni Pizza")


def clicked(pname):
    my_label.config(text=pname)
    my_label.grid(row=2, column=0, columnspan=3, sticky=W+E)

MODES = [
    ("Pepproni", "Pepproni Pizza"),
    ("Chesse", "Chesse Pizza"),
    ("Onion", "Onion Pizza")
]

count =0

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).grid(row=0, column=count)
    count+=1

my_label = Label(root, text="Select the pizza")

myButton =Button(root, text="Order Pizza", command=lambda: clicked(pizza.get())).grid(row=1, column=0, columnspan=3, pady=10)


root.mainloop()