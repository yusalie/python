from tkinter import *

window = Tk()
window.title("title")
window.geometry("500x400")


def submit_action():
    print("button clicked")


submit_button = Button(window, text="submit",
                       command=submit_action())

submit_button.pack()
window.mainloop()