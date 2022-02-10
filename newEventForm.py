'''
=======================================================
author: Lai Wan Lin 
summary:
form for users to input details regarding new events
form will allow users to input :
- name of event
- a short description of event 
- date(s) of event
features:
- able to select single day event or multiple day event
- unique event name validation
- saves event information
=======================================================
'''

import tkinter as tk #
import os.path #helps pathing to assets
import json #allows conversion to json storage format
from tkinter import IntVar, messagebox 
#IntVar allows use of tkinter integer variables, messagebox allows a message box popup to be made

#makes newEventForm class
class newEventForm(tk.Frame):
    #define prevPage func
    def prevPage(self):
        #self.uiFrame.pack(expand = True, fill = BOTH)
        self.destroy()
    
    #class constructor
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.configure(background="white")
        
        ##initialise variables
        isMultDay = tk.IntVar()
        dateStr = tk.StringVar()
        dateStr.set("Date:")
        
        ##define functions

        #defines function  for saving form
        def saveForm():
            print('saveForm')
            #creating dict obj containing the users input
            formData = {}
            formData['eventName']=nameEntry.get() 
            formData['startDate']=date1Entry.get()
            formData['eventDesc']=descEntry.get()
            #sets the end date of the event to the start date in one day events
            if (isMultDay.get()):
                formData['endDate']=date2Entry.get()
            else:
                formData['endDate']=date1Entry.get()
            #makes new eventCollection.json file if there isn't already an existing one
            if not os.path.isfile("./database/eventCollection.json"): ##utiliseies is 
                with open("./database/eventCollection.json", "x") as outfile: ##outfile is file object 
                    json.dump({"events": []}, outfile) ##dump takes (data, where the data goes)
            
            # unique name validation
            with open("./database/eventCollection.json", 'r') as f:
                eventCollectionData = json.load(f)
                #checks the database for events with the same name as the new event name
                for event in eventCollectionData["events"]:
                    if (event["eventName"]==formData['eventName']):
                        msg = "Event with name "+formData['eventName']+" already exists!"
                        messagebox.showerror(title="Validation Error",
                            message=msg)
                        return
            # adds the new event details to the database
            with open("./database/eventCollection.json", 'r+') as f:
                eventCollectionData = json.load(f)

                #appends the new event details to a copy of the database data
                eventCollectionData["events"].append(formData)

                #sets file pointer to start of file 
                f.seek(0)
                
                #puts the copy of the new database data into the orignal database
                json.dump(eventCollectionData, f, indent=4)
                
                #removes the old data after the file pointer
                f.truncate()    
            #closes form
            self.destroy()
            
    
            

        #defines function for selecting whether an event is multiple days 
        def isMultDayFunc():
            print("isMultDay")
            if (isMultDay.get()):
                dateStr.set("Start Date:")
                #creating global label and global entry
                global date2Label
                date2Label = tk.Label(bodyFrame, text="End Date:",
                    bg="white",
                    bd=2,
                    fg='black',
                    font=("Arial", 22))
                global date2Entry
                date2Entry = tk.Entry(bodyFrame,
                    bg="white",
                    bd=2,
                    fg='black',
                    font=("Arial", 22),
                    relief='sunken')
                #positions the label and entry into the form
                date2Label.grid(row=2,column=2, sticky='w', pady=5)
                date2Entry.grid(row=2,column=3, sticky='we', pady=5)
            else:
                dateStr.set("Date:")
                date2Label.destroy()
                date2Entry.destroy()
        #headerframe to put title label and back button
        headerFrame = tk.Frame(
            self, 
            height=150,
            bg="white",
            highlightthickness=2)
        headerFrame.pack(side='top', fill='x')
        headerFrame.configure(height=headerFrame["height"],width=headerFrame["width"])
        headerFrame.pack_propagate(0)
        #label for title to indicate to user which  page of app they are on
        titleLbl =  tk.Label(
            headerFrame,
            text='NEW EVENT',
            bg="white",
            fg='black',
            font=("Arial", 58))
        titleLbl.pack(side='bottom')
        #button to return to previous page
        backBtn = tk.Button(
            headerFrame,
            text='Back',
            bg="white",
            fg='blue',
            font=("Arial", 42),
            command=self.prevPage)
        backBtn.place(anchor='nw', x=20, y=20)

        #bodyframe to put event form key contents
        bodyFrame = tk.Frame(
            self, 
            height=600,
            bg="white")
        bodyFrame.pack(side='top', pady=(10,0))
        bodyFrame.configure(width=800)

        #prevents frame from squishing
        bodyFrame.grid_propagate(0)
        #adds weight to columns
        bodyFrame.grid_columnconfigure(0, weight=1) # For column 0
        bodyFrame.grid_columnconfigure(1, weight=1) # For column 1 
        bodyFrame.grid_columnconfigure(2, weight=1) # For column 2
        bodyFrame.grid_columnconfigure(3, weight=1) # For column 3

        #label displayed next to nameEntry to give context to nameEntry
        nameLabel = tk.Label(bodyFrame, text="Event Name:",
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22))
        
        #Entry for users to input name of the event
        nameEntry = tk.Entry(bodyFrame,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        nameEntry.focus()
        nameLabel.grid(row=0,column=0, sticky='w', pady=5)
        nameEntry.grid(row=0,column=1, columnspan=3, sticky='we', pady=5)
        # ROW 1-------------------------------------------------------------------------------------------------
        #checkbutton for user to select whether event lasts multiple days or one day
        isMultDayCheckBtn = tk.Checkbutton(bodyFrame,
            text="Multi-day event",
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            variable=isMultDay,
            command=isMultDayFunc)
        isMultDayCheckBtn.deselect()
        isMultDayCheckBtn.grid(row=1, column=1, columnspan=3, sticky='w', pady=5)
        # ROW 2-------------------------------------------------------------------------------------------------
        #label displayed next to date1Entry to give Entry context
        date1Label = tk.Label(bodyFrame, textvariable=dateStr,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22))
        #Entry for user to input starting date for event
        date1Entry = tk.Entry(bodyFrame,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        date1Label.grid(row=2,column=0, sticky='w', pady=5)
        date1Entry.grid(row=2,column=1, sticky='we', pady=5)
        # ROW 3-------------------------------------------------------------------------------------------------
        #label displayed next to descEntry to give Entry context
        descLabel = tk.Label(bodyFrame, text="Description:",
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22))

        #Entry for user to input short description for event
        descEntry = tk.Entry(bodyFrame,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        descLabel.grid(row=3,column=0, sticky='w', pady=5)
        descEntry.grid(row=3,column=1, columnspan=3, sticky='we', pady=5)

        # button to save the user inputted form data into database and return to previous page
        saveBtn = tk.Button(
            self,
            text='Save',
            bg="white",
            fg='orange',
            font=("Arial", 42),
            command=saveForm)
        saveBtn.place(relx=1,rely=1, x=-30, y=-20, anchor='se')

        