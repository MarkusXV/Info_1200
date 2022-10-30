#!/usr/bin/env python3

import csv

'''
3. Create an If elif elif else statement
4. Read a .csv or .txt file
5. Write to a .csv or .txt file
6. For loop and print all items inside the loop
7. List that holds a 2d list
'''


'''Prints the menu for the commands that the user can enter'''
def print_menu():
    print("Command Menu:\n"
          "view\t= Views Total To-Do List\n"
          "add\t= Adds a New To-Do Entry\n"
          "delete\t= Deletes a To-Do Entry\n"
          "exit\t= Exits the program\n") # Commands are view, add, delete, and exit

'''Reads the csv file and returns a list'''
def read_to_do():
    lto_do = [] # Local empty list to put the values into
    try: # tries to read csv file, with a possible file not found error
        with open("To_Do_List.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    lto_do.append(row) # puts each row into the list, making a two dimensional list
                return lto_do # returns the list back to the function
    except FileNotFoundError:
        return lto_do # If there isn't a csv file, return the empty list (file will be created when the write_to_do function is called)

'''Writes the to_do list to the csv file'''
def write_to_do(to_do):
    with open("To_Do_List.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(to_do)

'''Adds an item to the to_do list'''
def add_to_do(to_do):
    lto_do = [] # local empty list

    # Gets the values for the new items that the user wants to add
    name = input("\nWhat Needs to Get Done?\t")
    date = input("When is the Deadline to Get this Done?\t")

    # Adds the two values to the local list
    lto_do.append(name)
    lto_do.append(date)

    # Adds the local list to the passed to_do list
    to_do.append(lto_do)

    write_to_do(to_do) # calls the write function so that the csv file adds the new item
    view_all_to_do(to_do) # calls the view function so that the user knows it was added
    print_menu() # Prints the menu again to remind the user of the command options

'''Deletes an item from the to_do list'''
def delete_to_do(to_do):
    while True: # Creates a while loop that checks values and logic
        try: # Gets the value from the user, with a possible value error
            number = int(input("\nWhich # of the To-Do Entries do you want to delete? "))
        except ValueError: # If there's a value error, print the error and continue to the next iteration of the loop to task for another number
            print("\nPlease input a number")
            continue
        
        if number > 0 and number <= len(to_do): # Checks to see if the number is a valid item in the list
            to_do.pop(number - 1)
            break
        else: # If the number is invalid, print invalid number and continue to the next iteration of the loop to ask for another number
            print("\nInvalid Number")
            continue

    write_to_do(to_do) # calls the write function so that the csv file adds the new item
    view_all_to_do(to_do) # calls the view function so that the user knows it was added
    print_menu() # Prints the menu again to remind the user of the command options

'''Vies all of the items in the to_do list'''
def view_all_to_do(to_do):
    if len(to_do) != 0: # Only prints the to do list if there's something in it
        print("\n\tTo Do\t|   Due Date\n") # Prints header for list

        counter = 1 # Counter for the item number
        for row in to_do: # For every row, print the items with the item number
            print(f"{counter}. {row[0]}  |  {row[1]}")
            counter += 1 # Adds one to counter after each row
        print() # Prints a blank line after all items are printed
    else: 
        print("\n\tNothing in To Do List Currently\n") # if there's nothing in the to do list, print Nothing in To Do List

'''Main function that calls all other functions'''
def main():
    to_do = read_to_do() # Reads the csv file and puts the list into the to_do variable, making it a list
    view_all_to_do(to_do) # Prints all the items in the to_do list just created
    print_menu() # Prints the menu of commands
    
    while True: # Gets the command from the user and calls the corresponding function
        command = input("Command: ")
        if command.lower() == "view":
            view_all_to_do(to_do)
            print_menu()
        elif command.lower() == "add":
            add_to_do(to_do)
        elif command.lower() == "delete":
            if len(to_do) != 0: # Only calls the delete_to_do function if there's something to delete
                delete_to_do(to_do)
            else: # prints that there's nothing to delete and continues the loop to get a new command
                print("\n\tNothing in To Do List to Delete\n")
                print_menu()
                continue
        elif command.lower() == "exit":
            break # breaks if exit is inputted
        else: 
            print("\nNot a valid command. Please try again.\n") # If it doesn't match any of these, prints that it's not a valid command



if __name__ == "__main__": # if this is the main module, run the main function
    main()
