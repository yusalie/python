# Imports libraries
from tkinter import filedialog
from tkinter import *
from pydub import AudioSegment
from os import path
from pygame import mixer
from tkinter import ttk
from tkinter.filedialog import askopenfilename


#Creates basic widgets
window = Tk()
window.geometry("560x215")
window.title("Audio Player")
select_song = Label(window, text="Select song:")
li = Listbox(window)
    
# Creates a function to exit the program
def exit():
    window.destroy()

#Creates a Function to add a song
def addSong():
    window.filename = askopenfilename(initialdir = "Desktop",title = "Select file",filetypes = (("Mp3 files","*.mp3"),("all files","*.*")))
    li.insert(END, window.filename)

# Button to add a song
add_btn = Button(window, text="Add song", command=addSong)

# Function to play and convert audio
def ply():
    mp3_src = li.get(END)
    conv_f = "test.wav"
    sound = AudioSegment.from_mp3(mp3_src)
    sound.export(conv_f, format="wav")
    mixer.init()
    mixer.music.load('test.wav')
    mixer.music.play()    

# Button to play audio
ply_btn = Button(window, command=ply, text="play")

# Function to stop audio
def stp():
    mixer.music.stop()

# Button to stop music
stp_btn = Button(window, text="stop", command=stp)

# Function to pause audio
def pse():
    mixer.music.pause()

# Button to pause audio   
pse_btn = Button(window, text="Pause", command=pse)

# Function to unpause audio
def unpse():
    mixer.music.unpause()

# Button to unpause audio
unpse_btn =Button(window, text="Unpause", command=unpse)

# Button to exit
exbtn = Button(window, command=exit, text="exit")

# Places widgets
stp_btn.place(x=56,y=1)
exbtn.place(x=112,y=1)
ply_btn.place(x=1, y=1)
pse_btn.place(x=160, y=1)
unpse_btn.place(x=226, y=1)
add_btn.place(x=300, y=1)
select_song.place(x=390, y=1)
li.place(x=390, y=18)
window.mainloop()