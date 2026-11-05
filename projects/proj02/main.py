# Starting file for PROJECT 2
# Include your course number, student first and last name, and date in the comment header
# CS 31, josh lucero, 11-4-26

#added a counter
counter = 0

#we put everything in a while loop so the user can keep replaying with a counter :)
while True:


    print("The Spontaneous RPG!")
    print("Times played: ", counter)


    #Here we ask if the user wants to play and also added a counter.
    choice = input("Would you like to try the Spontaneous RPG? y/n:")
    if choice.upper() == "Y":


             
        
        counter += 1
        print("\nTimes played:", counter)
        print("You are brave, adventurer.")
    else:
        print("You are not brave enough for this adventure. Farewell, adventurer.")
        raise SystemExit

    name = input("Please enter your name:")
    print(f"Welcome, {name}!")


    #Here we ask which story they want 1 or 2...
    story = input("Would you like to experience story 1 or story 2? 1/2:")
    if story == "1":
        print("You have chosen story 1...")

        scent = input("What is your favorite scent?")
        weapon = input("Your choice of weapon for your adventure:")
        monster = input("Monster that you are afraid of?")
        level = input("What level would you be on this adventure?")
        armor = input("What type of armor would you wear?")
        difficulty = input("What difficulty would you like to play on?")
        print(f"As you entered the woods, a dark {scent} filled the air.")
        print(f"You hold your {weapon} for anything that appears.")
        print(f"Out of nowhere, a {monster} attacks you!!")
        print(f"However, you are level {level}")
        print(f"You are also wearing {armor}, which protects you from the {monster}!")
        print(f"You have selected {difficulty}, which makes the battle easier for your tastes...")

    elif story == "2":
        print("You have chosen story 2...")

        goomba = input("What would you name a goomba?")
        princessPeach = input("What was princess peach wearing?")
        mario = input("Mario jumped over what now?")
        bowser = input("Bowser likes what type of food?")
        luigi = input("Luigi does what type of activity for fun?")
        yoshi = input("Yoshi likes to eat what?")

        print(f"You are going for a walk and you see a {goomba} on the ground.")
        print(f"Moreover, you see princess peach wearing {princessPeach}.")
        print(f"Suddenly, Mario jumps over {mario} just to get to princess peach.")
        print(f"Bowser joins the party and eats {bowser} while nearby them.")
        print(f"Luigi is having fun doing some {luigi} chilling with them.")
        print(f"Finally, Yoshi was also eating {yoshi} with Luigi.")
        print("What an awesomeday for everyone! The end!")

    #here we ask if they want to play again \n introduces a line break for formatting :)
    play_again = input("\nWould you like to play again? (y/n): ")

    #we use continue to go back to the top of the whole code and start over :)
    if play_again.upper() == "Y":
        counter += 1
        continue 

#raise Systemexit is used to force the program to stop running
else:
    print("You are not brave enough for this adventure. Farewell, adventurer.")
    raise SystemExit

