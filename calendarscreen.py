from tkinter import *
from calendar import monthrange
from datetime import datetime
from  newEventForm  import newEventForm
def calendarScreen(self):
    def back(self, calendarframe):
        self.uiFrame.pack(expand = True, fill = BOTH)
        calendarframe.pack_forget()
    def switchtoneweventframe(self):
        self.uiFrame.pack_forget()
        newEventFormObj = newEventForm(self).place(in_=self, anchor="c", relx=.5, rely=.5, relheight=1, relwidth=1)
        newEventFormObj()
    # length=self.winfo_screenwidth()/10.5
    # height=self.winfo_screenheight()/10.5
    
    calendarframe = Frame(self.mainFrame, bg = 'white')
    calendarframe.pack(expand = True, fill = BOTH)

    #find current date
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    
    #back button
    backbutton = Button(calendarframe, bg = 'white', text = '< Back', font = ("Ariel, 20"), fg = "blue", borderwidth = 0 ,command=(lambda: back(self,calendarframe)))
    backbutton.grid(row = 0, column = 0)

    #Calendar Title
    calendartitle = Label(calendarframe, text = "Calendar", font = ("Ariel, 50"), bg = 'white', fg = "black")
    calendartitle.grid(row = 0, column = 1, columnspan=4, pady = 10)

    #neweventbutton
    calendartoneweventbutton = Button(calendarframe, text = "New Event", width = 44, height = 5, padx = 5,command = lambda: switchtoneweventframe(self))
    calendartoneweventbutton.grid(row = 0, column = 5, columnspan=2, sticky = E, pady = 10)

    #Day of the Week Label
    calendardayslabelmonday = Label(calendarframe, text = 'Monday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelmonday.grid(row = 2, column = 0)
    calendardayslabeltuesday = Label(calendarframe, text = 'Tuesday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabeltuesday.grid(row = 2, column = 1)
    calendardayslabelwednesday = Label(calendarframe, text = 'Wednesday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelwednesday.grid(row = 2, column = 2)
    calendardayslabelthursday = Label(calendarframe, text = 'Thursday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelthursday.grid(row = 2, column = 3)
    calendardayslabelfriday = Label(calendarframe, text = 'Friday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelfriday.grid(row = 2, column = 4)
    calendardayslabelsaturday = Label(calendarframe, text = 'Saturday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelsaturday.grid(row = 2, column = 5)
    calendardayslabelsunday = Label(calendarframe, text = 'Sunday', font = ("Ariel, 20"), bg = 'white', fg = "black")
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

    if monthrange(currentYear, currentMonth)[1] == 29:
        day = dict()
        calendarrow = 3
        calendarcolumn = 0
        for x in range(1, 30):
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

    if monthrange(currentYear, currentMonth)[1] == 30:
        day = dict()
        calendarrow = 3
        calendarcolumn = 0
        for x in range(1, 31):
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

    if monthrange(currentYear, currentMonth)[1] == 31:
        day = dict()
        calendarrow = 3
        calendarcolumn = 0
        for x in range(1, 32):
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
            