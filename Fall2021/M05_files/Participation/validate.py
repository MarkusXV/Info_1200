#!/usr/bin/env python3

# Peter Sanford validation file for the Future Value App
'''
Creates a function that checks if the user's input is a valid float value
'''
def get_float(prompt, low, high): # Sets the function name to get_float and has three parameters
    while True: # sets an infinite while loop
        number = float(input(prompt)) # sets number variable to the user's input as a float
        if number > low and number <= high: # checks if the number is in the accepted range of values
            return number # returns the number value if the value is in the accepted range
        else: # sets the else statement
            print("Entry must be greater than", low, "and less than or equal to", high) # prints that there was an error and what the value has to be between
'''
Creates a function that checks if the user's input is a valid integer value
'''
def get_int(prompt, low, high): # Sets the function name to get_int
    while True: # sets an infinite while loop
        number = int(input(prompt)) # sets number variable to the user's input as an integer
        if number > low and number <= high: # checks if the number is in the accepted range of values
            return number # returns the number value if the value is in the accepted range
        else: # sets the else statement
            print("Entry must be greater than", low, "and less than or equal to", high) # prints that there was an error and what the value has to be between
'''
Creates a main function that checks if the above functions are working
Doesn't run when imported into other python files
'''
def main(): # Sets the main funciton to test the above functions
    choice = "y" # sets choice to y so that the while loop will initially run
    while choice.lower() == "y": # as long a choice equals y, the loop will run
        valid_number = get_float("Enter number: ", 0, 1000) # sets the valid_number variable and calls the get_float function with these arguments
        print("Valid number = ", valid_number) # prints the valid_number that was just inputted by the function
        print() # adds a blank line
        valid_integer = get_int("Enter integer: ", 0, 50) # sets the valid_integer variable and calls the get_int function with these arguments
        print("Valid integer = ", valid_integer) # prints the valid_integer that was just inputted by the function
        print() # adds a blank line
        choice = input("Repeat? (y/n): ") # Asks the user if they would like to repeat or not. anything but a y will exit the while loop

    print("Bye!") # prints the exit message


if __name__ == "__main__": # runs the main function if ran inside this file, but not when imported in another file
    main()
