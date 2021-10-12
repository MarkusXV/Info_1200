#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date: 9/23/2021
#Project #: MO4_P1
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.


print("Peter Sanford's Letter Grade Converter") # Prints first and last name with title
print() # Adds blank line

choice = "y" # Sets choice to y so that the while loop will start
while choice.lower() == "y": # Sets up while loop so that if the user types in a y, the loop continues and if they type in an n, the loop stops
    number = int(input("Enter numerical grade: ")) # Gets the grade from the user
    if number > 93: # Sees if the grade is an A
        letter = "A" # Sets letter to the correct letter grade for the percentage
    elif number > 89: # Sees if the grade is an A-
        letter = "A-" # Sets letter to the correct letter grade for the percentage
    elif number > 86: # Sees if the grade is an B+
        letter = "B+" # Sets letter to the correct letter grade for the percentage
    elif number > 82: # Sees if the grade is an B
        letter = "B"  # Sets letter to the correct letter grade for the percentage
    elif number > 79: # Sees if the grade is an B-
        letter = "B-" # Sets letter to the correct letter grade for the percentage
    elif number > 76: # Sees if the grade is an C+
        letter = "C+" # Sets letter to the correct letter grade for the percentage
    elif number > 72: # Sees if the grade is an C
        letter = "C"  # Sets letter to the correct letter grade for the percentage
    elif number > 69: # Sees if the grade is an C-
        letter = "C-" # Sets letter to the correct letter grade for the percentage
    elif number > 66: # Sees if the grade is an D+
        letter = "D+" # Sets letter to the correct letter grade for the percentage
    elif number > 63: # Sees if the grade is an D
        letter = "D"  # Sets letter to the correct letter grade for the percentage
    elif number >= 59: # Sees if the grade is an D-
        letter = "D-" # Sets letter to the correct letter grade for the percentage
    elif 0 <= number <= 59: # Sees if the grade is an F
        letter = "F" # Sets letter to the correct letter grade for the percentage
    print(letter) # Displays the letter grade
    print() # Adds a blank line
    choice = input("Would you like to continue? (y/n): ") # Asks the user if they would like to continue

print() # Adds blank line
print("Bye!") # Salutation once the user ends the loop
