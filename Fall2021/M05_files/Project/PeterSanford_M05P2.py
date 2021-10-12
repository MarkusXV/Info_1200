#!usr/bin/env python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date:  10/9/21
#Project #: MO5_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import psconverter as c  # imports the psconverter file and names it c

'''
Function that displays a welcome message with no parameters
'''
def fm_welcome():
    print("Peter Sanford's Feet and Meters Converter") # Prints a welcome message
    print() # Adds a blank line

'''
Function that displays a conversion menu with no parameters
'''
def fm_menu(): # Sets function named fm_menu
    print("Conversions Menu:\n\na. Feet to Meters\nb. Meters to Feet") # prints the conversion menu

'''
Function that utilizes all other functions, included imported modules
'''
def main(): # Sets function named main
    fm_welcome() # calls the fm_welcome function
    while True: # Sets up an infinite while loop that continues until break
        fm_menu() # calls the fm_menu function
        choice = input("Select a conversion (a/b): ") # Creates a variable named choice that gets the user's input which conversion they want
        print() # Adds a blank line
        if choice.lower() == "a": # Sets up an if statement that checks what the user's desired conversion is
            feet = int(input("Enter feet: ")) # creates new variable named feet that gets the user's number of feet that they want coverted
            meters = c.to_meters(feet) # calls the to_meters function that's imported and puts it in a variable named meters
            print(round(meters, 2), "meters") # prints the converted meters and rounds it to two decimal places
        elif choice.lower() == "b": # Sets up an if statement that checks what the user's desired conversion is
            meters = int(input("Enter meters: ")) # creates new variable named meters that gets the user's number of meters that they want coverted
            feet = c.to_feet(meters) # calls the to_feet function that's imported and puts it in a variable named feet
            print(round(feet, 2), "feet") # prints the converted feet and rounds it to two decimal places
        else:
            print("You didn't enter a valid selection") # if they didn't input a correct value, it will display that it wasn't a valid selection

        print() # Adds a blank line
        more = input("Would you like to perform another conversion? (y/n): ") # sets a variable named more with the user's input whether they would like to continue or not
        print() # Adds a blank line
        if more.lower() != "y": # if the user puts in anything other than a y, this if statement will run
            print("Thanks, bye!") # Prints a bye message
            break # breaks the infinite while loop if they said they wouldn't like to continue


if __name__ == "__main__": # runs the main function if this file is run directly (no functions called if this file is imported)
    main()


