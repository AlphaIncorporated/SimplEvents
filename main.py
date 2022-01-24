from tkinter import *
from calendarscreen import CalendarUI

root = Tk()
root.geometry('2304x1440')
root.title('SimplEvents')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.attributes('-fullscreen', True)

class App():
    def __init__(self, parent):
        self.setupWidgets(self)
    
    def setupWidgets(self):
        self.mainframe = Frame(self, bg = 'red')
        self.mainframe.pack(expand = True, fill = BOTH)

        self.mainframe.grid_rowconfigure(0, weight=0) # For row 0
        self.mainframe.grid_rowconfigure(1, weight=2) # For row 1
        self.mainframe.grid_columnconfigure(0, weight=1) # For column 0
        self.mainframe.grid_columnconfigure(1, weight=1) # For column 1 

        #change frame functions
        def changetocalendar(self): 
            self.mainframe.forget()
            CalendarUI(self)
            
        def changetomainframe(self):
            self.mainframe.pack(expand = True, fill = BOTH)
            self.calendarframe.forget()
                
        #image declaring
        calendarimg = PhotoImage(file = "./pictures/calenderbuttonpic.png")
        neweventimg = PhotoImage(file = "./pictures/neweventbuttonpic.png")
        aboutusimg = PhotoImage(file = "./pictures/aboutusbuttonpic.png")

        calendarbutton = Button(self.mainframe, text = "Calendar", width = 965, height = 1135, borderwidth=0, image = calendarimg, bg = 'white', command=lambda: self.changetocalendar(self))
        calendarbutton.grid(row = 0, column = 0, rowspan = 2)

        neweventbutton = Button(self.mainframe, text = "New Event", width = 960, height = 575, borderwidth=0, image = neweventimg, bg = 'white')
        neweventbutton.grid(row = 0, column = 1)

        aboutusbutton = Button(self.mainframe, text = 'About Us', width = 957, height = 560, borderwidth=0, image = aboutusimg, bg = 'white')
        aboutusbutton.grid(row = 1, column = 1)

    root.mainloop()