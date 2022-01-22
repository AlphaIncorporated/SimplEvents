from tkinter import *
from unittest import main
im

#screen
self = Tk()
self.geometry('2304x1440')
self.title('SimplEvents')
self.grid_columnconfigure(0, weight = 1)
self.grid_rowconfigure(0, weight = 1)   
self.attributes('-fullscreen', True)

class MainframeUI:
    def __init__(self, master):
        #mainFrame
        self.mainframe = Frame(self, bg = 'red')
        self.mainframe.pack(expand = True, fill = BOTH)
        self.mainframe.pack(expand = True, fill = BOTH)

    #change frame functions
    def changetocalendar(self):
        self.mainframe.forget()
        CalendarUI(self)
        
    def changetomainframe(self):
        self.mainframe.pack(expand = True, fill = BOTH)
        calendarframe.forget()

    #grid configs
    self.mainframe.grid_rowconfigure(0, weight=0) # For row 0
    self.mainframe.grid_rowconfigure(1, weight=2) # For row 1
    self.mainframe.grid_columnconfigure(0, weight=1) # For column 0
    self.mainframe.grid_columnconfigure(1, weight=1) # For column 1

    #mainframe image declaring
    calendarimg = PhotoImage(file = "./pictures/calenderbuttonpic.png")
    neweventimg = PhotoImage(file = "./pictures/neweventbuttonpic.png")
    aboutusimg = PhotoImage(file = "./pictures/aboutusbuttonpic.png")

    #mainframe buttons
    calendarbutton = Button(self.mainframe, text = "Calendar", width = 965, height = 1135, borderwidth=0, image = calendarimg, bg = 'white', command = changetocalendar)
    calendarbutton.grid(row = 0, column = 0, rowspan = 2)

    neweventbutton = Button(self.mainframe, text = "New Event", width = 960, height = 575, borderwidth=0, image = neweventimg, bg = 'white')
    neweventbutton.grid(row = 0, column = 1)

    aboutusbutton = Button(self.mainframe, text = 'About Us', width = 957, height = 560, borderwidth=0, image = aboutusimg, bg = 'white')
    aboutusbutton.grid(row = 1, column = 1)
    
    for frame in (self.mainframe, calendarframe):
        frame.grid(row = 0, column = 0, sticky = 'nsew')
        
    self.mainloop()