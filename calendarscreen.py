'''
=======================================================
author: Alfred Kang
summary:
creates interactable calendar(only for current month)
Has buttons to:
- Change to New Event frame
- View events added for date pressed
- Go back to previous frame
features:
- Able to identify current month, length of month, first day of month to reformat the calendar
- Number of date buttons change according to length of current month
- Every button leads to a frame where the label displays the events for that current day(and it has a back button)
=======================================================
'''
from tkinter import *
from calendar import *
import calendar
import json
import os
from datetime import datetime
from  newEventForm  import newEventForm

def calendarScreen(self):
    def back(self, calendarframe):
        self.uiFrame.pack(expand = True, fill = BOTH)
        calendarframe.pack_forget()
    def switchtoneweventframe(self):
        
        newEventFormObj = newEventForm(self).place(in_=self, anchor="c", relx=.5, rely=.5, relheight=1, relwidth=1)
    
    self.calendarframe = Frame(self.mainFrame, bg = 'white')
    self.calendarframe.pack(expand = True, fill = BOTH)

    #find current date
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    
    monthnow = ''
    if currentMonth == "1":
        monthnow = 'January'
    elif currentMonth == '2':
        monthnow = str('February')
    elif currentMonth == '3':
        monthnow = 'March'
    elif currentMonth == '4':
        monthnow = 'April'
    elif currentMonth == '5':
        monthnow = 'May'
    elif currentMonth == '6':
        monthnow = 'June'
    elif currentMonth == '7':
        monthnow = 'July'
    elif currentMonth == '8':
        monthnow = 'Augest'
    elif currentMonth == '9':
        monthnow = 'September'
    elif currentMonth == '10':
        monthnow = 'October'
    elif currentMonth == '11':
        monthnow = 'November'
    elif currentMonth == '12':
        monthnow = 'December'
  
    first_weekday, num_days_in_month = calendar.monthrange(currentYear, currentMonth)

    #finding out first day of month
    if (calendar.day_name[first_weekday]) == "Monday":
        firstdaycolumn = 0
    elif (calendar.day_name[first_weekday]) == "Tuesday":
        firstdaycolumn = 1
    elif (calendar.day_name[first_weekday]) == "Wednesday":
        firstdaycolumn = 2
    elif (calendar.day_name[first_weekday]) == "Thursday":
        firstdaycolumn = 3
    elif (calendar.day_name[first_weekday]) == "Friday":
        firstdaycolumn = 4
    elif (calendar.day_name[first_weekday]) == "Saturday":
        firstdaycolumn = 5
    elif (calendar.day_name[first_weekday]) == "Sunday":
        firstdaycolumn = 6
    
    #back button
    backbutton = Button(self.calendarframe, text = '< Back', font = ("Ariel, 30"), bg = 'white', fg = 'blue', borderwidth = 0 ,command=(lambda: back(self, self.calendarframe)))
    backbutton.grid(row = 0, column = 0, sticky = '')

    #Calendar Title
    calendartitle = Label(self.calendarframe, text = "Calendar", font = ("Ariel, 50"), bg = 'white', fg = "black")
    calendartitle.grid(row = 0, column = 1, columnspan=4, pady = 10)

    #neweventbutton
    calendartoneweventbutton = Button(self.calendarframe, text = "New Event", width = 35, height = 5, padx = 5, command = lambda: switchtoneweventframe(self))
    calendartoneweventbutton.grid(row = 0, column = 5, columnspan=2, sticky = '', pady = 10)

    #Day of the Week Label
    calendardayslabelmonday = Label(self.calendarframe, text = 'Monday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelmonday.grid(row = 2, column = 0)
    calendardayslabeltuesday = Label(self.calendarframe, text = 'Tuesday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabeltuesday.grid(row = 2, column = 1)
    calendardayslabelwednesday = Label(self.calendarframe, text = 'Wednesday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelwednesday.grid(row = 2, column = 2)
    calendardayslabelthursday = Label(self.calendarframe, text = 'Thursday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelthursday.grid(row = 2, column = 3)
    calendardayslabelfriday = Label(self.calendarframe, text = 'Friday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelfriday.grid(row = 2, column = 4)
    calendardayslabelsaturday = Label(self.calendarframe, text = 'Saturday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelsaturday.grid(row = 2, column = 5)
    calendardayslabelsunday = Label(self.calendarframe, text = 'Sunday', font = ("Ariel, 20"), bg = 'white', fg = "black")
    calendardayslabelsunday.grid(row = 2, column = 6)
    
    #frame to display events on day pressed
    def createEventDayFrame(self, buttonname):
        self.buttonpressed = buttonname
        # print(self.buttonpressed)
        self.calendarframe.pack_forget()
        eventDayFrame = Frame(self.mainFrame, bg = 'white')
        eventDayFrame.pack()
        
        # print('retrieveForm')
        retrievedEvents = ""
        eventRetrieve = {}
        eventRetrieve['startDate']=str(buttonname)
        # print("this start date:",eventRetrieve['startDate'])
        with open("./database/eventCollection.json", 'r') as f:
            eventCollectionData = json.load(f)
            for event in eventCollectionData["events"]:
                # if (event["startDate"]==eventRetrieve['startDate']):
                # print(int(eventRetrieve['startDate']),int(eventRetrieve['endDate'])+1)
                if event['endDate'] != "":
                    if event['startDate'] != "":
                        if buttonname in range(int(event['startDate']),int(event['endDate'])+1):
                            retrievedEvents += "Event:\n" +event["eventName"] +"\n"+"Description:\n"+event["eventDesc"]+"\n\n"
                    

        def eventDayFrameBackFunc(self, eventDayFrame):
            eventDayFrame.pack_forget()
            self.calendarframe.pack(expand = True, fill = BOTH)

        eventDayFrameBack = Button(eventDayFrame, text = "< Back", bg = 'white', fg = 'blue', font = ("Ariel, 25"), borderwidth=0, command = lambda: eventDayFrameBackFunc(self, eventDayFrame))
        eventDayFrameBack.grid(row = 0, column = 0, sticky = W)

        eventsDate = Label(eventDayFrame, text = "Events on "+str(self.buttonpressed), bg = 'white', fg = 'black', font = ("Ariel, 30"))
        eventsDate.grid(row = 1, column = 0, columnspan = 8, pady = 20, sticky = '')
        eventsInDay = Label(
            eventDayFrame, 
            ##-------------------part for the data to be chucked in-----------------------------------------
            text = retrievedEvents, 
            font = ("Ariel, 30"), 
            bg = 'white', 
            fg = 'black')
        eventsInDay.grid(row = 2, column = 0, columnspan = 8, sticky = '') 

        
        
    #making daybuttons
    if monthrange(currentYear, currentMonth)[1] == 28:
        day = dict()
        calendarrow = 3
        calendarcolumn = firstdaycolumn
        if datetime.now().day > 27:
            jsonPath = './database/eventCollection.json'
            os.remove(jsonPath)
            if not os.path.isfile(jsonPath): ##utiliseies is 
                with open("./database/eventCollection.json", "x") as outfile: ##outfile is file object 
                    json.dump({"events": []}, outfile)
        for x in range(1, 29):
            day[x] = x + 1
            day[x] = Button(self.calendarframe, 
            text = x, 
            width = 20, 
            height = 8, 
            borderwidth = 0, 
            bg = 'white', 
            command = lambda buttonname = x : createEventDayFrame(self, buttonname))
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
        calendarcolumn = firstdaycolumn
        if datetime.now().day > 28:
            print('clear json')
            jsonPath = './database/eventCollection.json'
            os.remove(jsonPath)
            if not os.path.isfile(jsonPath): ##utiliseies is 
                with open("./database/eventCollection.json", "x") as outfile: ##outfile is file object 
                    json.dump({"events": []}, outfile)
        for x in range(1, 30):
            day[x] = x + 1
            day[x] = Button(self.calendarframe, text = x, width = 22, height = 9, borderwidth = 0, bg = 'white', command = lambda buttonname = x : createEventDayFrame(self, buttonname))
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
        calendarcolumn = firstdaycolumn
        if datetime.now().day > 29:
            print('clear json')
            jsonPath = './database/eventCollection.json'
            os.remove(jsonPath)
            if not os.path.isfile(jsonPath): ##utiliseies is 
                with open("./database/eventCollection.json", "x") as outfile: ##outfile is file object 
                    json.dump({"events": []}, outfile)
        for x in range(1, 31):
            day[x] = x + 1
            day[x] = Button(self.calendarframe, text = x, width = 22, height = 9, borderwidth = 0, bg = 'white', command = lambda buttonname = x : createEventDayFrame(self, buttonname))
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
        calendarcolumn = firstdaycolumn
        if datetime.now().day > 30:
            print('clear json')
            jsonPath = './database/eventCollection.json'
            os.remove(jsonPath)
            if not os.path.isfile(jsonPath): ##utiliseies is 
                with open("./database/eventCollection.json", "x") as outfile: ##outfile is file object 
                    json.dump({"events": []}, outfile)
        for x in range(1, 32):
            day[x] = x + 1
            day[x] = Button(self.calendarframe, text = x, width = 22, height = 9, borderwidth = 0, bg = 'white', command = lambda buttonname = x : createEventDayFrame(self, buttonname))
            if calendarcolumn > 6:
                calendarrow = calendarrow + 2
                calendarcolumn = 0
                day[x].grid(row = calendarrow, column = calendarcolumn, rowspan = '2')
                calendarcolumn = calendarcolumn + 1
            else:
                day[x].grid(row = calendarrow, column = calendarcolumn, rowspan = '2')
                calendarcolumn = calendarcolumn + 1
            