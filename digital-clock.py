# import tkinter for gui
from tkinter import *

# importing strftime function to capturing system's time
from time import strftime

# creating tkinter window
digital_clock = Tk()
digital_clock.geometry("600x300")
digital_clock.title('Digital Clock')


def time():
    # %h=hour ,%M=Minute ,%S=second ,p%=am or pm according to the given time value
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Increase the user experience designning the label widget


label = Label(digital_clock, font=('calibri', 40,       'bold'),
              background='#AA0000', foreground='white')

# clock at the centre of the tkinter window
label.pack(anchor='center')
time()  # call function

mainloop()
