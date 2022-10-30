#!/usr/bin/env python3

print("Welcome to Peter Sanford's Future Value Calculator") # Welcome message
print() # Adds a blank line

choice = "y" # Sets choice to y so the while loop starts
while choice.lower() == "y": # Sets up while loop so that it continues if the user inputs y at the end
    is_valid = False # Sets is_valid to true so that the while loop starts
    while is_valid == False: # Sets up while loop to check if user's input is valid
        monthly_investment = float(input("Enter monthly investment:\t")) # gets user input

        if monthly_investment > 0 and monthly_investment <= 1000: # checks to see if the input is valid
            is_valid = True # if it's valid, then the while loop ends
        else: # if it's invalid, prints it and goes through the loop again
            print("Entry must be greater than 0 and less than or equal to 1000. Please try again.") # Says that the input is invalid
    is_valid = False # sets the variable back to true so that the while loop will start again on the next loop

    while is_valid == False: # Sets up while loop to check if user's input is valid
        yearly_interest_rate = float(input("Enter yearly interest rate:\t")) # Gets user input

        if yearly_interest_rate > 0 and yearly_interest_rate <= 15: # checks to see if the input is valid
            is_valid = True # if it's valid, then the while loop ends
        else: # if it's invalid, prints it and goes through the loop again
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.") # Says that the input is invalid
    is_valid = False # sets the variable back to true so that the while loop will start again on the next loop

    while is_valid == False: # Sets up while loop to check if user's input is valid
        years = int(input("Enter number of years:\t\t")) # Gets user input

        if years > 0 and years <= 50: # checks to see if the input is valid
            is_valid = True # if it's valid, then the while loop ends
        else: # if it's invalid, prints it and goes through the loop again
            print("Entry must be greater than 0 and less than or equal to 50. Please try again.") # Says that the input is invalid
    is_valid = False # sets the variable back to true so that the while loop will start again on the next loop
    print() # Adds a blank line
    
    
    monthly_interest_rate = yearly_interest_rate / 12 / 100 # Converts the monthly interest rate
    months = years * 12 # Converts the years to months

    future_value = 0 # sets the future value to 0 initially
    for i in range(1, months + 1): # Sets up the for loop to continue until the time frame inputted by the user ends
        future_value += monthly_investment # Adds the monthly investment to the future value
        monthly_interest_amount = future_value * monthly_interest_rate # Calculates the interest amount for each month
        future_value += monthly_interest_amount # Adds the interest amount to the future value

        if i % 12 == 0: # Sets up the if statement to print the future value at every year in the investment time frame
            year_number = i // 12 # Gets the year number
            
            print(f"Year = {year_number}\tFuture Value = ${round(future_value, 2)}") # prints the future value for that given year


    # see if the user wants to continue
    print() # Adds a blank line
    choice = input("Continue (y/n)? ") # Gets input from the user if they want to continue or not
    print() # Adds a blank line

print("Bye!") # Salutation message
