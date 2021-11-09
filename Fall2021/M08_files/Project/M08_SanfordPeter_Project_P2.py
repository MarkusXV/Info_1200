#!usr/bin/env/python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 11/7/2021
#Project #: MO8_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

'''Import all of the gui modules'''
import tkinter as tk
from tkinter import ttk, messagebox

'''Sets up the class called Volume'''
class Volume(ttk.Frame):
    '''Defines the init function to initalize the variabels needed in the instances'''
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding = "20 20 20 20") # initalizes the initial frame for the gui
        self.parent = parent # sets the parent to the self parent so that each instance knows the parent
        self.message = "" # sets the message to an empty string so that we can use it later

        self.length = tk.StringVar() # sets the length variable to a string var so the gui can take it from the user
        self.width = tk.StringVar() # sets the width variable to a string var so the gui can take it from the user
        self.height = tk.StringVar() # sets the height variable to a string var so the gui can take it from the user
        self.volume = tk.StringVar() # sets the volume variable to a string var so the gui can display it in a read only entry box

        self.initComponents() # Each instance runs the initComponents function to set up the grid

    '''Display the grid of labels and text entry fields'''
    def initComponents(self):
        # First label with Length
        ttk.Label(self, text = "Length: ").grid(column = 0, row = 0, sticky = tk.E, pady = 3)
        # First entry box to input length and puts the value in the self.length variable
        ttk.Entry(self, width = 25, textvariable = self.length).grid(column = 1, row = 0, pady = 3)

        # Second label with Width
        ttk.Label(self, text = "Width: ").grid(column = 0, row = 1, sticky = tk.E, pady = 3)
        # Second entry box to input width and puts the value in the self.width variable
        ttk.Entry(self, width = 25, textvariable = self.width).grid(column = 1, row = 1, pady = 3)

        # Third label with height
        ttk.Label(self, text = "Height: ").grid(column = 0, row = 2, sticky = tk.E, pady = 3)
        # Third entry box to input height and puts the value in the self.height variable
        ttk.Entry(self, width = 25, textvariable = self.height).grid(column = 1, row = 2, pady = 3)

        # Fourth label with volume
        ttk.Label(self, text = "Volume: ").grid(column = 0, row = 3, sticky = tk.E, pady = 3)
        # Fourth entry box which is read only and displays the resulting volume
        ttk.Entry(self, width = 25, textvariable = self.volume, state = "readonly").grid(column = 1, row = 3, pady = 3)

        self.makeButtons() # Runs the makeButtons function to make the buttons at the bottom of the gui frame
        self.pack() # packs the frame so that it can be displayed in the gui

    '''Makes the buttons at the bottom of the frame for the user to click on'''
    def makeButtons(self):
        buttonFrame = ttk.Frame(self) # sets the button frame

        # SEts the grid of the buttons inside the button frame
        buttonFrame.grid(column = 0, row = 4, columnspan = 2, sticky = tk.E)

        # Makes a button that calls the calculate function when clicked
        ttk.Button(buttonFrame, text = "Calculate", command = self.calculate).grid(column = 0, row = 0, padx = 5)
        # Makes a button that calls the parent.destroy command whcih exits the guia nd exits the program
        ttk.Button(buttonFrame, text = "Exit", command = self.parent.destroy).grid(column = 1, row = 0)

    '''Calculates the volume from the length, width, and height and displays an error if the wrong value type is entered'''
    def calculate(self):
        try:
            length = float(self.length.get()) # Sets the variable length to the inputted value from the gui
            width = float(self.width.get()) # sets the variable width to the inputted value from the gui
            height = float(self.height.get()) # Sets the variable height to the inputted value from the gui
        except ValueError:
            self.message += f"Values need to be numbers.\n" # displays this message box if there's a value type error

        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.message = ""

        vol = length * width * height # Calculates the value of the volume

        self.volume.set(round(vol, 4)) # Puts the new volume into the self.volume variable so that the gui can display it


if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Right Triangle Calculator") # Sets the root title of the gui window
    Volume(root) # Calls the Volume class and passes in the root parent
    root.mainloop() # Starts the gui loop to display it
