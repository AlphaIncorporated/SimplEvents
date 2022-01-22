from tkinter import *

self = Tk()
self.geometry('2304x1440')
self.title('SimplEvents')
self.grid_columnconfigure(0, weight = 1)
self.grid_rowconfigure(0, weight = 1)
self.attributes('-fullscreen', True)

mainframe = Frame(self, bg = 'red')
mainframe.pack(expand = True, fill = BOTH)

mainframe.grid_rowconfigure(0, weight=0) # For row 0
mainframe.grid_rowconfigure(1, weight=2) # For row 1
mainframe.grid_columnconfigure(0, weight=1) # For column 0
mainframe.grid_columnconfigure(1, weight=1) # For column 1

#image declaring
calendarimg = PhotoImage(file = "./pictures/calenderbuttonpic.png")
neweventimg = PhotoImage(file = "./pictures/neweventbuttonpic.png")
aboutusimg = PhotoImage(file = "./pictures/aboutusbuttonpic.png")

calendarbutton = Button(mainframe, text = "Calendar", width = 965, height = 1135, borderwidth=0, image = calendarimg, bg = 'white')
calendarbutton.grid(row = 0, column = 0, rowspan = 2)

neweventbutton = Button(mainframe, text = "New Event", width = 960, height = 575, borderwidth=0, image = neweventimg, bg = 'white')
neweventbutton.grid(row = 0, column = 1)

aboutusbutton = Button(mainframe, text = 'About Us', width = 957, height = 560, borderwidth=0, image = aboutusimg, bg = 'white')
aboutusbutton.grid(row = 1, column = 1)

self.mainloop()