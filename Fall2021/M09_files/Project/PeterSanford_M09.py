#!usr/bin/env/ python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 11/13/2021
#Project #: MO9
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

'''Import all of the GUI modules'''
import tkinter as tk
from tkinter import ttk, messagebox

'''Sets up the class called Wizard'''
class Wizard(ttk.Frame):
    '''Defines the init function to initalize the variables needed in the instances'''
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding = "20 20 20 20") # initalizes the initial frame for the gui
        self.parent = parent # sets the parent to the self parent so that each instance knows the parent
        self.message = "" # sets the message to an empty string so that we can use it later

        self.item1 = tk.StringVar() = "" # sets the length variable to a string var so the gui can take it from the user
        self.item2 = tk.StringVar() = "" # sets the width variable to a string var so the gui can take it from the user
        self.item3 = tk.StringVar() = ""# sets the hypot variable toa string var so the gui can display it in a read only entry box
        self.item4 = tk.StringVar() = ""# sets the hypot variable toa string var so the gui can display it in a read only entry box
        
        self.initComponents() # Each instance runs the initComponents function to set up the grid

    '''Display the grid of labels and text entry fields'''
    def initComponents(self):
        
        ttk.Label(self, text = "Length: ").grid(column = 0, row = 0, sticky = tk.E, pady = 3)
        
        ttk.Entry(self, width = 25, textvariable = self.length).grid(column = 1, row = 0, pady = 3)
        
        # Second label with Width
        ttk.Label(self, text = "Width: ").grid(column = 0, row = 1, sticky = tk.E, pady = 3)
        # Second entry box to input width and puts the value in the self.length variable
        ttk.Entry(self, width = 25, textvariable = self.width).grid(column = 1, row = 1, pady = 3)

        # Third label with Hypotenuse
        ttk.Label(self, text = "Hypotenuse: ").grid(column = 0, row = 2, sticky = tk.E, pady = 3)
        # Third entry box which is read only and displays the resulting hypotenuse
        ttk.Entry(self, width = 25, textvariable = self.hypot, state = "readonly").grid(column = 1, row = 2, pady = 3)

        self.makeButtons() # Runs the makeButtons function to make the buttons at the bottom of the gui frame
        self.pack() # packs the frame so that it can be displayed in the gui

    '''Makes the buttons at the bottom of the frame for the user to click on'''
    def makeButtons(self):
        buttonFrame = ttk.Frame(self) # sets the button frame

        # Sets the grid of the buttons inside the button frame
        buttonFrame.grid(column = 0, row = 3, columnspan = 2, sticky = tk.E) 

        # Makes a button that calls the calculate function when clicked
        ttk.Button(buttonFrame, text = "Calculate", command = self.calculate).grid(column = 0, row = 0, padx = 5)
        # Makes a button that calls the parent.destroy command which exits the gui and exits the program
        ttk.Button(buttonFrame, text = "Exit", command = self.parent.destroy).grid(column = 1, row = 0)

    '''Calculates the hypotenuse from the length and width and displays an error if the wrong value type is entered'''
    def CheckValues(self):
        inventory = [] * 3

        try:
            length = float(self.length.get()) # Sets the variable length to the inputted value from the gui
            width = float(self.width.get()) # Sets the variable width to the inputted value from the gui
        except ValueError:
            self.message += f"Length and Width need to be a numbers.\n" # Displays this message box if there's a value type error

        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.message = ""

        c_squared = (length ** 2) + (width ** 2) # Calculates the value of the hypotenuse squared first
        hypot = (c_squared ** (1/2)) # takes hypotenuse squared and square roots it

        self.hypot.set(round(hypot, 3)) # Puts the new hypotenuse value into the self.hypot variable so that the gui can display it


    def show(self):

    def grab_item(self):

    def edit_item(self):

    def drop_item(self):

    

if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Right Triangle Calculator") # Sets the root title of the gui window
    Wizard(root) # calls the wizard class and passes in the root parent
    root.mainloop() # starts the gui loop to display it
    



            
