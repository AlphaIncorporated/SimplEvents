'''
=======================================================
author: Alfred Kang, Lai Wan Lin 
summary:
Shows a simple description about us
form will allow users to see:
- more about this app
- more about why we made this app 
- more about us
features:
- back button
=======================================================
'''
##stuff needed for bout us page: back button, desc box, title label, 

import tkinter as tk
import os.path
import json
from tkinter import IntVar, messagebox

class aboutUs(tk.Frame):

    def prevPage(self):
        self.destroy()
       
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.configure(background="white")
        
        ##init
        
        dateStr = tk.StringVar()
        dateStr.set("Date:")
        
        
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
            text='About Us',
            bg="white",
            fg='black',
            font=("Arial", 58))
        titleLbl.pack(side='bottom')
        backBtn = tk.Button(
            headerFrame,
            text='Back',
            bg="white",
            fg='blue',
            font=("Arial", 42),
            command=self.prevPage)
        backBtn.place(anchor='nw', x=20, y=20)
        bodyFrame = tk.Frame(
            self, 
            height=700,
            width=1650,
            bd=5,
            
            bg="white")
        bodyFrame.pack(expand = True)
        bodyFrame.pack_propagate(0)
        # bodyFrame.configure(width=800)

        aboutUsDescLabel = tk.Label(bodyFrame, 
            text="Hello! We are a group of Secondary Four students from the School of Science and Technology, Singapore. \n Alfred Kang (S401 2022), Lai Wan Lin (S401 2022), Laavanya Sundaravel (S401 2022)\n SimplEvents is a beginner's app made for our coursework project, aimed to make planning events simpler\n We used Python's Tkinter to create this application, and Visual Studio Code as our main text editor\n SimplEvents is most likely not going to be updated again, despite the many UI and code problems, and we do apologize for that.\n However, do expect more and better products from us, as we continue to hone our programming skills\n Thank you for using SimplEvents!", 
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            )
        aboutUsDescLabel.pack(side='top',fill=tk.BOTH)
        
    

        