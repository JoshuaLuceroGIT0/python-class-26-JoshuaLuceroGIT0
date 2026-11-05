# Starting file for LAB 6-2
# Include your course number, student first and last name, and date in the comment header
# CS 31, josh lucero, 11-4-26


def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie[0]} ({movie[1]})"
                  + " @ " + str(movie[2]))
        print()

def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    price = input("Price: ")
    movie = [name, year]
    movie.append(name)
    movie.append(year)
    movie.append(price)
    movie_list.append(movie)
    print(f"{movie[0]} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie[0]} was deleted.\n")




def display_menu():
    print("The Fantastic List Movie Program!")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find movies by year")
    print("exit - Exit program")
    print()
    
def find_by_year(movie_list):
    year = int(input("Year: "))
    found_movies = [movie for movie in movie_list if str(movie[1]) == str(year)]
    if found_movies:
        print(f"Movies from {year}:")
        for movie in found_movies:
            print(f"{movie[0]} ({movie[1]}) @ {movie[2]}")
    else:
        print(f"No movies found from {year}.")
    print()

def main():
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                  ["On the Waterfront", 1954,5.99],
                  ["Cat on a Hot Tin Roof", 1958, 7.99]]
    
    display_menu()
    
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "find":
            find_by_year(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
