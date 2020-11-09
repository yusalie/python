from tkinter import *

window = Tk()
s = Entry(window, width=20)
items = Label(window)




def selection():
    x = s.get()
    w = items.config(text=sorted(x))
    

btn = Button(window, text="sort")    

s.grid()
btn.grid()
btn.grid()
window.mainloop()