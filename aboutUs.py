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
            height=600,
            width=800,
            bd=5,
            
            bg="blue")
        bodyFrame.pack(side='top', pady=(10,0))
        bodyFrame.pack_propagate(0)
        # bodyFrame.configure(width=800)

        aboutUsDescLabel = tk.Label(bodyFrame, 
            text="According to all known laws of aviation, \n there is no way a bee should be able to fly. \nIts wings are too small to get its fat little body off the ground. The bee, of course,\n flies anyway because bees don't care what humans think is impossible.\n Yellow, black. Yellow, black. Yellow, black.\n Yellow, black. Ooh, black and yellow!\n Let's shake it up a little. Barry! Breakfast is ready! Ooming! Hang on a second. Hello? - Barry? - Adam? - Oan you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. - You got lint on your fuzz. - Ow! That's me! - Wave to us! We'll be in row 118,000. - Bye! Barry, I told you, stop flying in", 
            bg="white",
            bd=2,
            fg='black',
            font=("Arial", 22),
            )
        aboutUsDescLabel.pack(side='top',fill=tk.BOTH)
        
    

        