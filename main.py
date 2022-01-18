from tkinter import *

self = Tk()
self.geometry('1920x1080')
self.title('SimplEvents')
self.attributes("-fullscreen", True)

mainframe = Frame(self, bg = 'red')
mainframe.pack(expand = True, fill = BOTH)

#image declaring
calendarimg = PhotoImage(file = "pictures/calenderbuttonpic.png", width = 970, height = 1190)
neweventimg = PhotoImage(file = "pictures/neweventbuttonpic.png", width = 970, height = 605)
aboutusimg = PhotoImage(file = "pictures/aboutusbuttonpic.png", width = 970, height = 555)

calendarbutton = Button(mainframe, text = "Calendar", width = 965, height = 1136, borderwidth=0, image = calendarimg, bg = 'white')
calendarbutton.grid(row = 0, column = 0, rowspan = 2, sticky = W)

neweventbutton = Button(mainframe, text = "New Event", width = 957, height = 575, borderwidth=0, image = neweventimg, bg = 'white')
neweventbutton.grid(row = 0, column = 1)

aboutusbutton = Button(mainframe, text = 'About Us', width = 957, height = 560, borderwidth=0, image = aboutusimg, bg = 'white')
aboutusbutton.grid(row = 1, column = 1, sticky = S )

self.mainloop()