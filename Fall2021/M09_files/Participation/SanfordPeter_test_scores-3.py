#!/usr/bin/env python3

'''Displays a welcome message'''
def display_welcome(): # defines function called display_welcome
    print("The Test Scores program") # prints the welcome message
    print("Enter 'x' to exit") # tells the user how to exit
    print("") # Adds blank line

'''Gets the user's input for the scores list'''
def get_scores(): # defines function called get_scores
    scores = [] # sets an empty list so we can add to it later
    while True: # creates an infinite while loop for getting scores
        score = input("Enter test score: ")
        if score.lower() == "x":
            return  scores # if the user puts in x, it stops getting values
        else:
            score = int(score) # makes it an int instead of str so we can put it in the list
            if score >= 0 and score <= 100: # checks to see if the score is valid
                scores.append(score) # Adds the new score to the list
            else:
                print("Test score must be from 0 through 100. " + "Score discarded. Try again.") # Displays an error message

'''Processes the scores and gives statistical analysis'''
def process_scores(scores): # defines function called process_scores
    scores.sort() # sorts the values so the median is calculated correctly
    total = 0 # creates a variable total so we can use it later
    
    for n in scores: # runs for every number in the list
        total += n # adds all of the numbers in the list together
    average = total / len(scores) # calculates the average
    
    total_index = len(scores) - 1 # Sets variable equal to the index number total

    # Calculates the minimum and maximum number
    minimum = scores[0]
    maximum = scores[total_index]
    median_index = total_index // 2

    # Calculates the median number
    if len(scores) % 2 != 0: # Sees if the total amount of numbers is divisible by two or not
        # Calculates the median if the total number in the list is not even
        median = scores[int(median_index)] 
        
    else:
        # calculates the median if the total number in the list is even
        first_median_num = scores[int(median_index)] # Finds the lower median number from the list
        second_median_num = scores[int(median_index + 1)] # Finds the upper median number from the list                          
        median =  (first_median_num + second_median_num) / 2 # averages the two above median numbers

    # Format and display the results        
    print()
    print("Score total:       ", total) 
    print("Number of Scores:  ", len(scores)) 
    print("Average Score:     ", average) 
    print("Minimum Number:    ", minimum) 
    print("Maximum Number:    ", maximum) 
    print("Median:            ", median) 

def main(): # defines the main function
    display_welcome() # calls the display welcome function
    scores = get_scores() # calles the get scores function and puts it into the score total variable
    process_scores(scores) # calles the process scores variable and passes the score total variable list in
    print() # prints blank line
    print("Bye!") # prints the salutation

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


