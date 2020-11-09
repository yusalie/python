from tkinter import *
from tkinter import ttk

window = Tk()
fndnum = Entry(window)
entr = Entry(window, width=20)
ans =Label()

def srch():
    x = entr.get()
    y = fndnum.get()
    z = y.index(x)
    
    
    ans.config(text="The index is:" + str(z))
    
btn= Button(window, height=1, width=20, command=srch, text="Find index")

fndnum.grid()
entr.grid()
btn.grid()
ans.grid()
window.mainloop()