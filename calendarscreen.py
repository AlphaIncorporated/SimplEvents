from tkinter import *

root = Tk()
root.geometry('2304x1440')
root.title('SimplEvents')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)   
root.attributes('-fullscreen', True)
    
calendarframe = Frame(root)
calendarframe.pack(expand = True, fill = BOTH)

#def switchtomainframe():
    #root.destroy()
    #import main

#root.calendarbackbutton = Button(calendarframe, text = "Back")
#root.calendarbackbutton.grid(row = 0, column = 0)

root.mainloop()
