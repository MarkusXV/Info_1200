#Name: (First Name Last Name)
#Class: (INFO 1200)
#Section: (X01)
#Professor: (Crandall)
#Date:
#Project #: M10
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

import csv


def display_title():
    print("Trevor Sanford's Monthly Sales")

def display_menu():
    print("COMMAND MENU\n")
    print("1 - View Monthly Sales")
    print("2 - View Yearly Sales")
    print("3 - Edit Sales")
    print("q - Exit program")

def read_sales():
    sales = []
    with open("monthly_sales.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
    file.close()
    return sales

def view_monthly_sales(sales):
    print()
    for row in sales:
        print(f"{row[0]} - {row[1]}")

def view_yearly_summary(sales):
    total=0
    for row in sales:
        amount = int(row[1])
        total += amount

    # get count
    count = len(sales)
    
    # calculate average
    average = total / count
    average = round(average, 2)

    # format and display the result
    print("\nYearly total:    ", total)
    print("Monthly average: ", average)        

def edit(sales):
    print(sales)
        

def main():
    display_title()
    display_menu()
    sales=read_sales()

    while True:
        command = input("\nCommand: ")
        if command == "1":
            view_monthly_sales(sales)
        elif command == "2":
            view_yearly_summary(sales)
        elif command == "3":
            edit(sales)
        elif command == "q":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
    



       
main()
