print("Peter Sanford's Pay Check Calculator App") # Displays first and last name with title
print() # adds a blank line

hoursWorked = int(input("How many hours have you worked? ")) # gets user's hours worked
payRate = int(input("How much do you get payed hourly? ")) # gets user's hourly pay
print() # adds a blank line

grossPay = hoursWorked * payRate # calculates gross pay
print("Gross Pay: ", grossPay) # displays user's gross pay

taxRate = 18
print("Tax Rate: ", taxRate)
taxAmount = grossPay * (taxRate / 100)

print("Tax Amount: ", taxAmount)


