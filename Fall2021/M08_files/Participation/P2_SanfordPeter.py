#!usr/bin/env/python3

'''Import all of the GUI modules and the math module for the value pi'''
import tkinter as tk
from tkinter import ttk, messagebox
import math

'''Sets up the class called CircValueFrame'''
class CircValueFrame(ttk.Frame): 
    '''Defines the init function to initalize the variables needed in the instances'''
    def __init__(self, parent): 
        ttk.Frame.__init__(self, parent, padding = "10 10 10 10") # initalizes the initial frame for the gui
        self.parent = parent # sets the parent to the self parent so that each instance knows the parent
        self.message = "" # sets the message to an empty string

        self.radius = tk.StringVar() # sets the radius function to a string var so the gui can take it from the user
        self.circ = tk.StringVar() # sets the radius function to a string var so the gui can take it from the user

        self.initComponents() # Each instance runs the initComponents function to set up the grid

    '''Display the grid of labels and text entry fields'''
    def initComponents(self):
        # First label with radius
        ttk.Label(self, text = "Radius: ").grid(column = 0, row = 0, sticky = tk.E, pady = 5) 
        # First entry box to input radius and puts value in the self.radius variable
        ttk.Entry(self, width = 25, textvariable = self.radius).grid(column = 1, row = 0)

        # Second label with Circumference
        ttk.Label(self, text = "Circumference: ").grid(column = 0, row = 1, sticky = tk.E, pady = 5)
        # Second entry box which is read only and displays the resulting circumference
        ttk.Entry(self, width = 25, textvariable = self.circ, state = "readonly").grid(column = 1, row = 1)

        self.makeButtons() # Runs the makeButtons function to make the buttons at the bottom of the gui frame
        self.pack() # packs the frame so that it can be displayed in the gui

    '''Makes the buttons at the bottom of the frame for the user to click on'''
    def makeButtons(self):
        buttonFrame = ttk.Frame(self) # sets the button frame

        buttonFrame.grid(column = 0, row = 4, columnspan = 2, sticky = tk.E) # sets the grid of the buttons inside the button frame

        # Makes a button that calls the calculate function when clicked
        ttk.Button(buttonFrame, text = "Calculate", command = self.calculate).grid(column = 0, row = 0, padx = 5)
        # Makes a button that calls the parent.destroy command which exits the gui and exits the program
        ttk.Button(buttonFrame, text = "Exit", command = self.parent.destroy).grid(column = 1, row = 0,)

    '''Calculates the circumference from the radius and displays an error if the wrong value type is entered'''
    def calculate(self):
        try:
            radius = float(self.radius.get()) # Sets the variable radius to the inputted value from the gui
            circumference = radius * math.pi * 2 # Calculates the circumference from the radius
            self.circ.set(round(circumference, 4)) # Puts the calculated circumference into the circ variable
            # so that it displays the result in the read only entry box
        except ValueError:
            self.message += f"Radius needs to be a number.\n" # Displays this message box if there's a value type error

        if self.message != "": # If the message isn't an empty string, it will display an error message
            messagebox.showerror("Error:", self.message)




if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # creates the root
    root.title("Circle Circumference Calculator") # sets the root title of the gui window
    CircValueFrame(root) # calls the CircValueFrame class and passes in root
    root.mainloop() # starts the gui loop
