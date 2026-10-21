# Starting file for LAB 4
# Include your course number, student first and last name, and date in the comment header
#CS 31 - 72473 Joshua Lucero 

import random

LIMIT = 10



#print the title of the program
def display_title():
    print("Guess the Number game")
    print()



def play_game():
    print("""
        Easy - Guess from 1 to 10, limit 5 attempts
        Medium - Guess from 1 to 100, limit 7 attempts
        Hard - Guess from 1 to 1000, limit 10 attempts
    """)
    your_level = input("Which level would you like to play? E/M/H:  ")
    # Set the limit based on their game level choice
    if your_level.upper() == "E":
        limit = 10
        attempts = 5
    elif your_level.upper() == "M":
        limit == 100
        attempts = 7
    elif your_level.upper() == "H":
        limit = 1000
        attempts = 10
    else:
        limit = 10000 # punish them if they don't enter a correct level :)
        attempts = 5

    secret_number = random.randint(1, LIMIT)
    print(f"I am thinking of a number from 1 to {LIMIT}\n")
    # \n prints a new line f does f string
    count = 1
    #count = 1 # keep track of the total number of attempts



    # check if they have any attempts left
    if count  <= attempts:


        while (guess := int(input("Your guess: "))) != secret_number: #!= means does not equal
            if count >= attempts:
                print ("Sorry, you ran out of attempts!")
                break
            

            # the guess is incorrect
            if guess < secret_number:
                print("Sorry, your guess is too low.")
            elif guess > secret_number:
                print("Sorry, your guess is too high.")
            count += 1 #increment the guess attempt counter

        else: # if they guessed correctly
            print(f"Congrats! you guessed it in {count} tries!\n")


    # if they guess correctly 
    print(f"Congrats! You guessed it in {count} tries!\n")

def main():
    # the main program driver
    display_title()
    again = "y" # set initial game loop variable

    #ask for the players name
    player_name = input("Hi there! What is your name? ")
    print()

    while again.lower() == "y": # play the game
        play_game()
        again = input(f"Would you like to play another round of the game?, {player_name} y/n: ")
        print()


    print("Thanks for playing! Goodbye!")

#if started as the main module, call the main() function
if __name__ == "__main__":
    main()
    
