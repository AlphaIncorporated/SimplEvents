from tkinter import *

root = Tk()

#title
root.title('SimplEvents')
root.iconbitmap('')
root.geometry("1280x720")
root.configure(bg='grey')

def neweventfunction():
    label3 = Button(root, text= "Same day", fg='blue')
    label4 = Button(root, text= "Multiple days", fg='blue')
    label3.pack()
    label4.pack()

#creating label widget
newEventButton = Button(root, text="New Event", command=neweventfunction, fg='black', bg='green',padx=150,pady=350)
newEventButton.grid(row=0, column=0)

root.mainloop()