#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date: 9/23/2021
#Project #: MO4_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

print("Peter Sanford's Tip Calculator") # Prints first and last name with title
print() # Adds a blank line

tip_percentage = [5 , 15 , 30] # Sets the tip percentages we want to calculate using the for loop

meal_cost = float(input("Cost of meal: ")) # Gets the meal cost from the user
print() # Adds a blank line

for i in range(len(tip_percentage)): # Sets up the for loop to run through the different values in the tip_percentage variable
    print(str(tip_percentage[i]) + "%") # Prints the percentage value that the loop is in
    tip_percent = tip_percentage[i] / 100 # Calculates the tip percentage depending on what value the loop is on
    tip_amount = round(meal_cost * tip_percent, 2) # calculates the tip amount and rounds to two decimal places
    total_amount = tip_amount + meal_cost # calculates the total amount of the meal
    print(f"Tip amount:\t{tip_amount}") # Displays the amount of the tip with that percentage
    print(f"Total amount:\t{total_amount}") # Displays the total cost of the meal
    print() # Adds a blank line at the end of each loop cycle
