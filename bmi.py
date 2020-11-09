from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


window = Tk()
window.title("BMI calculator")


wBox = Entry(window, width=20)
hBox = Entry(window, width=20)
bmiBox = Text(window, height=1, width=20)
lbW = Label(window, text="Weight:")
lbH = Label(window, text="Height:")
lbBMI = Label(window, text="BMI:")
cb = ttk.Combobox(window, text="Select", values=["male", "female"])


def bmicalc():
    w = int(wBox.get())
    h = int(hBox.get())/100
    bmi = (w / (h**2))
    bmiBox.insert(END, round(bmi),2)
    return bmi

bCalc = Button(window, text="Calculate", command=bmicalc, height=1, width=5)

wBox.grid(row=1, column =1)
hBox.grid(row=2, column =1)
bCalc.grid(row=4, column =0)
cb.grid(row=4, column=1)
bmiBox.grid(row=3, column =1)
lbW.grid(row=1, column =0, sticky=W)
lbH.grid(row=2, column =0, sticky=W)
lbBMI.grid(row=3, column =0, sticky=W)
window.mainloop()