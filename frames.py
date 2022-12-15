from tkinter import *
root = Tk()

root.title("Frame Learning...")

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

btn = Button(frame, text="Click Me", padx=7, pady=5)
btn2 = Button(frame, text="Click Me", padx=7, pady=5)
btn3 = Button(frame, text="Click Me", padx=7, pady=5)

btn.grid(row=0, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=2, column=2)

root.mainloop()
