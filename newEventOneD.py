from tkinter import *

root = Tk()

#function for the text aftet you enter the date
#def enteredDate():
    #enteredDateLbl = Label(root,text="the date you entered is: "+str(dateInpt.get()))
    #enteredDateLbl.grid(row=4,column=0,sticky=W)

def backToNewEventForm():
    root.withdraw()
    import newEvent


print("init event1d page")
#title
root.title('SimplEvents')
root.iconbitmap('')
root.geometry("1280x720")
root.configure(bg='grey')

#frame for stuff
newEventFrame = Frame(root, width=2000, highlightbackground='red', highlightthickness=3)#.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
newEventFrame.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)

gridInGridFrame = Frame(newEventFrame,  highlightbackground='red', highlightthickness=3)#.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
gridInGridFrame.grid(row=2,column=3,)
strtLbl = Label(gridInGridFrame, text="Starts on:")
strtLbl.grid(row=2,column=2)
strtInpt = Entry(gridInGridFrame, width=20, bg="white")
strtInpt.grid(row=2, column=3)

#the date label prompt 
newEvnLabel = Label(newEventFrame, text="New Event")
newEvnLabel.grid(row=0,column=1)

titleLbl = Label(newEventFrame, text="Title:")
titleLbl.grid(row=1,column=2)

descLbl = Label(newEventFrame, text="Description:")
descLbl.grid(row=3,column=2)
#text input2
titleInpt = Entry(newEventFrame, width=20, bg="white")
titleInpt.grid(row=1, column=3)

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
