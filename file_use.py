# imports libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb


# creates widgets
window = Tk()
window.title("Text files")
file_ = ttk.Combobox(window, width=20, value=["file.txt", "file2.txt", "file3.txt", "file5.txt", "file6.txt"])
file_write = Entry(window, width=20)
list_ = Text(window, height=5, width=20)

#Function to create file
def create_():
    f = open(file_.get(), "w+")
    f.close()
    
# Button creates file
btn = Button(window, text="create", width=5,height=1, command=create_)

# function to read file
def read_():
    f = open(file_.get(), "r")
    r = list_.insert(END, f.read())
    
    
# Button to read file
btn_read = Button(window, text="read", width=5,height=1, command=read_)

# Function to write to file
def write_():
    f = open(file_.get(), "a")
    f.write(file_write.get() + "\n")
    f.close()
    mb.showinfo("Confirm message", "Your text was added")
    
# Button to write to file 
btn_write = Button(window, text="write", width=5,height=1, command=write_)

# Function to clear widgets
def clr():
    file_.delete("0", END)
    file_write.delete("0", END)
    list_.delete('1.0', END)

# Button that clears widgets
btn_clear = Button(window, text="Clear", width=5,height=1, command=clr)

# Creats labels 
s_c = Label(window, text="Search or Create a file:")
wr = Label(window, text="Text to input:")
dt = Label(window, text="Data:")

# Packs widgets
s_c.grid(row=0, column=0, sticky=W)
wr.grid(row=1, column=0, sticky=W)
dt.grid(row=2, column=0, sticky=W)
file_.grid(row=0, column=1)
file_write.grid(row=1, column=1)
list_.grid(row=2, column=1)
btn.grid(row=3, column=1)
btn_read.grid(row=4, column=2)
btn_write.grid(row=4, column=1)
btn_clear.grid(row=3, column=2)
window.mainloop()    