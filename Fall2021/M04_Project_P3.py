#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date: 9/23/2021
#Project #: MO4_P3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Peter Sanford's Change App") # Prints first and last name with title
print() # adds a blank line

choice = "y" # Sets choice to y so that the while loop will initially start

while choice.lower() == "y": # Sets up the while loop to continue until the user types in anything other than a y
    cents = int(input("Enter number of cents (0-99): ")) # Gets the user's input on how many cents they have
    print() # prints a blank line
    
    quarters = cents // 25 # Calculates how many quarters there are
    cents %= 25 # Calculates the cents remaining after the quarters are taken out
    
    dimes = cents // 10 # Calculates how many dimes there are
    cents %= 10 # Calculates the cents remaining after taking out dimes as well
    
    nickels = cents // 5 # Calculates how many nickels there are
    cents %= 5 # Calculates the cents remaining after taking out nickels as well

    pennies = cents # Calculates how many pennies there are at the very end

    print(f"Quarters:\t{quarters}") # Displays how many quarters could be taken out
    print(f"Dimes:\t\t{dimes}") # Displays how many dimes could be taken out
    print(f"Nickels:\t{nickels}") # Displays how many nickels could be taken out
    print(f"Pennies:\t{pennies}") # Displays how many pennies are at the end
    print() # Adds a blank line
    choice = input("Continue? (y/n): ") # Gets the user's input on whether they want to continue or not
    print() # Adds a blank line

print("Bye!") # Salutation after the while loop is concluded
