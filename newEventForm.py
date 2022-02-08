import tkinter as tk
import os.path
import json
from tkinter import IntVar, messagebox

class newEventForm(tk.Frame):

    def prevPage(self, newEventForm):
        self.uiFrame.pack(expand = True, fill = BOTH)
        self.destroy()

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.configure(background="white")
        
        ##init
        isMultDay = tk.IntVar()
        dateStr = tk.StringVar()
        dateStr.set("Date:")
        
        ##define functions
        def saveForm():
            print('saveForm')
            formData = {}
            formData['eventName']=nameEntry.get() 
            formData['startDate']=date1Entry.get()
            formData['eventDesc']=descEntry.get()
            if (isMultDay.get()):
                formData['endDate']=date2Entry.get()
            else:
                formData['endDate']=date1Entry.get()
            if not os.path.isfile("./database/eventCollection.json"): ##utiliseies is 
                with open("./database/eventCollection.json", "x") as outfile: ##outfile is file object (the pointing thingy that also has metadata)
                    json.dump({"events": []}, outfile) ##dump takes (data, where the data goes)
            
            # unique name validation
            with open("./database/eventCollection.json", 'r') as f:
                eventCollectionData = json.load(f)
                for event in eventCollectionData["events"]:
                    if (event["eventName"]==formData['eventName']):
                        msg = "Event with name "+formData['eventName']+" already exists!"
                        messagebox.showerror(title="Validation Error",
                            message=msg)
                        return
            with open("./database/eventCollection.json", 'r+') as f:
                eventCollectionData = json.load(f)
                eventCollectionData["events"].append(formData)
                f.seek(0)
                json.dump(eventCollectionData, f, indent=4)
                f.truncate()    
            self.prevPage()
            



        def isMultDayFunc():
            print("isMultDay")
            if (isMultDay.get()):
                dateStr.set("Start Date:")
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
                date2Label.grid(row=2,column=2, sticky='w', pady=5)
                date2Entry.grid(row=2,column=3, sticky='we', pady=5)
            else:
                dateStr.set("Date:")
                date2Label.destroy()
                date2Entry.destroy()
        headerFrame = tk.Frame(
            self, 
            height=150,
            bg="white",
            highlightthickness=2)
        headerFrame.pack(side='top', fill='x')
        headerFrame.configure(height=headerFrame["height"],width=headerFrame["width"])
        headerFrame.pack_propagate(0)
        titleLbl =  tk.Label(
            headerFrame,
            text='NEW EVENT',
            bg="white",
            fg='black',
            font=("Arial", 58))
        titleLbl.pack(side='bottom')
        backBtn = tk.Button(
            headerFrame,
            text='Back',
            bg="white",
            fg='blue',
            font=("Arial", 42),
            command=self.prevPage)
        backBtn.place(anchor='nw', x=20, y=20)
        bodyFrame = tk.Frame(
            self, 
            height=600,
            bg="white")
        bodyFrame.pack(side='top', pady=(10,0))
        bodyFrame.configure(width=800)
        bodyFrame.grid_propagate(0)
        bodyFrame.grid_columnconfigure(0, weight=1) # For column 0
        bodyFrame.grid_columnconfigure(1, weight=1) # For column 1 
        bodyFrame.grid_columnconfigure(2, weight=1) # For column 2
        bodyFrame.grid_columnconfigure(3, weight=1) # For column 3

        nameLabel = tk.Label(bodyFrame, text="Event Name:",
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22))
        nameEntry = tk.Entry(bodyFrame,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        nameEntry.focus()
        nameLabel.grid(row=0,column=0, sticky='w', pady=5)
        nameEntry.grid(row=0,column=1, columnspan=3, sticky='we', pady=5)
        # ROW 1
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
        # ROW 2
        date1Label = tk.Label(bodyFrame, textvariable=dateStr,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22))
        date1Entry = tk.Entry(bodyFrame,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        date1Label.grid(row=2,column=0, sticky='w', pady=5)
        date1Entry.grid(row=2,column=1, sticky='we', pady=5)
        # ROW 3
        descLabel = tk.Label(bodyFrame, text="Description:",
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22))
        descEntry = tk.Entry(bodyFrame,
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            relief='sunken')
        descLabel.grid(row=3,column=0, sticky='w', pady=5)
        descEntry.grid(row=3,column=1, columnspan=3, sticky='we', pady=5)

        # save button
        saveBtn = tk.Button(
            self,
            text='Save',
            bg="white",
            fg='orange',
            font=("Arial", 42),
            command=saveForm)
        saveBtn.place(relx=1,rely=1, x=-30, y=-20, anchor='se')

        