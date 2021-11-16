#!/usr/bin/env python3

import csv

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def write_trips(trips):
    with open("trips.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def read_trips():
    with open("trips.csv", "r") as file:
        reader = csv.reader(file)
        trips = []
        for row in reader:
            each_trip = []
            each_trip.append(row[0])
            each_trip.append(row[1])
            each_trip.append(row[2])
            trips.append(each_trip)
        return trips
        

def list_trips():
    with open("trips.csv", "r") as file:
        print("Distance\t Gallons\t MPG")
        reader = csv.reader(file)
        for row in reader:
            each_trip = []
            each_trip.append(row[0])
            each_trip.append(row[1])
            each_trip.append(row[2])
            print(each_trip[0] + "\t\t", each_trip[1] + "\t\t", each_trip[2])
       

def main():
    # display a welcome message
    print("The Miles Per Gallon Program\n")

    trips = read_trips()
    list_trips()
    print() # adds a blank line
    

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}\n")

        new_trip = []
        new_trip.append(miles_driven)
        new_trip.append(gallons_used)
        new_trip.append(mpg)
        trips.append(new_trip)
        
        write_trips(trips)
        list_trips()

        more = input("\nMore entries? (y or n): ")
    
    print("\nBye!")

if __name__ == "__main__":
    main()

