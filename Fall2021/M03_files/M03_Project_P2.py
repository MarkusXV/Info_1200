print("Peter Sanford's Pay Check Calculator App") # Displays first and last name with title
print() # adds a blank line

hoursWorked = float(input("How many hours have you worked? ")) # gets user's hours worked
payRate = float(input("How much do you get payed hourly? ")) # gets user's hourly pay
print() # adds a blank line

grossPay = hoursWorked * payRate # calculates gross pay
print("Gross Pay: ", grossPay) # displays user's gross pay

taxRate = 18 # sets the tax rate variable
print("Tax Rate: ", str(taxRate) + "%") # displays the tax rate
taxAmount = grossPay * (taxRate / 100) # calculates the tax amount

print("Tax Amount: ", taxAmount) # prints the tax amount

takeHomePay = round(grossPay - taxAmount, 2) # calculates take home pay and rounds to two decimal places
print("Take Home Pay: ", takeHomePay) # displays the take home pay



