#!/usr/bin/env python3

import csv # imports the csv module

'''Gets the miles driven from the user'''
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0: # Gets the number from the user
        print("Entry must be greater than zero. Please try again.\n") # Prints an error if the number is less than zero
    return miles_driven # returns the number entered

'''Gets the amount of gallons used'''
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0: # Gets the number from the user                 
        print("Entry must be greater than zero. Please try again.\n") # Prints an error if the number is less than zero
    return gallons_used # returns the number entered

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print() # Adds a blank line

    alltrips = [] # creates a list that we can use later

    more = "y" # Creates a more variable that will let the user keep going or stop the while loop
    while more.lower() == "y":
        miles_driven = get_miles_driven() # Calls the get miles function to get it from the user
        gallons_used = get_gallons_used() # Calls the get gallons function to get it from the user
                                 
        mpg = round((miles_driven / gallons_used), 2) # Calculate the mpg from those two inputted values
        print(f"Miles Per Gallon:\t{mpg}") # prints the Data that they entered as well as the mpg
        print() # Adds a blank line

        #Creates a trip list and puts the new data into it
        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)

        alltrips.append(trip)# adds that list we just made to the alltrips list, making it two-dimensional
        
        
        more = input("More entries? (y or n): ") # asks the user if they want to add another trip
        print() # Adds a blank line
    
    with open("trips.csv", "w", newline = "") as file: # Writes the alltrips list to the csv file so that the user will have it later
        writer = csv.writer(file)
        writer.writerows(alltrips)

    print("\nBye!") # prints a bye message

if __name__ == "__main__": # if this is the main module, call the main function
    main()

