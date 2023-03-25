import tkinter as tk
WINDOW_WIDTH = "800"
WINDOW_HEIGHT = "500"
WINDOW_NAME = "Project 2: Hotel Bidding with COR by Nico Bokhari"
WINDOW_BACKGROUND_COLOR = "#00274C"
TEXT_COLOR = "#FFCB05"
FONT = "Arial"
FONT_SIZE = 25

class App:
    
    _bid = 0.0
    _successor = ""
    
    def __init__(self):
        # Create window
        self.createWindow()
        
    def createWindow(self):
        self.win = tk.Tk(className=WINDOW_NAME)
        # set window size
        self.win.geometry(WINDOW_WIDTH + "x" + WINDOW_HEIGHT)
        # set window background
        self.win['background'] = WINDOW_BACKGROUND_COLOR
        #Create prompt
        self.promptBid = tk.Label(
            master=self.win,
            text = "Enter your Hotel Bid:",
            bg = WINDOW_BACKGROUND_COLOR,
            fg = TEXT_COLOR,
            font = (FONT, FONT_SIZE)
        )
        #Place prompt
        self.promptBid.place(
            relx = 0.05,
            rely = 0.1, 
            anchor ="nw"
        )
        #Create input text field
        self.inputBid = tk.Entry(
            master = self.win,
            width = 25,
            font = (FONT, FONT_SIZE)
        )
        #Place input field
        self.inputBid.place(
            relx = 0.05,
            rely = 0.2,
        )
        #Create Error Label
        self.errorLabel = tk.Label(
            master=self.win,
            text = "",
            bg = WINDOW_BACKGROUND_COLOR,
            fg = TEXT_COLOR,
            font = (FONT, FONT_SIZE - 5)
        )
        #Place Error Label
        self.errorLabel.place(
            relx = 0.05,
            rely = 0.3
        )
        #Create Submit Button 
        self.submitButton = tk.Button(
            master = self.win,
            text = "Submit",
            bg = WINDOW_BACKGROUND_COLOR,
            fg = TEXT_COLOR,
            font = (FONT, FONT_SIZE - 5),
            command = self.onSubmit
        )
        #Place Submit Button 
        self.submitButton.place(
            relx = 0.05,
            rely = 0.4
        )
    
    
    def onSubmit(self):
        #clear error label text
        self.errorLabel.config(
            text = ""
        )
        #get input value from inputBid Entry
        value = self.inputBid.get() 
        if value != "":
            try:
                self.bid = float(value) # convert bid to float
                
                print(self.bid)
                
            except ValueError: # if bid conversion returns error

                self.errorLabel.config(
                    text = "Error: Please enter a number"
                )
            except: 
                print("I'm in the except condition")
            self.inputBid.delete(0, tk.END) # Remove text in field

