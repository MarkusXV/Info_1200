#!/usr/bin/env python3
print("Peter Snaford's MPG App") # Show the title with name

print("The Miles Per Gallon program") # display a welcome message
print() #adds blank line

# gets theinputs of miles driven, gallons used, and cost per gallon from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

mpg = round(miles_driven / gallons_used, 1) # calculate miles per gallon
total_cost = round(cost_per_gallon * gallons_used, 2) # calculates the total cost
cost_per_mile = round(total_cost / miles_driven, 2) # calculates the cost per mile
            
# format and display the result
print() # adds blank line
print(f"Miles Per Gallon:\t\t{mpg}") # prints the miles per gallon
print(f"Total cost:\t\t\t{total_cost}") # prints the total cost
print(f"Cost Per Mile:\t\t\t{cost_per_mile}") # prints the cost per mile
print() # adds blank line
print("Bye") # ending salutation


