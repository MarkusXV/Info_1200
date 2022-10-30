#!/usr/bin/env python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 12/11/2021
#Project #: M11
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
class Sales(ttk.Frame, tk.Text):
    '''Defines the init function to initalize the variables needed in the instances'''
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding = "30 8 30 20") # initalizes the initial frame for the gui
        self.parent = parent # sets the parent to the self parent so that this function knows the parent
        self.message = "" # sets the message to an empty string so that we can use it later

        '''Sets up the variables that will store the gui entries'''
        # Variables for adding a contact
        self.contact_name_a = tk.StringVar()
        self.contact_email_a = tk.StringVar()
        self.contact_phone_a = tk.StringVar()

        # Variable for viewing single contact
        self.contact_num_v = tk.StringVar()

        # Variable for deleting a contact
        self.contact_num_d = tk.StringVar()
        


        self.initComponents(root) # Runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self, parent):
        self.parent = parent # sets the parent to the self parent so that this function knows the parent
        
        # Creates the Frame for the text box
        textFrame = ttk.Frame(self)
        textFrame.grid(column = 0, row = 1, columnspan = 3, pady = 10)
        
        
        # Title
        ttk.Label(self, text = "Contact Manager").grid(column = 0, row = 0, columnspan = 3, pady = 10, sticky = tk.N)
        # Row 2 - Text Box
        self.contacts_output = scrolledtext.ScrolledText(textFrame, height = 16, width = 65, state = "normal")
        self.contacts_output.grid(column = 0, row = 0, sticky = tk.W)
        # Row 3 - View All contacts button
        ttk.Button(self, text = "View All Contacts", command = self.view_all_contacts, width = 30).grid(column = 0, row = 2, columnspan = 3, pady = 5)
        
        # Row 4 - Label
        ttk.Label(self, text = "Add a Contact").grid(column = 0, row = 3, columnspan = 3, pady = 12, sticky = tk.S)

        # Row 5
        ttk.Label(self, text = "Name: ").grid(column = 0, row = 4, padx = 5, sticky = tk.E)
        self.name_box = ttk.Entry(self, width = 34, textvariable = self.contact_name_a)
        self.name_box.grid(column = 1, row = 4, pady = 3, sticky = tk.W)
        ttk.Button(self, text = "Add Contact", command = self.add_contact).grid(column = 2, row = 4, rowspan = 4, sticky = tk.NW)

        # Row 6
        ttk.Label(self, text = "Email: ").grid(column = 0, row = 5, padx = 5, sticky = tk.E)
        ttk.Entry(self, width = 34, textvariable = self.contact_email_a).grid(column = 1, row = 5, pady = 3, sticky = tk.W)

        # Row 7
        ttk.Label(self, text = "Phone: ").grid(column = 0, row = 6, padx = 5, sticky = tk.E)
        ttk.Entry(self, width = 34, textvariable = self.contact_phone_a).grid(column = 1, row = 6, pady = 3, sticky = tk.W)

        # Row 8 - Label
        ttk.Label(self, text = "View a single contact").grid(column = 0, row = 7, columnspan = 3, pady = 8, sticky = tk.S)

        # Row 9
        ttk.Label(self, text = "Enter Contact # to View: ").grid(column = 0, row = 8, pady = 3, padx = 5, sticky = tk.E) 
        ttk.Entry(self, width = 12, textvariable = self.contact_num_v).grid(column = 1, row = 8, sticky = tk.W)
        ttk.Button(self, text = "View Single Contact", command = self.view_single_contact).grid(column = 2, row = 8, sticky = tk.W, pady = 3)

        # Row 10 - Label
        ttk.Label(self, text = "Delete a Contact").grid(column = 0, row = 9, columnspan = 3, pady = 8, sticky = tk.S)

        # Row 11
        ttk.Label(self, text = "Enter Contact # to Delete: ").grid(column = 0, row = 10, padx = 5, pady = 3, sticky = tk.E)
        ttk.Entry(self, width = 12, textvariable = self.contact_num_d).grid(column = 1, row = 10, pady = 3, sticky = tk.W)
        ttk.Button(self, text = "Delete Contact", command = self.delete_contact).grid(column = 2, row = 10, pady = 3, sticky = tk.W)

        # Row 12 - Exit Button
        ttk.Button(self, text = "Exit", command = self.parent.destroy).grid(column = 2, row = 11, sticky = tk.W, pady = 10)


        self.pack() # packs the frame so that it can be displayed in the gui

        self.contacts = self.read_contacts() # calls the read_contacts function to get the values from the csv
        self.view_all_contacts() # calls the view_all_contacts function so that they appear at the beginning of running the function

    '''Reads the csv file and puts it into the self.contacts list'''
    def read_contacts(self):
        lcontacts = [] # creates an empty list so that we can put the csv values into it
        try: # try block with statements that can throw exceptions
            with open("contacts.csv", newline="") as file: # Reads the csv file
                reader = csv.reader(file)
                for row in reader:
                    lcontacts.append(row) # For every row, it will put it into the list, making it a two-dimensional list
            return lcontacts
        except FileNotFoundError: # If there's a File not found error:
            self.message += f"Could not find contacts file. Starting new contacts file" # sets the error message
            self.display_message() # Displays the error message
            return lcontacts # returns the empty list so self.contacts becomes an empty list as well

    '''Writes the self.contacts list to the csv file'''
    def write_contacts(self):
        with open("contacts.csv", "w", newline = "") as file: # Opens the file and writes the list to it
            # Creates the file if there isn't one to begin with
            writer = csv.writer(file)
            writer.writerows(self.contacts)

    '''Views all the contacts that are in the self.contacts list'''
    def view_all_contacts(self):
        # Resets the text box to empty
        self.contacts_output.delete("1.0", END)

        counter = 1 # Creates the counter to print which contact it is
        # Outputs the Header to the textbox
        self.contacts_output.insert(tk.END, "        Name\t\t  |       Email\t\t    |      Phone Number\n\n")
        if len(self.contacts) > 0: # if there's something in the list to display:
            for row in self.contacts:
                # Prints each row in self.contacts in a good format
                self.contacts_output.insert(tk.END, f" {counter} - {row[0]} | {row[1]} | {row[2]}\n"
                    " ---------------------------------------------------------\n")
                counter += 1

    '''Views a single contact that the user chooses'''
    def view_single_contact(self):
        try: # try block that has statements that might throw exceptions
            input_num = int(self.contact_num_v.get())
        except ValueError: # if there's a value error:
            self.message += f"Please Enter a Number" # sets the error message
            self.display_message() # Displays the error message

        if input_num > 0 and input_num <= len(self.contacts): # If the inputted number is valid:
            # Resets the text box to empty
            self.contacts_output.delete("1.0", END)
            # Reprints the header to the text box
            self.contacts_output.insert(tk.END, "        Name\t\t  |       Email\t\t    |      Phone Number\n\n")
            # Sets the selected contact to the contact associated with the inputted number
            selected_contact = self.contacts[input_num - 1]
            # Outputs the selected contact to the text box
            self.contacts_output.insert(tk.END, f" {input_num} - {selected_contact[0]} | {selected_contact[1]} | {selected_contact[2]}\n")
            # Resets the entry box
            self.contact_num_v.set("")
        else: # If the inputted number is invalid:
            self.message += f"Invalid Contact Number" # Sets the error message
            self.contact_num_v.set("") # Resets the entry box
            self.display_message() # Displays the error message
            
    '''Adds a contact from name, email, and phone received from the user'''
    def add_contact(self):
        # Resets the text box to empty
        self.contacts_output.delete("1.0", END)

        try: # try block that has statements that might throw exceptions
            inputted_name = str(self.contact_name_a.get())
            inputted_email = str(self.contact_email_a.get())
            inputted_phone = str(self.contact_phone_a.get())
        except ValueError as e: # If there's a value error:
            total_message = str(type(e)) + str(e) # Creates the error message from the error object
            self.message += total_message # puts the error message to the self.message variable
            self.display_message() # Displays the error message


        lcontact = [] # creates a local list so we can add it to the global one
        lcontact.append(inputted_name) # Puts the name in the local list
        lcontact.append(inputted_email) # puts the email in the local list
        lcontact.append(inputted_phone) # puts the phone in the local list
        self.contacts.append(lcontact) # puts the local list into the global list to keep it a two-dimensional list

        self.view_all_contacts() # calls the view_all_contacts variable to show the newly added contact

        self.write_contacts() # Rewrites the global list to the csv file, including the newly added contact

        # Resets the entry boxes
        self.contact_name_a.set("")
        self.contact_email_a.set("")
        self.contact_phone_a.set("")

    '''Deletes a contact from the number the user inputs'''
    def delete_contact(self):
        try: # try block that has statements that might throw exceptions
            inputted_number = int(self.contact_num_d.get())
        except ValueError: # if there's a value error:
            self.message += f"Please enter a number" # creates the error message
            self.display_message() # displays the error message

        if inputted_number > 0 and inputted_number <= len(self.contacts): # If the inputted number is valid
            # Resets the text box
            self.contacts_output.delete("1.0", END)
            # Deletes the selected contact
            del self.contacts[inputted_number - 1]
            
            self.view_all_contacts() # calls the view_all_contacts function to show the deleted contact
            self.write_contacts() # Rewrites the global list to the csv file, including deleting the contact
            self.contact_num_d.set("") # resets the entry box
        else: # if the number is invalid
            self.message += f"Invalid number entered." # Creates the error message
            self.contact_num_d.set("") # resets the entry box
            self.display_message() # Displays the error message
        
    '''Displays the error message in self.message'''
    def display_message(self):
        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.name_box.focus_force() # focuses the text entry boxes because the error box sometimes cause the entry boxes to freeze
            self.message = "" # Resets the error message back to empty
            

        

        

        

if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Contact Manager App") # Sets the root title of the gui window
    Sales(root) # calls the Sales class and passes in the root parent
    root.mainloop() # starts the gui loop to display it

    
    
    



            
