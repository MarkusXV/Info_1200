#!/usr/bin/env python3

import csv

'''
3. Create an If elif elif else statement
4. Read a .csv or .txt file
5. Write to a .csv or .txt file
6. For loop and print all items inside the loop
7. List that holds a 2d list
'''


def print_menu():
    print("Command Menu:\n"
          "view\t= Views Total To-Do List\n"
          "add\t= Adds a New To-Do Entry\n"
          "delete\t= Deletes a To-Do Entry\n"
          "exit\t= Exits the program\n")

def read_to_do():
    lto_do = []
    try:
        with open("To_Do_List.csv", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    lto_do.append(row)
                return lto_do
    except FileNotFoundError:
        return lto_do
    
def write_to_do(to_do):
    with open("To_Do_List.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(to_do)

def add_to_do(to_do):
    lto_do = []
    
    name = input("\nWhat Needs to Get Done?\t")
    date = input("When is the Deadline to Get this Done?\t")

    lto_do.append(name)
    lto_do.append(date)
    to_do.append(lto_do)

    write_to_do(to_do)
    view_all_to_do(to_do)
    print_menu()

def delete_to_do(to_do):
    while True:
        try:
            number = int(input("\nWhich # of the To-Do Entries do you want to delete? "))
        except ValueError:
            print("\nPlease input a number")
            continue

        if number > 0 and number <= len(to_do):
            to_do.pop(number - 1)
            break
        else:
            print("\nInvalid Number")
            continue

    write_to_do(to_do)
    view_all_to_do(to_do)
    print_menu()


def view_all_to_do(to_do):
    if len(to_do) != 0:
        print("\n\tTo Do\t|   Due Date\n")

        counter = 1
        for row in to_do:
            print(f"{counter}. {row[0]}  |  {row[1]}")
            counter += 1
        print()
    else:
        print("\n\tNothing in To Do List Currently\n")

    
def main():
    to_do = read_to_do()
    view_all_to_do(to_do)
    print_menu()
    
    while True:
        command = input("Command: ")
        if command.lower() == "view":
            view_all_to_do(to_do)
            print_menu()
        elif command.lower() == "add":
            add_to_do(to_do)
        elif command.lower() == "delete":
            delete_to_do(to_do)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")



if __name__ == "__main__": # if this is the main module, run the main function
    main()
