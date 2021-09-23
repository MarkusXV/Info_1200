print("Peter Sanford's Registration App") # Displays first and last name with title
print() # adds a blank line

user_first_name = input("What's your first name?  ") # Gets user's first name
user_last_name = input("What's your last name?  ") # Gets user's last name
user_birth_year = input("What year were you born?  ") # Gets user's birth year
print() # adds a blank line

print("Welcome", user_first_name, user_last_name + "!") # displays a welcome message
print() # adds a blank line
print("Your registration is complete") # displays that the registration is comeplete

temp_pass = user_first_name + "*" + user_birth_year # sets temporary password
print("Your temporary password is: ", temp_pass) # tells the user what their temporary password is
