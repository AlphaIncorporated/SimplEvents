from tkinter import *
from calendar import monthrange
from datetime import datetime

def calendarScreen(self):
    calendarframe = Frame(self.mainFrame, bg = 'white')
    calendarframe.pack(expand = True, fill = BOTH)

    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    
    if monthrange(currentYear, currentMonth)[1] == 28:
        day = dict()
        for x in range(1, 29):
            day[x] = x + 1
            day[x] = Button(calendarframe, text = x, width = 25, height = 10)
            day[x].grid(row = 0, column = x + 1)
            