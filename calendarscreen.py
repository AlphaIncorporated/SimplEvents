from tkinter import *
from calendar import monthrange
from datetime import datetime

def calendarScreen(self):
    calendarframe = Frame(self.mainFrame, bg = 'white')
    calendarframe.pack(expand = True, fill = BOTH)

    #find current date
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    #Calendar Title
    calendartitle = Label(calendarframe, text = "Calendar", font = ("Ariel, 50"), bg = 'white')
    calendartitle.grid(row = 0, column = 0, columnspan=5, pady = 10)

    #neweventbutton
    calendartoneweventbutton = Button(calendarframe, text = "New Event", width = 44, height = 5, bg = 'white', borderwidth = 1)
    calendartoneweventbutton.grid(row = 0, column = 5, columnspan=2, sticky = E, pady = 10)

    #Day of the Week Label
    calendardayslabelmonday = Label(calendarframe, text = 'Monday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabelmonday.grid(row = 2, column = 0)
    calendardayslabeltuesday = Label(calendarframe, text = 'Tuesday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabeltuesday.grid(row = 2, column = 1)
    calendardayslabelwednesday = Label(calendarframe, text = 'Wednesday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabelwednesday.grid(row = 2, column = 2)
    calendardayslabelthursday = Label(calendarframe, text = 'Thursday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabelthursday.grid(row = 2, column = 3)
    calendardayslabelfriday = Label(calendarframe, text = 'Friday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabelfriday.grid(row = 2, column = 4)
    calendardayslabelsaturday = Label(calendarframe, text = 'Saturday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabelsaturday.grid(row = 2, column = 5)
    calendardayslabelsunday = Label(calendarframe, text = 'Sunday', font = ("Ariel, 30"), bg = 'white')
    calendardayslabelsunday.grid(row = 2, column = 6)
    
    #making daybuttons
    if monthrange(currentYear, currentMonth)[1] == 28:
        day = dict()
        calendarrow = 3
        calendarcolumn = 0
        for x in range(1, 29):
            day[x] = x + 1
            day[x] = Button(calendarframe, text = x, width = 22, height = 9, borderwidth = 0, bg = 'white')
            if calendarcolumn > 6:
                calendarrow = calendarrow + 2
                calendarcolumn = 0
                day[x].grid(row = calendarrow, column = calendarcolumn, rowspan = '2')
                calendarcolumn = calendarcolumn + 1
            else:
                day[x].grid(row = calendarrow, column = calendarcolumn, rowspan = '2')
                calendarcolumn = calendarcolumn + 1
            