from tkinter import *

self = Tk()
self.geometry('1920x1080')
self.title('SimplEvents')
self.attributes("-fullscreen", True)

mainframe = Frame(self, bg = 'red')
mainframe.pack(expand = True, fill = BOTH)

calendarimg = PhotoImage(file = "pictures/calenderbuttonpic.png", width = 970, height = 1190)

neweventbutton = Button(mainframe, text = "Calendar", width = 136, height = 40, borderwidth=0, bg = 'white')
neweventbutton.grid(row = 0, column = 1)

aboutusbutton = Button(mainframe, text = 'About Us', width = 136, height = 35, borderwidth=0, bg = 'white')
aboutusbutton.grid(row = 1, column = 1, sticky = S )

calendarbutton = Button(mainframe, text = "New Event", width = 965, height = 1135, borderwidth=0, image = calendarimg, bg = 'white')
calendarbutton.grid(row = 0, column = 0, rowspan = 2, sticky = W)

self.mainloop()