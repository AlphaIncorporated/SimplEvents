import matplotlib.pyplot as plt
from tkinter import *
import json
import tkinter as tk

def newBudget(self):
    #data
    size_of_groups=[]

    #categories
    Categories = []
    
    budgetScreen = Frame(self.mainFrame)
    budgetScreen.pack()
    
    def addButton():
        pass
    
    def saveinput(self):
        global Categories, size_of_groups
        try:
            categoryTitle = self.pieChartCategoryEntry.get()
            categoryData = int(self.pieChartValEntry.get())
            size_of_groups.append(categoryData)
            Categories.append(categoryTitle)
        except Exception as err:
            print(err)

    def updatepiechart():
        # create pieplot
        plt.pie(size_of_groups, labels=Categories)

        # add a circle at the center to transform it in a donut chart
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)

        plt.show()
    
    plusbutton = tk.Button(budgetScreent="+", width=20, command=addButton)
    plusbutton.pack()
    
    saveButton = tk.Button(budgetScreen, text = "Save", width=20, command = saveinput)
    saveButton.pack()

    updateButton = tk.Button(budgetScreen, text="Update Pie Chart", width=20, command=updatepiechart)
    updateButton.pack()