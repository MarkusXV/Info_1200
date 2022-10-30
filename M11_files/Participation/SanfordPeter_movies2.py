# Imports the following modules
import csv
import sys

FILENAME = "movies.csv" 

'''Exits the program'''
def exit_program():
    print("Terminating program.")
    sys.exit() 

'''Reads the csv file and puts it into the movies list'''
def read_movies():
    try: # try to read the csv and prints the exceptions if the occur
        rmovies = [] 
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                rmovies.append(row)
        return rmovies
    except FileNotFoundError as e: # If there's a File not found error, return the empty list
        return rmovies
        # We removed these so that if there wasn't a file, it would create it when we try to write to it later
##        print(f"Could not find {FILENAME} file.")
##        exit_program()
    except Exception as e: # If there's any other exception:
        print(type(e), e) # Print both the type and the discription
        exit_program() # calls the exit_program that ends the program

'''Writes the movies list to the csv file'''
def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            # this line will throw a Blocking IO error to test what would happen if the user encounters this error
            raise BlockingIOError("Error raised for testing.")
            writer = csv.writer(file)
            writer.writerows(movies)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

'''Lists all the movies in the movies list'''
def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()

'''Adds a movie to the movie list and writes it to the csv file'''
def add_movie(movies):
    name = input("Name: ")
    while True: # Creates a loop for getting the year input
        try: # try block that has statements that could throw exceptions
            year = int(input("Year: ")) # Could get a value error if the user puts in a string for example
        except ValueError: # if theres a value error:
            print("Needs to be a number.") # prints that it needs to be a number
            continue # Continues to the next loop iteration so they can input a different number
        if year < 0: # Checks to see if the year is less than zero
            print("Year needs to be greater than zero.") # prints that the number needs to be greater than zero
            continue # Continues to the next loop iteration so they can input a different number
        break # If the year is correct and there are no exceptions, breaks out of the while loop
    movie = [name, year]
    movies.append(movie)
    write_movies(movies)
    print(f"{name} was added.\n")

'''Deletes a certain movie from the list and writes to csv file'''
def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

'''Prints a diplay menu'''
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

'''Runs all other functions'''
def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__": # if this is the main module, run the main function
    main()
