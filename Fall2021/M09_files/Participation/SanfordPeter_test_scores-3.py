#!/usr/bin/env python3

import math # imports the math function

'''Displays a welcome message'''
def display_welcome(): # defines function called display_welcome
    print("The Test Scores program") # prints the welcome message
    print("Enter 'x' to exit") # tells the user how to exit
    print("") # Adds blank line

'''Gets the user's input for the scores list'''
def get_scores(): # defines function called get_scores
    score_total = [] # sets an empty list so we can add to it later
    while True: # creates an infinite while loop for getting scores
        score = input("Enter test score: ")
        if score.lower() == "x":
            return  score_total # if the user puts in x, it stops getting values
        else:
            score = int(score) # makes it an int instead of str so we can put it in the list
            if score >= 0 and score <= 100: # checks to see if the score is valid
                score_total.append(score) # Adds the new score to the list
            else:
                print("Test score must be from 0 through 100. " + "Score discarded. Try again.") # Displays an error message

'''Processes the scores and gives statistical analysis'''
def process_scores(score_total): # defines function called process_scores
    score_total.sort() # sorts the values so the median is calculated correctly
    average = sum(score_total) / len(score_total) # calculates the average
    total = 0 # creates a variable total so we can use it later
    for n in score_total: # runs for every number in the list
        total += n # adds all of the numbers in the list together
    total_index = len(score_total) # Sets variable equal to the total amount of numbers
    if total_index % 2 != 0: # Sees if the total amount of numbers is divisible by two or not
        median = score_total[int((total_index - 1) / 2)] # Calculates the median if the total number in the list is not even
    else: # calculates the median if the total number in the list is even
        first_median_num = score_total[int(total_index // 2 - 1)] # Finds the lower median number from the list
        second_median_num = score_total[int(total_index // 2)] # Finds the upper median number from the list                          
        median =  (first_median_num + second_median_num) / 2 # averages the two above median numbers
                   
    print() # Adds a blank line
    print("Score total:       ", total) # Prints the score total
    print("Number of Scores:  ", len(score_total)) # Prints the total count of numbers
    print("Average Score:     ", average) # Prints the average
    print("Median:            ", median) # Prints the median

def main(): # defines the main function
    display_welcome() # calls the display welcome function
    score_total = get_scores() # calles the get scores function and puts it into the score total variable
    process_scores(score_total) # calles the process scores variable and passes the score total variable list in
    print() # prints blank line
    print("Bye!") # prints the salutation

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


