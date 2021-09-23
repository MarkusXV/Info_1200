#Name: (Peter Sanford)
#Class: (INFO 1200)
#Section: (001)
#Professor: (Crandall)
#Date: 9/16
#Project #: M02 Part 3
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

firstName = 'Peter'
print('Hello, my name is ' + firstName)

var_school = ' Utah Valley University'
print('I go to' + var_school)

credits = 3
classes = 6
totalcredits = credits * classes

print('If I take 6 classes this semester and all are three credits each, I will be taking ' + str(totalcredits) + " credits")

print('I would like to save money by taking this many credits.')

maxCredits = 12
costPerClass = 350
classFee = 20

totalCostPerSemester = ((totalcredits - maxCredits) / (credits)) * costPerClass + (classFee * ((totalcredits - maxCredits)/(credits)))

print('If classes are free after the ' + str(maxCredits) + ' credits and each class cost $' + str(costPerClass) + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.')

totalCostPerYear = totalCostPerSemester * 3

print('That is a wopping $' + str(totalCostPerYear) + ' a year!')
print('This was a very informative and worth while Python assignment!')




