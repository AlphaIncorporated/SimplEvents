'''
=======================================================
author: Laavanya Sundaravel
summary:
Allows user to input their budget, and display it in a pie chart
form will allow users to input :
- budget for a range of catergories
features:
- takes in user input and displays information collated into a pie chart
- 
=======================================================
'''
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
#defining them lists
#function
class budgetClss(tk.Frame):
    #class constructor
    
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.configure(background="white")
        
        def prevPage(self,parent):
            parent.destroy()
        
        #formatting
        headerFrame = tk.Frame(
            self, 
            height=150,
            bg="white",
            highlightthickness=2)
        headerFrame.pack(side='top', fill='x')
        headerFrame.configure(height=headerFrame["height"],width=headerFrame["width"])
        headerFrame.pack_propagate(0)
        titleLbl =  tk.Label(
            headerFrame,
            text='Budget',
            bg="white",
            fg='black',
            font=("Arial", 58))
        titleLbl.pack(side='bottom')
        backBtn = tk.Button(
            headerFrame,
            text='< Back',
            bg="white",
            fg='blue',
            font=("Arial", 42),
            command=lambda: prevPage(self,parent))
        backBtn.place(anchor='nw', x=20, y=20)
        bodyFrame = tk.Frame(
            self, 
            height=700,
            width=1650,
            bd=5,
            
            bg="white")
        bodyFrame.pack(expand = True)
        bodyFrame.pack_propagate(0)
#======================================================================================================
        def savesave():
            plt.pie(dataValues, labels=dataNameList)
            circle = plt.Circle((0, 0), radius=0.7, facecolor='white')
            plt.axis('equal')
            plt.gca().add_artist(circle)
            plt.legend(dataNameList, loc='lower right',bbox_to_anchor=(1,0),bbox_transform=plt.gcf().transFigure)
            plt.show()


        def saveData1():
            a=dataValue1.get()
            if a.isdigit()==True:
                dataValues.append(a)
                dataNameList.append("Food & Catering") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        def saveData2():
            b = dataValue2.get()
            if b.isdigit()==True:
                dataValues.append(b)
                dataNameList.append("Contingency") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        def saveData3():
            c = dataValue3.get()
            if c.isdigit()==True:
                dataValues.append(c)
                dataNameList.append("Decoration") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        def saveData4():
            d = dataValue4.get()
            if d.isdigit()==True:
                dataValues.append(d)
                dataNameList.append("Entertainment") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        def saveData5():
            e = dataValue5.get()
            if e.isdigit()==True:
                dataValues.append(e)
                dataNameList.append("Venue") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        def saveData6():
            f = dataValue6.get()
            if f.isdigit()==True:
                dataValues.append(f)
                dataNameList.append("Photography/ Videography") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        def saveData7():
            g = dataValue7.get()
            if g.isdigit()==True:
                dataValues.append(g)
                dataNameList.append("Gifts") 
            else:
                tk.messagebox.showerror(title="showerror",message='Please enter an integer value into the budget.')
        dataNameList = []
        dataValues=[]
        
        #data1
        label1 = tk.Label(bodyFrame,text = "Food & Catering", bg = 'white', font = ("Ariel, 30"))
        dataValue1 = tk.Entry(bodyFrame,highlightthickness=2, bg = 'white',fg='black', font = ("Ariel, 30"))
        plusButton1 = tk.Button(bodyFrame, text="Save", command=saveData1, font = ("Ariel, 20"))

        #data2
        label2 = tk.Label(bodyFrame,text = "Contingency", bg = 'white', font = ("Ariel, 30"))
        dataValue2 = tk.Entry(bodyFrame,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))
        plusButton2 = tk.Button(bodyFrame, text="Save", command=saveData2, font = ("Ariel, 20"))

        #data3
        label3 = tk.Label(bodyFrame,text = "Decoration", bg = 'white', font = ("Ariel, 30"))
        dataValue3 = tk.Entry(bodyFrame,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))
        plusButton3 = tk.Button(bodyFrame, text="Save", command=saveData3, font = ("Ariel, 20"))

        #data4
        label4 = tk.Label(bodyFrame,text = "Entertainment", bg = 'white', font = ("Ariel, 30"))
        dataValue4 = tk.Entry(bodyFrame,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))
        plusButton4 = tk.Button(bodyFrame, text="Save", command=saveData4, font = ("Ariel, 20"))

        #data5
        label5 = tk.Label(bodyFrame,text = "Venue", bg = 'white', font = ("Ariel, 30"))
        dataValue5 = tk.Entry(bodyFrame,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))
        plusButton5 = tk.Button(bodyFrame, text="Save", command=saveData5, font = ("Ariel, 20"))

        #data6
        label6 = tk.Label(bodyFrame,text = "Photography/ Videography", bg = 'white', font = ("Ariel, 30"))
        dataValue6 = tk.Entry(bodyFrame,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))
        plusButton6 = tk.Button(bodyFrame, text="Save", command=saveData6, font = ("Ariel, 20"))


        #data7
        label7 = tk.Label(bodyFrame,text = "Gifts", bg = 'white', font = ("Ariel, 30"))
        dataValue7 = tk.Entry(bodyFrame,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))
        plusButton7 = tk.Button(bodyFrame, text="Save", command=saveData7, font = ("Ariel, 20"))

        sussysave= tk.Button(bodyFrame, text="Update Pie Chart", font = ("Ariel, 30"), command=savesave, )

        label1.grid(row=0, column=0, pady=2)
        label2.grid(row=1, column=0, pady=2)
        label3.grid(row=2, column=0, pady=2)
        label4.grid(row=3, column=0, pady=2)
        label5.grid(row=4, column=0, pady=2)
        label6.grid(row=5, column=0, pady=2)
        label7.grid(row=6, column=0, pady=2)
        dataValue1.grid(row=0,column=1,pady=2)
        dataValue2.grid(row=1,column=1,pady=2)
        dataValue3.grid(row=2,column=1,pady=2)
        dataValue4.grid(row=3,column=1,pady=2)
        dataValue5.grid(row=4,column=1,pady=2)
        dataValue6.grid(row=5,column=1,pady=2)
        dataValue7.grid(row=6,column=1,pady=2)
        plusButton1.grid(row=0, column=2,pady=2)
        plusButton2.grid(row=1, column=2,pady=2)
        plusButton3.grid(row=2, column=2,pady=2)
        plusButton4.grid(row=3, column=2,pady=2)
        plusButton5.grid(row=4, column=2,pady=2)
        plusButton6.grid(row=5, column=2,pady=2)
        plusButton7.grid(row=6, column=2,pady=2)
        sussysave.grid(row=7, column=0, pady=2)
