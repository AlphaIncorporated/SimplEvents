from tkinter import *

root = Tk()

# function for the text aftet you enter the date
# def enteredDate():
#     enteredDateLbl = Label(root,text="the date you entered is: "+str(dateInpt.get()))
#     enteredDateLbl.grid(row=4,column=0,sticky=W)

# def openOneDayForm():
#     root.destroy()
#     import newBudgetOneD

# def openMultDayForm():
#     root.destroy()
#     import newBudgetMultD

#title
root.title('SimplEvents')
root.iconbitmap('')
root.geometry("1280x720")
root.configure(bg='grey')

#frame for stuff
newBudgetFrame = Frame(root, width=2000, highlightbackground='red', highlightthickness=3)#.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
newBudgetFrame.grid(row=0,column=0, padx=20, pady=20, ipadx=20, ipady=20)
#the date label prompt 
newBudgetLabel = Label(newBudgetFrame, text="Budget")
newBudgetLabel.grid(row=0,column=1)
orLbl = Label(newBudgetFrame, text="or")
orLbl.grid(row=2,column=2)
#text input2
###dateInpt = Entry(newBudgetFrame, width=20, bg="white").grid(row=1, column=0)
#dateInpt.grid(row=2, column=0,sticky=W)
# dateInpt.pack()
##dateInpt.insert(0,"Enter the date:")

#button for confirming date input
####dateInptCfn = Button(newBudgetFrame,text="date input confirm", command=enteredDate, bg="grey").grid(row=2,column=0)
# dateInptCfn.pack()
skipBudBtn = Button(newBudgetFrame,text = "Skip", )#command=openMultDayForm)
skipBudBtn.grid(row=2,column=3)
planBudBtn = Button(newBudgetFrame,text = "Plan budget", )#command=openOneDayForm)
planBudBtn.grid(row=2,column=1)
#keeps the window/app/thingy open and running
root.mainloop()
