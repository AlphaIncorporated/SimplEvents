from tkinter import *

self = Tk()
self.geometry('2304x1440')
self.title('SimplEvents')
self.grid_columnconfigure(0, weight = 1)
self.grid_rowconfigure(0, weight = 1)   
self.attributes('-fullscreen', True)

class CalendarUI:
    
    def __init__(self, master):
        calendarframe = Frame(master)
        calendarframe.pack(expand = True, fill = BOTH)
    
        self.calendarbackbutton = Button(calendarframe, text = "Back")
        #, command = self.changetomainframe
        self.calendarbackbutton.grid(row = 0, column = 0)
    #def changetomainframe():
           # mainframe.pack(expand = True, fill = BOTH)
           # calendarframe.forget()
            
calendar = CalendarUI(self)


self.mainloop()
        













self.mainloop()