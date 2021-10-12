#!/usr/bin/env python3

print("Peter Sanford's Miles Per Gallon application") # Prints a welcome message
print() # Adds a blank line

another_trip = "y" # Sets another trip to y so that the while loop will start

# Creates a while loop so that the user can repeat if they put in a y
while another_trip.lower() == "y": # Sets up the while loop to continue until user inputs an n
    miles_driven = float(input("Enter miles driven:         ")) # Gets the users miles driven
    gallons_used = float(input("Enter gallons of gas used:  ")) # Gets the users gallons used
    cost_per_gallon = float(input("Enter cost per gallon:   ")) # Gets the cost per gallon from user

    if miles_driven <= 0: # sets up the if statement so that the inputs are valid
        print("Miles driven must be greater than zero. Please try again.") # tells the user if the input is invalid
    elif gallons_used <= 0: # sets up the if statement so that the inputs are valid
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0: # sets up the if statement so that the inputs are valid
        print("Cost per gallon must be greater than zero. Please try again.")
    else: # If the inputs are valid, then it continues
        mpg = round((miles_driven / gallons_used), 2) # Calculates the miles per gallon
        total_gas_cost = round((cost_per_gallon * gallons_used), 1) # Calculates the total gas cost
        cost_per_mile = round((total_gas_cost / miles_driven), 1) # Calculates the cost per mile
        
        print() # Adds a blank line
        print(f"Miles Per Gallon:\t{mpg}") # Prints the miles per gallon
        print(f"Total Gas Cost::\t{total_gas_cost}") # prints the total gas cost
        print(f"Cost Per Mile:\t\t{cost_per_mile}") # prints the cost per mile
        print() # Adds a blank line
        
    another_trip = input("Get entries for another trip? (y/n): ") # gets input for if the user wants to continue

print() # Adds a blank line
print("Bye") # Salutation message



