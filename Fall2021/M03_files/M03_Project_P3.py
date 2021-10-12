print("Peter Sanford's Tip Calculator App") # Displays first and last name with title

costOfMeal = float(input("What's the cost of the meal? ")) # gets input for the cost of the meal
tipPercentage = float(input("What's the percentage of tip you want to give? ")) # gets the user's desired tip percentage

tip = round(costOfMeal * (tipPercentage / 100), 2) # calculates the tip amount
print("Tip amount: ", tip) # displays the tip amount

totalMealCost = round(tip + costOfMeal, 2) # calculates the total meal cost
print("Total amount: ", totalMealCost) # displays the total meal cost
