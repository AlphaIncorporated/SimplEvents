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

#defining them lists
#function
class budgetClss(tk.Frame):
    #class constructor
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.configure(background="white")
        
        def saveData1():
            a=dataValue1.get()
            dataValues.append(a)
            dataNameList.append("Food & Catering")
        def saveData2():
            b = dataValue2.get()
            dataValues.append(b)
            dataNameList.append("Contingency")
        def saveData3():
            c = dataValue3.get()
            dataValues.append(c)
            dataNameList.append("Decoration")
        def saveData4():
            d = dataValue4.get()
            dataValues.append(d)
            dataNameList.append("Entertainment")
        def saveData5():
            e = dataValue5.get()
            dataValues.append(e)
            dataNameList.append("Venue")
        def saveData6():
            f = dataValue2.get()
            dataValues.append(f)
            dataNameList.append("Photography/ Videography")
        def saveData7():
            g = dataValue7.get()
            dataValues.append(g)
            dataNameList.append("Gifts")
        dataNameList = []
        dataValues=[]
        
        #data1
        label1 = tk.Label(self,text = "Food & Catering", bg = 'white', font = ("Ariel, 30"))
        dataValue1 = tk.Entry(self,highlightthickness=2, bg = 'white',fg='black', font = ("Ariel, 30"))

        plusButton1 = tk.Button(self, text="Save", command=saveData1, font = ("Ariel, 20"))

        #data2
        label2 = tk.Label(self,text = "Contingency", bg = 'white', font = ("Ariel, 30"))
        dataValue2 = tk.Entry(self,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))

        plusButton2 = tk.Button(self, text="Save", command=saveData2, font = ("Ariel, 20"))
        #temp comment for tkinter to stop screaming pls

        #data3
        label3 = tk.Label(self,text = "Decoration", bg = 'white', font = ("Ariel, 30"))
        dataValue3 = tk.Entry(self,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))


        

        plusButton3 = tk.Button(self, text="Save", command=saveData3, font = ("Ariel, 20"))


        #data4
        label4 = tk.Label(self,text = "Entertainment", bg = 'white', font = ("Ariel, 30"))
        dataValue4 = tk.Entry(self,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))


        

        plusButton4 = tk.Button(self, text="Save", command=saveData4, font = ("Ariel, 20"))


        #data5
        label5 = tk.Label(self,text = "Venue", bg = 'white', font = ("Ariel, 30"))
        dataValue5 = tk.Entry(self,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))


        

        plusButton5 = tk.Button(self, text="Save", command=saveData5, font = ("Ariel, 20"))


        #data6
        label6 = tk.Label(self,text = "Photography/ Videography", bg = 'white', font = ("Ariel, 30"))
        dataValue6 = tk.Entry(self,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))


        

        plusButton6 = tk.Button(self, text="Save", command=saveData6, font = ("Ariel, 20"))


        #data7
        label7 = tk.Label(self,text = "Gifts", bg = 'white', font = ("Ariel, 30"))
        dataValue7 = tk.Entry(self,highlightthickness=2, background='white',fg='black', font = ("Ariel, 30"))


        

        plusButton7 = tk.Button(self, text="Save", command=saveData7, font = ("Ariel, 20"))

        def savesave():
            plt.pie(dataValues, labels=dataNameList)
            circle = plt.Circle((0, 0), radius=0.7, facecolor='white')
            plt.axis('equal')
            plt.gca().add_artist(circle)
            plt.legend(dataNameList, loc='lower right')
            plt.show()



        sussysave= tk.Button(self, text="Update Pie Chart", font = ("Ariel, 30"), command=savesave, )


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
