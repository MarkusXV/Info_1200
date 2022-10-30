#!/usr/bin/env python3

import csv # imports the csv module

'''Gets the miles driven from the user'''
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0: # Gets the number from the user
        print("Entry must be greater than zero. Please try again.\n") # Prints an error if the number is less than zero
    return miles_driven # Returns the number entered

'''Gets the amount of gallons used'''
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0: # Gets the number from the user
        print("Entry must be greater than zero. Please try again.\n") # Prints an error if the number is less than zero
    return gallons_used # Returns the number entered

'''Writes the trips list to the csv file'''
def write_trips(trips):
    with open("trips.csv", "w", newline = "") as file: # opens the file and writes to it
        writer = csv.writer(file)
        writer.writerows(trips)

'''Reads the csv file and puts it into the trips list'''
def read_trips():
    with open("trips.csv", "r") as file: # opens the file and reads it
        reader = csv.reader(file)
        trips = []
        for row in reader: # puts each individual list into the trips list
            each_trip = []
            each_trip.append(row[0])
            each_trip.append(row[1])
            each_trip.append(row[2])
            trips.append(each_trip)
        return trips
        
'''Reads the csv file and then prints each trip in that list'''
def list_trips():
    with open("trips.csv", "r") as file: # opens the file and reads it
        print("Distance\t Gallons\t MPG")# prints the header
        reader = csv.reader(file)
        for row in reader: # puts each individual list into the trips list
            each_trip = []
            each_trip.append(row[0])
            each_trip.append(row[1])
            each_trip.append(row[2])
            print(each_trip[0] + "\t\t", each_trip[1] + "\t\t", each_trip[2]) # prints each trip individually
       

def main():
    # display a welcome message
    print("The Miles Per Gallon Program\n")

    trips = read_trips() # Calls the read trips function
    list_trips() # calls the list trips function
    print() # adds a blank line
    

    more = "y" # Creates a more variable that will let the user keep going or stop the while loop
    while more.lower() == "y":
        miles_driven = get_miles_driven() # calls the get miles function to get it from the user
        gallons_used = get_gallons_used() # calls the get gallons function to get it from the user
                                 
        mpg = round((miles_driven / gallons_used), 2) # Calculates the mpg from those two inputted values
        print(f"Miles Per Gallon:\t{mpg}\n") # Prints the miles per gallon

        # Creates a trip list and puts the new data into it
        new_trip = []
        new_trip.append(miles_driven)
        new_trip.append(gallons_used)
        new_trip.append(mpg)
        trips.append(new_trip)

        write_trips(trips) # Writes the trips list to the csv
        list_trips() # Lists the trips again

        more = input("\nMore entries? (y or n): ") # asks the user if they want to add another trip
        print() # Adds a blank line
    
    print("\nBye!") # prints a bye message

if __name__ == "__main__": # if this is the main module, call the main function
    main()

