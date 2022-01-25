print("init event2d page start")
from tkinter import *

root = Tk()

#function for the text aftet you enter the date
#def enteredDate():
    #enteredDateLbl = Label(root,text="the date you entered is: "+str(dateInpt.get()))
    #enteredDateLbl.grid(row=4,column=0,sticky=W)

def backToNewEventForm():
    root.destroy()
    import newEvent

print("init event2d page")

#title
root.title('SimplEvents')
root.iconbitmap('')
root.geometry("1280x720")
root.configure(bg='grey')
#frame for stuff
newEventFrame = Frame(root, width=2000, highlightbackground='red', highlightthickness=3)#.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
newEventFrame.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
newEventFrame.grid_columnconfigure(5, weight=1)
newEventFrame.grid_columnconfigure(3, weight=0)

startEndFrame = Frame(newEventFrame,  highlightbackground='red', highlightthickness=3)
startEndFrame.grid(row=2,column=3,sticky=W) #sticky=W doesnt work?? ueue
startEndFrame.grid_columnconfigure(5, weight=1)
# root.grid_columnconfigure(1, weight=3)

titleFrame = Frame(newEventFrame,  highlightbackground='blue', highlightthickness=3)
titleFrame.grid(row=1,column=3,sticky=W) #sticky=W doesnt work?? ueue

titleLbl = Label(titleFrame, text="Title:")
titleLbl.grid(row=1,column=2)
titleInpt = Entry(titleFrame, width=20, bg="white")
titleInpt.grid(row=1, column=3)


strtLbl = Label(startEndFrame, text="Starts on:")
strtLbl.grid(row=2,column=2)
strtInpt = Entry(startEndFrame, width=20, bg="white")
strtInpt.grid(row=2, column=3)

endsLbl = Label(startEndFrame, text="Ends on:")
endsLbl.grid(row=2,column=4)
endsInpt = Entry(startEndFrame, width=20, bg="white")
endsInpt.grid(row=2, column=5)
#the date label prompt 
newEvnLabel = Label(newEventFrame, text="New Event")
newEvnLabel.grid(row=0,column=1)



descLbl = Label(newEventFrame, text="Description:")
descLbl.grid(row=3,column=2)
#text input2


descInpt = Entry(newEventFrame, width=20, bg="white")
descInpt.grid(row=3, column=3)
#dateInpt.grid(row=2, column=0,sticky=W)
# dateInpt.pack()
##dateInpt.insert(0,"Enter the date:")

#button for confirming date input
####dateInptCfn = Button(newEventFrame,text="date input confirm", command=enteredDate, bg="grey").grid(row=2,column=0)
# dateInptCfn.pack()
saveBtn = Button(newEventFrame,text = "Save",)
saveBtn.grid(row=0,column=3, sticky=E)
backBtn = Button(newEventFrame,text = "back",command=backToNewEventForm)
backBtn.grid(row=0,column=4, sticky=E)
#keeps the window/app/thingy open and running
root.mainloop()
