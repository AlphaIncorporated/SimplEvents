from tkinter import *
import tkinter as tk
from aboutUs import aboutUs
from calendarscreen import calendarScreen
from newEventForm import newEventForm
root = Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

root.geometry("1800x1000")
root.title('SimplEvents')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.configure(background='white')
#root.attributes('-fullscreen', True)

def new_func(root):
    root.mainFrame = Frame(root) # A new frame to 'govern' and contain all other frames

new_func(root)
root.mainFrame.pack()
root.uiFrame = Frame(root.mainFrame, bg = 'white')
root.uiFrame.pack(expand = True, fill = BOTH)

def switchtocalendarframe(root):
    root.uiFrame.pack_forget()
    calendarScreen(root)
def switchtoneweventframe(root):
    root.uiFrame.pack_forget()
    newEventFormObj = newEventForm(root).place(in_=root, anchor="c", relx=.5, rely=.5, relheight=1, relwidth=1)
    newEventFormObj()
def switchToAboutUsframe(root):
    root.uiFrame.pack_forget()
    aboutUsObj = aboutUs(root).place(in_=root, anchor="c", relx=.5, rely=.5, relheight=1, relwidth=1)
    
root.uiFrame.grid_rowconfigure(0, weight=0) # For row 0
root.uiFrame.grid_rowconfigure(1, weight=2) # For row 1
root.uiFrame.grid_columnconfigure(0, weight=1) # For column 0
root.uiFrame.grid_columnconfigure(1, weight=1) # For column 1 

#image declaring
calendarimg = PhotoImage(file = "./pictures/calenderbuttonpic.png")
neweventimg = PhotoImage(file = "./pictures/neweventbuttonpic.png")
aboutusimg = PhotoImage(file = "./pictures/aboutusbuttonpic.png")
 
calendarbutton = Button(root.uiFrame, text = "Calendar", width = 965, height = 1135, borderwidth=0, image = calendarimg, bg = 'white', command = lambda: switchtocalendarframe(root))
calendarbutton.grid(row = 0, column = 0, rowspan = 2 )
neweventbutton = Button(
    root.uiFrame,
    text = "New Event",
    width = 960,
    height = 575,
    borderwidth=0,  
    image = neweventimg,
    bg = 'white',
    command = lambda: switchtoneweventframe(root))
neweventbutton.grid(row = 0, column = 1)

aboutusbutton = Button(root.uiFrame, 
    text = 'About Us', 
    width = 957, 
    height = 560, 
    borderwidth=0, 
    image = aboutusimg, 
    bg = 'white',
    command= lambda:switchToAboutUsframe(root))
aboutusbutton.grid(row = 1, column = 1)

root.mainloop()
