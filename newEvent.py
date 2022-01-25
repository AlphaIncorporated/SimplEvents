print("init newEvent page start")
from tkinter import *

root = Tk()

#function for the text aftet you enter the date
# def enteredDate():
#     enteredDateLbl = Label(root,text="the date you entered is: "+str(dateInpt.get()))
#     enteredDateLbl.grid(row=4,column=0,sticky=W)
def openOneDayForm():
    root.destroy()
    import newEventOneD

def openMultDayForm():
    root.destroy()
    import newEventMultD

print("init newEvent page")
#title
root.title('SimplEvents')
root.attributes('-fullscreen', True)
root.iconbitmap('')
root.geometry("1280x720")
root.configure(bg='grey')

#frame for stuff
newEventFrame = Frame(root, width=2000, highlightbackground='red', highlightthickness=3)#.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
newEventFrame.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
#the date label prompt 
newEvnLabel = Label(newEventFrame, text="New Event")
newEvnLabel.grid(row=0,column=1)
orLbl = Label(newEventFrame, text="or")
orLbl.grid(row=2,column=2)
#text input2
###dateInpt = Entry(newEventFrame, width=20, bg="white").grid(row=1, column=0)
#dateInpt.grid(row=2, column=0,sticky=W)
# dateInpt.pack()
##dateInpt.insert(0,"Enter the date:")

#button for confirming date input
####dateInptCfn = Button(newEventFrame,text="date input confirm", command=enteredDate, bg="grey").grid(row=2,column=0)
# dateInptCfn.pack()
multDBtn = Button(newEventFrame,text = "multiple day", command=openMultDayForm)
multDBtn.grid(row=2,column=3)
oneDBtn = Button(newEventFrame,text = "one day", command=openOneDayForm)
oneDBtn.grid(row=2,column=1)
#keeps the window/app/thingy open and running
root.mainloop()
