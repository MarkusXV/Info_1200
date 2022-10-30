#!/usr/bin/env python3

#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date: 10/30/21
#Project #: MO7_P2
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import random # imports the random module so we can use those functions


'''Function that displays the title of the program'''
def display_title(): # Names the function display_title with no arguments
    print("Guess the number!") # Prints the title of the program
    print() # Adds a blank line
    
'''Function that gets the limit of the random number from the user'''
def get_limit(): # Names the function get_limit with no arguments
    limit = int(input("Enter the upper limit for the range of numbers: ")) # gets the input limit from the user
    return limit # Returns the limit value from the user to the function

'''Function that generates a random number and the user has to guess that number'''
def play_game(limit): # Names the function play_game with one argument limit
    number = random.randint(1, limit) # sets the variable number
    # that calls a function from the random module that gets a random integer from 1 to the limit
    print(f"I'm thinking of a number from 1 to {limit}\n") # prints the range that the random number could be in
    
    count = 0 # initializes the count variable so it can be used later
    while True: # Sets up an infinite while loop
        guess = int(input("Your guess: ")) # Gets the guessed number from the user
        if guess < number: # If the guess is lower than the random number, prints that the guess was too low
            print("Too low.") # prints too low
            count += 1 # adds one to the counter
        elif guess > number: # If the guessed number is higher than the random number, prints that the guess was too high
            print("Too high.") # prints too high
            count += 1 # adds one to the counter
        elif guess == number: # if the guessed number is equal to the random number, prints that the user guessed it correctly
            count += 1 # adds one to the counter
            print(f"You guessed it in {count} tries.\n") # prints that the user was correct and displays how many guesses it took
            return # returns so that we get out of the infinite while loop

'''Function that runs all of the other functions'''
def main(): # defines the main function
    display_title() # calls the display title function first
    
    again = "y" # sets again equal to y so that the while loop will initially start
    while again.lower() == "y": # sets up a while loop that runs if again is equal to y
        limit = get_limit() # sets limit variable that calls the get limit function to get the limit from the user
        play_game(limit) # calls the play game function and passes in the limit as a parameter
        
        again = input("Play again? (y/n): ") # asks the user if they would like to play again
        print() # adds a blank line
    print("Bye!") # prints bye if they didn't want to continue

if __name__ == "__main__": # if started as the main module, call the main function
    main()


