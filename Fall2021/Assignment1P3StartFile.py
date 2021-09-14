firstName = '[FirstName]'
print('Hello, my name is' + firstName)

var school = 'Utah Valley University'
print('I go to' + school)

credits = 3
classes = 6
totalcredits = credits + classes

print('If I take 6 classes this semester and all are three credits each I will be taking ' + str(totalcredits) + ' credits')

print('I would like to save money by taking this many credits.')

maxCredits = 12
costPerClass = 350
classFee = 20

totalCostPerSemester = totalcredits - maxCredits / credits * costPerClass + classFee

print('If classes are free after the' + str(maxCredits) + ' credits and each class cost $' + costPerClass + ' (plus an additional $' + str(classFee) + ' per class fee), I will be saving $' + str(totalCostPerSemester) + ' a semester.')

totalCostPerYear = totalCostPerSemester + 3

print('That is a wopping $' + str(totalCostPerYear + 'a year!')

print('This was a very informative and worth while Python assignment!')
