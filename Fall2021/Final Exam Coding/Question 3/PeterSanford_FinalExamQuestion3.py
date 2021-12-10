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

        '''Sets up the variables that will work with the gui'''
        # Variables for dividing
        self.div_fir = tk.StringVar()
        self.div_sec = tk.StringVar()

        # Variables for multiplying
        self.mult_fir = tk.StringVar()
        self.mult_sec = tk.StringVar()

        # Variables for subtracting
        self.sub_fir = tk.StringVar()
        self.sub_sec = tk.StringVar()

        # Variables for adding
        self.add_fir = tk.StringVar()
        self.add_sec = tk.StringVar()

        self.expression = ""
        

        self.initComponents(root) # Runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self, parent):
        self.parent = parent # sets the parent to the self parent so that this function knows the parent
        
        # Creates the Frame for the text box
        textFrame = ttk.Frame(self)
        textFrame.grid(column = 0, row = 1, columnspan = 5, pady = 5)

        calcFrame = ttk.Frame(self)
        calcFrame.grid(column = 0, row = 3, columnspan = 5, pady = 15)
        
        
        # Title
        ttk.Label(self, text = "Calculator").grid(column = 0, row = 0, columnspan = 5, pady = 5, sticky = tk.N)
        # Row 2 - Text Box
        self.number_output = scrolledtext.ScrolledText(textFrame, height = 5, width = 35, state = "normal")
        self.number_output.grid(column = 0, row = 0, sticky = tk.W, padx = (17, 0))

        # Row 3 - Clear
        ttk.Button(calcFrame, text = "Clear", command = self.clear_output, width = 7).grid(column = 3, row = 0, pady = 3, padx = 3)

        # Row 4 - (1, 2, 3, +)
        ttk.Button(calcFrame, text = "1", command = lambda: self.press(1), width = 7).grid(column = 0, row = 1, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "2", command = lambda: self.press(2), width = 7).grid(column = 1, row = 1, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "3", command = lambda: self.press(3), width = 7).grid(column = 2, row = 1, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "+", command = lambda: self.press(" + "), width = 7).grid(column = 3, row = 1, pady = 3, padx = 3)

        # Row 5 - (4, 5, 6, -)
        ttk.Button(calcFrame, text = "4", command = lambda: self.press(4), width = 7).grid(column = 0, row = 2, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "5", command = lambda: self.press(5), width = 7).grid(column = 1, row = 2, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "6", command = lambda: self.press(6), width = 7).grid(column = 2, row = 2, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "-", command = lambda: self.press(" - "), width = 7).grid(column = 3, row = 2, pady = 3, padx = 3)

        # Row 6 - (7, 8, 9, *)
        ttk.Button(calcFrame, text = "7", command = lambda: self.press(7), width = 7).grid(column = 0, row = 3, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "8", command = lambda: self.press(8), width = 7).grid(column = 1, row = 3, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "9", command = lambda: self.press(9), width = 7).grid(column = 2, row = 3, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "*", command = lambda: self.press(" * "), width = 7).grid(column = 3, row = 3, pady = 3, padx = 3)

        # Row 7 - (0, Clear, =, /)
        ttk.Button(calcFrame, text = "0", command = lambda: self.press(0), width = 7).grid(column = 0, row = 4, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = ".", command = lambda: self.press("."), width = 7).grid(column = 1, row = 4, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "=", command = self.equals, width = 7).grid(column = 2, row = 4, pady = 3, padx = 3)
        ttk.Button(calcFrame, text = "/", command = lambda: self.press(" / "), width = 7).grid(column = 3, row = 4, pady = 3, padx = 3)
        
        
                
        self.pack() # packs the frame so that it can be displayed in the gui

    def clear_output(self):
        self.expression = ""
        self.number_output.delete("1.0", END)
        self.number_output.insert(tk.END, self.expression)

    def press(self, number):
        self.expression += str(number)

        self.number_output.delete("1.0", END)
        self.number_output.insert(tk.END, self.expression)

    def equals(self):
        try:
            total = str(eval(self.expression))

            if len(self.expression) >= 25:
                self.number_output.insert(tk.END, f"\n = {total}")
            else:
                self.number_output.insert(tk.END, f" = {total}")

            self.expression = ""
        except:
            self.message += "Can't Calculate"
            self.display_message()
            
            self.expression = ""
        

        
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



    
