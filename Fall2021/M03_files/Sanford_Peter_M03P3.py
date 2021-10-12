#!/usr/bin/env python3
print("Peter Sanford's Rectangle App") # display a welcome message with name

print() # adds blank line

# gets both inputs from the user
length= float(input("Please enter the length: "))
width = float(input("Please enter the width: "))

# calculate miles per gallon
area = length * width # Calculates area
perimeter = 2 * (length + width) # calculates perimeter
            
# format and display the result
print()
print(f"Area = {area}")
print(f"Perimeter = {perimeter}")
print()
print("Thanks for using this program!")


