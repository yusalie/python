from tkinter import *

window = Tk()
fndnum = Entry(window)
ans =Label()

def srt():
    
    srt_list = sorted(fndnum.get())
    
    
    ans.config(text="The sorted list is:" + str(srt_list))
    
btn= Button(window, height=1, width=20, command=srt, text="sort")

fndnum.grid()
btn.grid()
ans.grid()
window.mainloop()