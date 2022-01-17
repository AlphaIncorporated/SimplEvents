from tkinter import *
from tkinter import ttk
from tkinter import font
import tkinter as tk

root = tk.Tk()
root.geometry('1920x1080')
root.title('SimplEvents')
root.attributes("-fullscreen", True)

mainframe = Frame(root, bg = 'white')
mainframe.pack(expand = True, fill = BOTH)

neweventbutton = Button(mainframe, text = "New Event", width = 136, height = 75,)
#neweventbutton.grid(row=0,column=0)

#neweventbutton.place(x = 20, y = 30, width=120, height=25)
neweventbutton.grid(row = 0, column = 0,  sticky = 'nsew')

calendarbutton = Button(mainframe, text = "Calendar", width = 136, height = 40)
calendarbutton.grid(row = 0, column = 1,  sticky = 'nsew')

aboutusbutton = Button(mainframe, text = 'About Us', width = 136, height = 35)
aboutusbutton.grid(row = 2, column = 1,  sticky = 'nsew')

root.mainloop()