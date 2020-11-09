from tkinter import *

from tkinter import messagebox

window = Tk()

window.geometry("500x500")
def clck():
    messagebox.showinfo("message", "Hello")

btn = Button(window, text="Button", command=clck)
btn.grid()
window.mainloop()