#!/usr/bin/env python3

TAX = 0.06 # Creates the global variable for tax

'''Calculates the Sales tax from the total'''
def sales_tax(total): # function named sales_tax with a total argument
    sales_tax = total * TAX # Calculates the sales_tax from the total and global tax
    return sales_tax # Returns the sales_tax so we can use it outside of the function

'''Runs all other functions'''
def main():
    print("Sales Tax Calculator\n") # Prints the title of the function
    total = float(input("Enter total: ")) # Gets the input for the total from the user and changes to a float
    total_after_tax = round(total + sales_tax(total), 2) # Calculates the after tax total and rounds it to two decimal points
    print("Total after tax: ", total_after_tax) # Prints the total after tax
    
if __name__ == "__main__": # if this is the main module, run the main function
    main()
