from tkinter import *

window = Tk()
window.geometry("1024x200")
window.title("my window")
enter = Entry(window, width=20)

lb = Label(window, text="Label")

def chnge():
    lb.config(text=enter.get())

btn = Button(window, text="Button", command=chnge)

enter.grid(row=0, column=0)
lb.grid(row=5, column=2)
btn.grid()
window.mainloop()
