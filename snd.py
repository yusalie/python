from playsound import playsound
from tkinter import filedialog
from tkinter import *
import wave
import simpleaudio as sa


window = Tk()
filename =  filedialog.askopenfilename(initialdir = "Desktop",title = "Select file",filetypes = ((".mp3","*.mp3"),("all files","*.*")))
def chse():
    f = wave.open(filename,'r')
    playsound(filename) 

def exit():
    window.destroy()


stp_btn = Button(window, text="stop")
    
btn = Button(window, command=chse, text="Select song", height=1, width=20)
exbtn = Button(window, command=exit, text="exit")
btn.grid()
stp_btn.grid()
exbtn.grid()
window.mainloop()