#! /usr/bin/env python3
# Declare variables
hours = 0
minutes = 0
seconds = 0

# Show the title of the time machine
print("Peter's Time Machine")

# Get user input as an int for seconds
total_seconds = int(input("Enter seconds: "))
print()

# Convert to hours
hours = total_seconds // 3600

# Convert to minutes
minutes = (total_seconds % 3600) // 60 

# Convert to seconds
seconds = total_seconds % 60                    

# Display hours, minutes, and seconds
print(f"Hours:\t\t{hours}")
print(f"Minutes:\t{minutes}")
print(f"Seconds:\t{seconds}")
