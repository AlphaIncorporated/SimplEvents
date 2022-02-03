from tkinter import *
    

def calendarScreen(self):
    calendarframe = Frame(self.mainFrame)
    calendarframe.pack(expand = True, fill = BOTH)
    tempText = Label(calendarframe, text="This is a test") # Can be removed (Ethan)
    tempText.pack()

#def switchtomainframe():
    #root.destroy()
    #import main

#root.calendarbackbutton = Button(calendarframe, text = "Back")
#root.calendarbackbutton.grid(row = 0, column = 0)
