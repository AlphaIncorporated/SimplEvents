from tkinter import *

def CalendarUI(self):  
    calendarframe = Frame(self.mainframe)
    calendarframe.pack(expand = True, fill = BOTH)

    self.calendarbackbutton = Button(calendarframe, text = "Back")
    self.calendarbackbutton.grid(row = 0, column = 0)

    

    self.mainloop()