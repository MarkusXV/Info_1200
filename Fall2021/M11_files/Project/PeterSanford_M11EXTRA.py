#!usr/bin/env/python3

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
        self.parent = parent # sets the parent to the self parent so that each instance knows the parent
        self.message = "" # sets the message to an empty string so that we can use it later

        self.contacts = self.read_contacts()

        self.contact_name_a = tk.StringVar()
        self.contact_email_a = tk.StringVar()
        self.contact_phone_a = tk.StringVar()

        self.contact_num_v = tk.StringVar()
        self.contact_num_e = tk.StringVar()

        self.contact_num_d = tk.StringVar()
        


        self.initComponents(root) # Each instance runs the initComponents function to set up the grid

    '''Display the grid of labels, buttons, and text entry fields'''
    def initComponents(self, parent):
        self.parent = parent
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
        ttk.Entry(self, width = 34, textvariable = self.contact_name_a).grid(column = 1, row = 4, pady = 3, sticky = tk.W)
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

        self.view_all_contacts()

    
    def read_contacts(self):
        lcontacts = []
        with open("contacts.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                lcontacts.append(row)
        return lcontacts

    def write_contacts(self):
        with open("contacts.csv", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(self.contacts)
        

    def view_all_contacts(self):
        # Resets the text box to empty
        self.contacts_output.delete("1.0", END)

        counter = 1
        self.contacts_output.insert(tk.END, "        Name\t\t  |       Email\t\t    |      Phone Number\n\n")
        for row in self.contacts:
            
            self.contacts_output.insert(tk.END, f" {counter} - {row[0]} | {row[1]} | {row[2]}\n"
                                     " ---------------------------------------------------------\n")
            counter += 1

    def view_single_contact(self):
        # Resets the text box to empty
        self.contacts_output.delete("1.0", END)

        try:
            input_num = int(self.contact_num_v.get())
        except ValueError:
            self.message += f"Please Enter a Number"
            self.display_message()

        if input_num > 0 and input_num <= len(self.contacts):
            self.contacts_output.insert(tk.END, "        Name\t\t  |       Email\t\t    |      Phone Number\n\n")
            
            selected_contact = self.contacts[input_num - 1]

            self.contacts_output.insert(tk.END, f" {input_num} - {selected_contact[0]} | {selected_contact[1]} | {selected_contact[2]}\n")

            self.contact_num_v.set("")

    def add_contact(self):
        self.contacts_output.delete("1.0", END)

        try:
            inputted_name = str(self.contact_name_a.get())
            inputted_email = str(self.contact_email_a.get())
            inputted_phone = str(self.contact_phone_a.get())
        except ValueError:
            print("error")


        lcontact = []
        lcontact.append(inputted_name)
        lcontact.append(inputted_email)
        lcontact.append(inputted_phone)
        self.contacts.append(lcontact)

        self.view_all_contacts()

        self.write_contacts()

        self.contact_name_a.set("")
        self.contact_email_a.set("")
        self.contact_phone_a.set("")

    def delete_contact(self):
        self.contacts_output.delete("1.0", END)

        try:
            inputted_number = int(self.contact_num_d.get())
        except ValueError:
            print("error")

        if inputted_number > 0 and inputted_number <= len(self.contacts):
            del self.contacts[inputted_number - 1]

            self.view_all_contacts()

            self.write_contacts()

            self.contact_num_d.set("")
        else:
            self.message += f"Invalid number entered."
            display_message()
        
        

    def display_message(self):
        if self.message != "": # If the message isn't an empty string, it will display the error message
            messagebox.showerror("Error:", self.message)
            self.message = "" # Resets the error message back to empty
            

        

        

        

if __name__ == "__main__": # If this is the main module, run this code
    root = tk.Tk() # Creates the root parent frame
    root.title("Contact Manager App") # Sets the root title of the gui window
    Sales(root) # calls the Sales class and passes in the root parent
    root.mainloop() # starts the gui loop to display it

    
    
    



            
