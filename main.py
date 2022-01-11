from tkinter import *

root = Tk()

#title
root.title('SimplEvents')
root.iconbitmap('')
root.geometry("500x500")
#creating label widget
label1 = Label(root, text="SimplEvents")
label2 = Label(root, text = "Events Made Simple")
#putting widget on screen
label1.grid(row=0, column = 1)
label2.grid(row=1, column = 1)
#loop
root.mainloop()

