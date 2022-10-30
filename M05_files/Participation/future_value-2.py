#!/usr/bin/env python3


print("Sanford's Validated Future Value App")

import validate as v # imports the validate module with the name v
        
'''
Sets a function that calculates the future value with three parameters
'''
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 # converts the yearly value to a monthly value as a decimal point
    months = years * 12 # Creates a months variable that converts the amount of years to the amount of months

    # calculate future value
    future_value = 0.0 # sets the future_value variable to 0 so we can use it later
    for i in range(0, months): # sets a for loop that will run for as many months as there are
        future_value += monthly_investment # adds the new amount added each month
        monthly_interest = future_value * monthly_interest_rate # calculates how much interest was accumulated that month
        future_value += monthly_interest # Adds how much interest there was to the total value accumulated

    return future_value # returns the final value once the for loop is done calculating it

'''
This function runs all of the other functions created
'''
def main(): # creates the main function
    choice = "y" # Sets the choice variable to y so that the while loop with run initially
    while choice.lower() == "y": # sets the while loop to run as long as choice is set to y
        # get input from the user
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 1000) # calls the get_float variable from the imported file called v
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15) # calls the get_float variable from the imported file called v
        years = v.get_int("Enter number of years:\t\t", 0, 50) # calls the get_int variable from the imported file called v

        # get and display future value
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years) # Calls the function defined above called calculate_future_value to calculate the future value

        print(f"Future value:\t\t\t{round(future_value, 2)}") # prints the future value after it's calculated
        print() # adds a blank line

        choice = input("Continue? (y/n): ") # see if the user wants to continue
        print() # adds a blank line

    print("Bye!") # prints the salutation message

    
if __name__ == "__main__": # runs the main function if run in this file, says that this file can be run by itself
    main()
