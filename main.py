from tkinter import *
import tkinter as tk
from tkinter_custom_button import TkinterCustomButton

root = tk.Tk()
root.geometry('1920x1080')
root.title('SimplEvents')
root.attributes("-fullscreen", True)

mainframe = Frame(root, bg = 'white')
mainframe.pack(expand = True, fill = BOTH)

calendarbutton = Button(mainframe, text = "Calendar", width = 136, height = 40)
calendarbutton.grid(row = 0, column = 1,  sticky = W)

aboutusbutton = Button(mainframe, text = 'About Us', width = 136, height = 35)
aboutusbutton.grid(row = 1, column = 1)

neweventbutton = Button(mainframe, text = "New Event", width = 136, height = 75)
#neweventbutton.grid(row=0,column=0)

#neweventbutton.place(x = 20, y = 30, width=120, height=25)
neweventbutton.grid(row = 0, column = 0, rowspan = 2)

root.mainloop()