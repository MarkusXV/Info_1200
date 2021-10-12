#!usr/bin/env python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date: 10/9/21
#Project #: MO5_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Peter Sanford's Even or Odd Checker") # Display's welcome message
print() # Adds a blank line

'''
This function checks to see if the inputted number is even or odd
'''
def is_even(num): # Defines the function as is_even and has one parameter
    if (num % 2) == 0: # Sets up an if statement so that if it's divisible by 2 with no remainder, its even
        return True # Returns True if it's divisible by two with no remainder
    else: # if it isn't divisible by two with no remainder (There's a remainder), then it returns false
        return False # If it isn't divisible by two with no remainder, returns false

'''
The main function utilizes all other functions
'''
def main(): # defines the main function which utilizes all other functions
    my_num = int(input("Enter an integer: ")) # creates a variable called my_num which gets an integer input from the user
    print() # Adds a blank line

    if is_even(my_num) == True: # Sets an if statement up which calls the is_even fuction and then checks if it's true or false
        print("This is an even number") # if is_even is true, then it prints it's an even number
    else: # This runs if is_even is false
        print("This is an odd number") # if is_even is false, then it prints it's an odd number
    print() # Adds a blank line
        

if __name__ == "__main__": # This says that this file can be run by itself (main function won't run when imported into another file)
    main() # calls the main fuction if this file is being run directly
