#!/usr/bin/env python3

TAX = 0.06 #Sets the tax variable for the whole program

'''
Function that calculates the sales tax of the bill and returns the value
'''
def sales_tax(total): # Names the function sales_tax with one argument, total
    sales_tax = total * TAX # Sets sales_tax equal to the inputted value multiplied by the tax variable declared earlier
    return sales_tax # returns the sales_tax variable to the function

'''
defines the main function that runs all other functions
'''
def main(): 
    print("Sales Tax Calculator\n") # displays Sales Tax Calculator with a line return
    total = float(input("Enter total: ")) # Gets a float value from the user and stored in total variable
    total_after_tax = round(total + sales_tax(total), 2) # Calls the sales_tax variable with the total parameter passed in,
    # added to the total bill, and rounded to two decimals
    print("Total after tax: ", total_after_tax) # displays the total after tax is added
    
if __name__ == "__main__": # Runs the main function if this is the main module
    main()
