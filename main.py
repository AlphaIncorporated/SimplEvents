from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
root.title('SimplEvents')

#fullscreen
#root.attributes('-fullscreen', True)

mainframe = Frame(root)
#neweventdaysframe = Frame(root)

mainframe = LabelFrame(root, text = "mainframe", padx = 1920, pady = 1080)
mainframe.pack(padx = 10, pady = 10)

'''
def change_to_neweventdaysframe():
    neweventdaysframe.pack(fill='both', expand=1)
    mainframe.pack_forget()
'''

neweventbutton = Button(mainframe, text = "New Event", font=("Arial", 25))
#neweventbutton.grid(row=0,column=0)

neweventbutton.place(x = 20, y = 30, width=120, height=25)
Button(neweventbutton.master,
              text="New Event",
  
              #font size
              font=("Arial", 25)
              ).pack()

'''
neweventdaysframe = LabelFrame(root, padx = 1920, pady = 1080)
neweventdaysframe.pack(padx = 10, pady = 10)

neweventonedaybutton = Button(neweventdaysframe, text = "One Day")
neweventonedaybutton.grid(row=0,column=0)

neweventmultdaysbutton = Button(neweventdaysframe, text = "Multiple Days")
neweventmultdaysbutton.grid(row=0,column=1)
'''

root.mainloop()

'''
#title
root.title('SimplEvents')
root.iconbitmap('')
root.geometry("1280x720")
root.configure(bg='grey')

def neweventfunction():
    label3 = Button(root, text= "Same day", fg='blue')
    label4 = Button(root, text= "Multiple days", fg='blue')

#creating label widget
newEventButton = Button(root, text="New Event", command=neweventfunction, fg='black', bg='green',padx=150,pady=350) 
newEventButton.grid(row=0, column=0)

root.mainloop()
'''