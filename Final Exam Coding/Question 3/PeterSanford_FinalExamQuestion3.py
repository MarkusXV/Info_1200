#!/usr/bin/env python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 12/7/2021
#Project #: Final Project Question 3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

'''Import all of the GUI modules'''
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import scrolledtext
import csv

'''Sets up the class called Sales'''
class Calculator(ttk.Frame, tk.Text):
    '''Defines the init function to initalize the variables needed in the instances'''
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding = "40 10 40 30") # initalizes the initial frame for the gui
        self.parent = parent # sets the parent to the self parent so that this function knows the parent
        self.message = "" # sets the message to an empty string so that we can use it later

        self.expression = "" # variable that will hold the numbers inputted that we will calculate and output the answer
        
        self.initComponents(root) # Runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self, parent):
        self.parent = parent # sets the parent to the self parent so that this function knows the parent
        
        # Creates the Frame for the text box
        textFrame = ttk.Frame(self)
        textFrame.grid(column = 0, row = 1, columnspan = 5, pady = 5)

        # Creates the Frame for the number buttons
        calcFrame = ttk.Frame(self)
        calcFrame.grid(column = 0, row = 3, columnspan = 5, pady = 15)
        
        
        # Title
        ttk.Label(self, text = "Calculator").grid(column = 0, row = 0, columnspan = 5, pady = 5, sticky = tk.N)
        # Row 2 - Text Box
        self.number_output = scrolledtext.ScrolledText(textFrame, height = 5, width = 30, state = "normal")
        self.number_output.grid(column = 0, row = 0, sticky = tk.W, padx = (17, 0))

        # Row 3 - Clear
        ttk.Button(calcFrame, text = "Clear", command = self.clear_output, width = 8).grid(column = 3, row = 0, pady = 3, padx = 3, ipady = 2)

        # Row 4 - (1, 2, 3, +)
        ttk.Button(calcFrame, text = "1", command = lambda: self.press(1), width = 8).grid(column = 0, row = 1, ipady = 4) #lambda lets us pass the 1 argument into the self.press function
        ttk.Button(calcFrame, text = "2", command = lambda: self.press(2), width = 8).grid(column = 1, row = 1, ipady = 4)
        ttk.Button(calcFrame, text = "3", command = lambda: self.press(3), width = 8).grid(column = 2, row = 1, ipady = 4)
        ttk.Button(calcFrame, text = "+", command = lambda: self.press(" + "), width = 8).grid(column = 3, row = 1, ipady = 4)

        # Row 5 - (4, 5, 6, -)
        ttk.Button(calcFrame, text = "4", command = lambda: self.press(4), width = 8).grid(column = 0, row = 2, ipady = 4)
        ttk.Button(calcFrame, text = "5", command = lambda: self.press(5), width = 8).grid(column = 1, row = 2, ipady = 4)
        ttk.Button(calcFrame, text = "6", command = lambda: self.press(6), width = 8).grid(column = 2, row = 2, ipady = 4)
        ttk.Button(calcFrame, text = "-", command = lambda: self.press(" - "), width = 8).grid(column = 3, row = 2, ipady = 4)

        # Row 6 - (7, 8, 9, *)
        ttk.Button(calcFrame, text = "7", command = lambda: self.press(7), width = 8).grid(column = 0, row = 3, ipady = 4)
        ttk.Button(calcFrame, text = "8", command = lambda: self.press(8), width = 8).grid(column = 1, row = 3, ipady = 4)
        ttk.Button(calcFrame, text = "9", command = lambda: self.press(9), width = 8).grid(column = 2, row = 3, ipady = 4)
        ttk.Button(calcFrame, text = "*", command = lambda: self.press(" * "), width = 8).grid(column = 3, row = 3, ipady = 4)

        # Row 7 - (0, Clear, =, /)
        ttk.Button(calcFrame, text = "0", command = lambda: self.press(0), width = 8).grid(column = 0, row = 4, ipady = 4)
        ttk.Button(calcFrame, text = ".", command = lambda: self.press("."), width = 8).grid(column = 1, row = 4, ipady = 4)
        ttk.Button(calcFrame, text = "=", command = self.equals, width = 8).grid(column = 2, row = 4, ipady = 4)
        ttk.Button(calcFrame, text = "/", command = lambda: self.press(" / "), width = 8).grid(column = 3, row = 4, ipady = 4)
                
        self.pack() # packs the frame so that it can be displayed in the gui
        

    '''Clears the text box output and the stored expression'''
    def clear_output(self):
        self.expression = "" # Sets the expression to empty
        self.number_output.delete("1.0", END) # Clears the text box output
        self.number_output.insert(tk.END, self.expression) # Prints the empty expression just to make sure they're the same

    '''Puts the pressed button into the expression variable'''
    def press(self, number):
        self.expression += str(number) # Adds the inputted number as a string to the expression variable

        self.number_output.delete("1.0", END) # Clears the text box
        self.number_output.insert(tk.END, self.expression) # outputs the new expression so that the user can see the number they just pressed

    '''Takes the expression variable, calculates it, and outputs the answer'''
    def equals(self):
        try: # Tries to evaluate the expression as a string, with a possible can't evaluate error
            total = str(eval(self.expression))

            if len(self.expression) >= 20: # if the expression has more than 20 characters, it outputs the answer on seperate lines
                self.number_output.insert(tk.END, f"\n = {total}")
            else: # if the expression is less than 20 characters, it puts the answer in the same line
                self.number_output.insert(tk.END, f" = {total}")

            self.expression = "" # resets the expression after it's done calculating
        except: # If it can't calculate:
            self.message += "Can't Calculate" # put can't calculate into the error message
            self.display_message() # outputs the error message
            
            self.expression = "" # Resets the expression, since it couldn't calculate it
        
    '''Displays the error message in self.message'''
    def display_message(self):
        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message back to empty
            


if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Calculator") # Sets the root title of the gui window
    Calculator(root) # calls the Sales class and passes in the root parent
    root.mainloop() # starts the gui loop to display it



    
