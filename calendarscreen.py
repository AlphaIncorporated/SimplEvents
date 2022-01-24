from tkinter import *

class CalendarUI:
    
    root = Tk()
    root.geometry('2304x1440')
    root.title('SimplEvents')
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)   
    root.attributes('-fullscreen', True)
    
    def __init__(self, master):
        calendarframe = Frame(master)
        calendarframe.pack(expand = True, fill = BOTH)
    
        self.calendarbackbutton = Button(calendarframe, text = "Back")
        #, command = self.changetomainframe
        self.calendarbackbutton.grid(row = 0, column = 0)
    #def changetomainframe():
           # mainframe.pack(expand = True, fill = BOTH)
           # calendarframe.forget()

    root.mainloop()
