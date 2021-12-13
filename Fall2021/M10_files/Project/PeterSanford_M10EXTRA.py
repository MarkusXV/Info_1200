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
from tkinter import *
from tkinter import ttk, messagebox
import csv

'''Sets up the class called Sales'''
class Sales(ttk.Frame, tk.Text):
    '''Defines the init function to initalize the variables needed in the instances'''
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding = "20 0 20 20") # initalizes the initial frame for the gui
        self.parent = parent # sets the parent to the self parent so that each instance knows the parent
        self.message = "" # sets the message to an empty string so that we can use it later

        # Calls the read sales function and puts it into a variable called sales that has the list of all sales
        self.read_sales()

        # Sets up the variables that will work with the Gui entries
        self.month_input = tk.StringVar()
        self.sales_input = tk.StringVar()


        
        
        self.initComponents(root) # Each instance runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self, parent):
        self.parent = parent # sets parent equal to self.parent so that parent is known in this function
        # Creates the Frame for the text box
        textFrame = ttk.Frame(self)
        textFrame.grid(column = 0, row = 1, columnspan = 2, sticky = tk.E)
        # Creates the frame for the side buttons
        buttonFrame1 = ttk.Frame(self)
        buttonFrame1.grid(column = 2, row = 1, sticky = tk.N)
        
        
        # Title
        ttk.Label(self, text = "Monthly Sales").grid(column = 0, row = 0, columnspan = 3, pady = 20, sticky = tk.N)
        # Text Box
        self.sales_output = tk.Text(textFrame, height = 13, width = 30, state = "normal")
        self.sales_output.grid(column = 0, row = 0, sticky = tk.E)
        # Side buttons
        ttk.Button(buttonFrame1, text = "View Monthly Sales", command = self.view_monthly_sales).grid(column = 0, row = 1, sticky = tk.W, padx = 5, pady = 3)
        ttk.Button(buttonFrame1, text = "View Yearly Summary", command = self.view_yearly_summary).grid(column = 0, row = 2, sticky = tk.W, padx = 5, pady = 3)
        
        # Row 3
        ttk.Label(self, text = "Edit a Month's Sales").grid(column = 0, row = 2, columnspan = 3, pady = 12, sticky = tk.S)

        # Row 4
        ttk.Label(self, text = "Enter 3 letter month:").grid(column = 0, row = 3, sticky = tk.E, padx = 5)
        ttk.Entry(self, width = 40, textvariable = self.month_input).grid(column = 1, row = 3)
        ttk.Button(self, text = "Edit", command = self.edit_sales).grid(column = 2, row = 3, sticky = tk.E, padx = 5, pady = 1)

        # Row 5
        ttk.Label(self, text = "New Sales for that Month:").grid(column = 0, row = 4, sticky = tk.E, padx = 5)
        ttk.Entry(self, width = 40, textvariable = self.sales_input).grid(column = 1, row = 4)
        ttk.Button(self, text = "Exit", command = self.parent.destroy).grid(column = 2, row = 4, sticky = tk.E, padx = 5, pady = 1)


        self.pack() # packs the frame so that it can be displayed in the gui

        self.view_monthly_sales() # calls the view monthly sales function so that the text box is showing all contacts on startup


    '''Reads the csv file and puts the contents into the sales list'''
    def read_sales(self):
        self.sales = [] # Creates an empty list so the reader can put the contents in it
        with open("monthly_sales.csv", newline="") as file: # Reads the csv file
            reader = csv.reader(file)
            for row in reader:
                self.sales.append(row) # For every row, it will put it into the list, making it a two-dimensional list
        return self.sales

    '''Writes the self.sales list to the csv file'''
    def write_sales(self):
        with open("monthly_sales.csv", "w", newline = "") as file: # Opens the file and writes the list to it
            writer = csv.writer(file)
            writer.writerows(self.sales)
        
    '''Views the contents of the self.sales list in a readable format'''
    def view_monthly_sales(self):
        # Resets the text box to empty
        self.sales_output.delete("1.0", END)
        
        for row in self.sales:
            row[1] = round(float(row[1]), 2)
            self.sales_output.insert(tk.END, f"{row[0]} - ${row[1]}\n") # for every row, prints it in a good format

    '''Views the yearly summary'''
    def view_yearly_summary(self):
        # Resets the text box to empty
        self.sales_output.delete("1.0", END)
        
        total = 0 # Creates total variable to be used later
        for row in self.sales: # for every row, we're going to add up each sales amount in the self.sales list
            amount = float(row[1])
            total += amount

        count = len(self.sales) # Gets the count (Always 12)
        
        # Calculate average
        average = total / count
        average = round(average, 2)
        average = f"${average}" # puts it in currency
        
        total = round(total, 2)
        total = f"${total}" # puts it in currency

        self.sales_output.insert(tk.END, f"Yearly total:\t{total}\nMonthly average:\t{average}") # outputs the results to the text box

    '''Edits the sales amount for a certain month'''
    def edit_sales(self):
        avail_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # creates a list of selectable months

        # Gets the values from the GUI and Checks if they're valid data types
        try:
            inputted_month = str(self.month_input.get())
            inputted_month = inputted_month.title() # Capitalizes the inputted month's first character
            inputted_sales = float(self.sales_input.get())

            # checks if the month is invalid and prints error if invald
            selected_month = ""
            for month in avail_months:
                if inputted_month == month:
                    selected_month = month

            if selected_month == "":
                self.message += f"Invalid three-letter month.\n"
                self.display_message()
            
        except ValueError: 
            self.message += f"Invalid Month or Sales. Put in a Three Letter Month and then a Number for Sales."
            self.display_message()

        # gets the index of the month they selected so we can change the sales value of it
        index = avail_months.index(selected_month)

        # Changes the sales value of the month they selected to the sales the user inputted
        self.sales[index][1] = inputted_sales

        # Resets the text box to show the new change
        self.view_monthly_sales()

        # Resets the entry boxes once the edit has been completed
        self.month_input.set("")
        self.sales_input.set("")

        # Calls the write sales function so the new change is updated to the csv file
        self.write_sales()

    '''Displays the error when called'''
    def display_message(self):
        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message back to empty
            

        

        

        

if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Monthly Sales") # Sets the root title of the gui window
    Sales(root) # calls the Sales class and passes in the root parent
    root.mainloop() # starts the gui loop to display it

    
    
    



            
