#!/usr/bin/env python3

'''Gets a number from the user'''
def get_number(prompt, low, high):
    while True:
        try: # adds a try block of the statements that can throw exceptions
            number = float(input(prompt)) # Can get a value error if the user puts in a value that can't be converted to a float
        except ValueError: 
            print("Needs to be a decimal number.") # If there's a value error, it will print that it needs to be a number or decimal number
            continue # Continues the loop to the next iteration so they can input another number
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")

'''Gets an integer from the user'''            
def get_integer(prompt, low, high):
    while True:
        try: # Adds a try block of the statements that can throw exceptions
            number = int(input(prompt)) # Can get a value error if the user puts in a value that can't be converted to an integer
        except ValueError:
            print("Needs to be a number.") # If there's a value error, it will print that it needs to be a number
            continue # Continues the loop to the next iteration so they can input another number
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")

'''Calculates the future value using the inputted numbers'''
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

'''Runs all other functions'''
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__": # if this is the main module, run the main function
    main()
