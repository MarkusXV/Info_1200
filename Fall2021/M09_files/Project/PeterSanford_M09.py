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

        # Sets up the variables that will work with the Gui entries
        self.grab = tk.StringVar() 
        self.drop = tk.StringVar() 
        self.edit_index = tk.StringVar() 
        self.edit_name = tk.StringVar() 

        self.item1 = tk.StringVar()
        self.item2 = tk.StringVar()
        self.item3 = tk.StringVar()
        self.item4 = tk.StringVar()

        #Starting inventory
        self.inventory = ["Wand", "Spellbook", "Candle"]
        self.item1.set(self.inventory[0])
        self.item2.set(self.inventory[1])
        self.item3.set(self.inventory[2])
        
        self.initComponents() # Each instance runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self):
        # Creates the button frame for the third column for the inventory commands
        buttonFrame1 = ttk.Frame(self)
        buttonFrame1.grid(column = 2, row = 1, rowspan = 3, sticky = tk.S)

        # Row 1
        ttk.Label(self, text = "You can only hold 4 items at a time").grid(column = 0, row = 0, columnspan = 3, pady = 3)
        # Row 2
        ttk.Label(self, text = "Grab new item called: ").grid(column = 0, row = 1, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 25, textvariable = self.grab).grid(column = 1, row = 1, sticky = tk.W, pady = 3)
        ttk.Button(buttonFrame1, text = "Grab", command = self.grab_item).grid(column = 2, row = 1, padx = 5, pady = 1)
        # Row 3
        ttk.Label(self, text = "Drop item #: ").grid(column = 0, row = 2, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 5, textvariable = self.drop).grid(column = 1, row = 2, sticky = tk.W, pady = 3)
        ttk.Button(buttonFrame1, text = "Drop", command = self.drop_item).grid(column = 2, row = 2, padx = 5, pady = 1)
        # Row 4
        ttk.Label(self, text = "Edit item # and New Name: ").grid(column = 0, row = 3, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 5, textvariable = self.edit_index).grid(column = 1, row = 3, sticky = tk.W, pady = 3)
        ttk.Entry(self, width = 18, textvariable = self.edit_name).grid(column = 1, row = 3, sticky = tk.E, pady = 3)
        ttk.Button(buttonFrame1, text = "Edit", command = self.edit_item).grid(column = 2, row = 3, padx = 5, pady = 1)
        # Row 5
        ttk.Label(self, text = "Item 1: ").grid(column = 0, row = 4, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 25, textvariable = self.item1, state = "readonly").grid(column = 1, row = 4, sticky = tk.W)
        # Row 6
        ttk.Label(self, text = "Item 2: ").grid(column = 0, row = 5, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 25, textvariable = self.item2, state = "readonly").grid(column = 1, row = 5, sticky = tk.W)
        # Row 7
        ttk.Label(self, text = "Item 3: ").grid(column = 0, row = 6, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 25, textvariable = self.item3, state = "readonly").grid(column = 1, row = 6, sticky = tk.W)
        # Row 8
        ttk.Label(self, text = "Item 4: ").grid(column = 0, row = 7, sticky = tk.E, pady = 3)
        ttk.Entry(self, width = 25, textvariable = self.item4, state = "readonly").grid(column = 1, row = 7, sticky = tk.W)
        
        
        self.makeButtons() # Runs the makeButtons function to make the buttons at the bottom of the gui frame
        self.pack() # packs the frame so that it can be displayed in the gui

    '''Makes the buttons at the bottom of the frame for the user to click on'''
    def makeButtons(self):
        buttonFrame2 = ttk.Frame(self) # sets the button frame

        # Sets the grid of the buttons inside the button frame
        buttonFrame2.grid(column = 0, row = 8, columnspan = 2, sticky = tk.E) 
        
        # Makes a button that calls the parent.destroy command which exits the gui and exits the program
        ttk.Button(buttonFrame2, text = "Exit", command = self.parent.destroy).grid(column = 0, row = 0)

    
    '''Updates the gui values according to the list so that the values displayed in the gui matches the items in the list'''
    def list_update(self):
        # 1 item in inventory
        if len(self.inventory) >= 1:
            self.item1.set(self.inventory[0])
        else:
            self.item1.set("")
            
        # 2 items in inventory
        if len(self.inventory) >= 2:
            self.item2.set(self.inventory[1])
        else:
            self.item2.set("")
            
        # 3 items in inventory    
        if len(self.inventory) >= 3:
            self.item3.set(self.inventory[2])
        else:
            self.item3.set("")
            
        # 4 items in inventory
        if len(self.inventory) == 4:
            self.item4.set(self.inventory[3])
        else:
            self.item4.set("")
        

    def grab_item(self):
        # Tries to set the value inputted to the GUI and checks for a value error
        try:
            item_name = str(self.grab.get()) # Sets the variable item_name to the inputted value from the gui
        except ValueError:
            self.message += f"Item name can't be a number.\n" # Displays this message box if there's a value type error

        # If the message isn't an empty string, it will display the error message
        if self.message != "": 
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message

        # Checks to see if there's an available spot in the inventory for them to add an item
        if len(self.inventory) <= 4:
            self.inventory.append(item_name) # Adds the item they want to the next available item in the list
            self.list_update() # Updates the displayed list so it's correct
        else:
            self.message += "You can't carry any more items. Drop something first.\n" # Displays this message box if the inventory is full

        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message

        # Resets the fields where they input the value so that it's blank for another command
        self.grab.set("")
            

    def edit_item(self):
        # Tries to set the value inputted to the GUI and checks for a value error
        try:
            edit_number = int(self.edit_index.get()) # Sets the variable edit_number to the inputted value from the gui
            edit_name = str(self.edit_name.get()) # Sets the variable edit_name to the inputted value from the gui
        except ValueError:
            self.message += "Item number needs to be a number.\n" # Displays this message box if there's a value type error

        # If the message isn't an empty string, it will display the error message
        if self.message != "": 
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message

        # Checks to see if the number they put in is valid
        if edit_number >= 1 and edit_number <= len(self.inventory):
            self.inventory[edit_number - 1] = edit_name # changes the item that's displayed using the number and name inputted in the gui
            self.list_update() # Updates the displayed list so it's correct
        else:
            if len(self.inventory) != 0:
                self.message += "Incorrect item number entered.\n" # Displays this message box if there's an error
            else:
                self.message += "You don't have an item to edit.\n" # Displays this message box if there's an error

        # If the message isn't an empty string, it will display the error message
        if self.message != "": 
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message

        # Resets the fields where they input the value so that it's blank for another command
        self.edit_index.set("")
        self.edit_name.set("")
            

    def drop_item(self):
        # Tries to set the value inputted to the GUI and checks for a value error
        try:
            drop_number = int(self.drop.get()) # Sets the variable drop_number to the inputted value from the gui
        except ValueError:
            self.message += "Incorrect item number entered.\n" # Displays this message box if there's a value type error

        # If the message isn't an empty string, it will display the error message
        if self.message != "": 
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message

        # Checks to see if the number they put in is valid
        if drop_number >= 1 and drop_number <= len(self.inventory):
            name_of_item = self.inventory[drop_number - 1] # Gets the name of the item number that they want to drop
            self.inventory.remove(name_of_item) # Drops the item with that name
            self.list_update() # Updates the displayed list so it's correct
        else:
            if len(self.inventory) != 0:
                self.message += "Incorrect item number entered.\n" # Displays this message box if there's an error
            else:
                self.message += "You don't have an item to drop.\n" # Displays this message box if there's an error
                
        # If the message isn't an empty string, it will display the error message
        if self.message != "": 
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message

        self.drop.set("") # Resets the fields where they input the value so that it's blank for another command

            

if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Wizard Inventory") # Sets the root title of the gui window
    Wizard(root) # calls the wizard class and passes in the root parent
    root.mainloop() # starts the gui loop to display it
    



            
