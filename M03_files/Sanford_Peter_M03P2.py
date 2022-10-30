#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores

test1 = int(input("Enter test score: ")) # gets input for first test
total_score += test1 # adds first test to total score
test2 = int(input("Enter test score: ")) # gets input for second test
total_score += test2 # adds second test to total score
test3 = int(input("Enter test score: ")) # gets input for third test
total_score += test3 # adds third test to total score

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print("Your scores: ", test1, test2, test3,
      "\nTotal Score:  ", total_score,
      "\nAverage Score: ", average_score)
print()
print("Bye")


