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
        ttk.Frame.__init__(self, parent, padding = "40 10 40 40") # initalizes the initial frame for the gui
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
        

        self.initComponents(root) # Runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self, parent):
        self.parent = parent # sets the parent to the self parent so that this function knows the parent
        
        # Creates the Frame for the text box
        textFrame = ttk.Frame(self)
        textFrame.grid(column = 0, row = 1, columnspan = 5, pady = 5)

        calcFrame = ttk.Frame(self)
        calcFrame.grid(column = 0, row = 4, columnspan = 5, pady = 5)
        
        
        # Title
        ttk.Label(self, text = "Calculator").grid(column = 0, row = 0, columnspan = 5, pady = 5, sticky = tk.N)
        # Row 2 - Text Box
        self.number_output = scrolledtext.ScrolledText(textFrame, height = 5, width = 35, state = "normal")
        self.number_output.grid(column = 0, row = 0, sticky = tk.W, padx = (17, 0))
        # Row 3 - Clear
        ttk.Button(self, text = "Clear", command = self.clear_output, width = 8).grid(column = 4, row = 2, pady = 3, sticky = tk.E)
        
        # Row 4 - Label
        ttk.Label(self, text = "    First Number   |   Second Number").grid(column = 0, row = 3, columnspan = 5, pady = (0,5), sticky = tk.S)

        # Row 5 - Add
        ttk.Label(calcFrame, text = " Add:").grid(column = 0, row = 0, pady = 3, padx = 5, sticky = tk.E)
        ttk.Entry(calcFrame, width = 20, textvariable = self.add_fir).grid(column = 1, row = 0, padx = 5, pady = 3)
        ttk.Label(calcFrame, text = " + ").grid(column = 2, row = 0)
        ttk.Entry(calcFrame, width = 20, textvariable = self.add_sec).grid(column = 3, row = 0, padx = 8, pady = 3)
        ttk.Button(calcFrame, text = " = ", command = self.add_num, width = 8).grid(column = 4, row = 0, pady = 3, sticky = tk.E)

        # Row 6 - Subtract
        ttk.Label(calcFrame, text = " Subtract:").grid(column = 0, row = 1, pady = 3, padx = 5, sticky = tk.E)
        ttk.Entry(calcFrame, width = 20, textvariable = self.sub_fir).grid(column = 1, row = 1, padx = 5, pady = 3)
        ttk.Label(calcFrame, text = " - ").grid(column = 2, row = 1)
        ttk.Entry(calcFrame, width = 20, textvariable = self.sub_sec).grid(column = 3, row = 1, padx = 8, pady = 3)
        ttk.Button(calcFrame, text = " = ", command = self.sub_num, width = 8).grid(column = 4, row = 1, pady = 3, sticky = tk.E)
        
        # Row 7 - Multiply
        ttk.Label(calcFrame, text = " Multiply:").grid(column = 0, row = 2, pady = 3, padx = 5, sticky = tk.E)
        ttk.Entry(calcFrame, width = 20, textvariable = self.mult_fir).grid(column = 1, row = 2, padx = 5, pady = 3)
        ttk.Label(calcFrame, text = " x ").grid(column = 2, row = 2)
        ttk.Entry(calcFrame, width = 20, textvariable = self.mult_sec).grid(column = 3, row = 2, padx = 8, pady = 3)
        ttk.Button(calcFrame, text = " = ", command = self.mult_num, width = 8).grid(column = 4, row = 2, pady = 3, sticky = tk.E)

        # Row 8 - Divide
        ttk.Label(calcFrame, text = " Divide:").grid(column = 0, row = 3, pady = 3, padx = 5, sticky = tk.E)
        ttk.Entry(calcFrame, width = 20, textvariable = self.div_fir).grid(column = 1, row = 3, padx = 5, pady = 3)
        ttk.Label(calcFrame, text = " / ").grid(column = 2, row = 3)
        ttk.Entry(calcFrame, width = 20, textvariable = self.div_sec).grid(column = 3, row = 3, padx = 8, pady = 3)
        ttk.Button(calcFrame, text = " = ", command = self.div_num, width = 8).grid(column = 4, row = 3, pady = 3, sticky = tk.E)

        
        self.pack() # packs the frame so that it can be displayed in the gui

    def clear_output(self):
        self.number_output.delete("1.0", END)

    def add_num(self):
        try:
            first = float(self.add_fir.get())
            second = float(self.add_sec.get())
        except ValueError:
            self.message += f"Please input two numbers."
            self.add_fir.set("")
            self.add_sec.set("")
            self.display_message()

        total = first + second

        self.clear_output()
        if total >= 100000000 or first >= 100000000 or second >= 100000000:
            self.number_output.insert(tk.END, f"{round(first, 2)}\n + \n{round(second, 2)}\n = \n{round(total, 4)}")
        else:
            self.number_output.insert(tk.END, f"{round(first, 2)} + {round(second, 2)} = {round(total, 4)}")

        self.add_fir.set("")
        self.add_sec.set("")
        

    def sub_num(self):
        try:
            first = float(self.sub_fir.get())
            second = float(self.sub_sec.get())
        except ValueError:
            self.message += f"Please input two numbers."
            self.sub_fir.set("")
            self.sub_sec.set("")
            self.display_message()

        difference = first - second

        self.clear_output()
        if difference >= 100000000 or first >= 100000000 or second >= 100000000:
            self.number_output.insert(tk.END, f"{round(first, 2)}\n - \n{round(second, 2)}\n = \n{round(difference, 4)}")
        else:
            self.number_output.insert(tk.END, f"{round(first, 2)} - {round(second, 2)} = {round(difference, 4)}")

        self.sub_fir.set("")
        self.sub_sec.set("")

    def mult_num(self):
        try:
            first = float(self.mult_fir.get())
            second = float(self.mult_sec.get())
        except ValueError:
            self.message += f"Please input two numbers."
            self.mult_fir.set("")
            self.mult_sec.set("")
            self.display_message()

        product = first * second

        self.clear_output()
        if product >= 100000000 or first >= 100000000 or second >= 100000000:
            self.number_output.insert(tk.END, f"{round(first, 2)}\n x \n{round(second, 2)}\n = \n{round(product, 4)}")
        else:
            self.number_output.insert(tk.END, f"{round(first, 2)} x {round(second, 2)} = {round(product, 4)}")

        self.mult_fir.set("")
        self.mult_sec.set("")

    def div_num(self):
        try:
            first = float(self.div_fir.get())
            second = float(self.div_sec.get())
        except ValueError:
            self.message += f"Please input two numbers."
            self.div_fir.set("")
            self.div_sec.set("")
            self.display_message()
            

        quotient = first / second

        self.clear_output()
        if quotient >= 100000000 or first >= 100000000 or second >= 100000000:
            self.number_output.insert(tk.END, f"{round(first, 2)}\n / \n{round(second, 2)}\n = \n{round(quotient, 4)}")
        else:
            self.number_output.insert(tk.END, f"{round(first, 2)} / {round(second, 2)} = {round(quotient, 4)}")

        self.div_fir.set("")
        self.div_sec.set("")

        
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



    
