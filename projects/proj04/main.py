# Starting file for PROJECT 4
# Include your course number, student first and last name, and date in the comment header
#CS 31, Josh Lucero, 11-25-26



#here we import random
import random

#we make a function too choose a random character type 
#followed by a list
def choose_character_type():
    character_types = [
        "Nordic Warrior",
        "Void Assassin",
        "Wood Elf",
        "Water Mage",
        "Pirate Ninja",
    ]
    return random.choice(character_types)
    #picking one random item, and returning it
    #as the output for the function

#making another function for random stats :O
def generate_character(name):
    stat_names = [
        "Strength",
        "Intellect",
        "Hit Points",
        "Wisdom",
        "Charisma",
        "Dexterity",
    ]

    #creating a dictionary for character... key: value
    character = {
        "Name": name,
        "Type": choose_character_type(),
        "Stats": {},
    }

    #we create a for statement to assign random int
    #for each respective stats
    for stat in stat_names:
        if stat == "Hit Points":
            character["Stats"][stat] = random.randint(20, 100)
        else:
            character["Stats"][stat] = random.randint(1, 20)

    return character

#create a function to display the character
def display_character(character):
    print("\n" + "=" * 36)
    print("       RANDOM CHARACTER")
    print("=" * 36)
    print(f"Name: {character['Name']}")
    print(f"Type: {character['Type']}")
    print("-" * 36)


    #we create a for loop, that goes
    #through character's stats dictionary
    #and prints it in a clean format
    for stat, value in character["Stats"].items():
        print(f"{stat:<15}: {value}")

    print("=" * 36)

#now we make a function that keeps asking
#the user yes or no
def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False

        print("Please enter yes or no...")

#now we make a function for the battle :O
def battle(character1, character2):
    #list for variables vvvvv
    fighters = [character1, character2]
    starting_hp = {
        fighter["Name"]: fighter["Stats"]["Hit Points"]
        for fighter in fighters
    }

    print(f"\n{character1['Name']} the {character1['Type']} faces "
          f"{character2['Name']} the {character2['Type']}!")

    round_number = 1

    while all(fighter["Stats"]["Hit Points"] > 0 for fighter in fighters):
        print(f"\n--- Round {round_number} ---")

        for attacker, defender in (
            (character1, character2),
            (character2, character1),
        ):
            if attacker["Stats"]["Hit Points"] <= 0:
                break #we put a break if the 
                      #battle is over

            #bonus stuff; character type affects
            #the amount of damage it dishes out
            type_bonus = {
                "Nordic Warrior": 5,
                "Void Assassin": 4,
                "Wood Elf": 3,
                "Water Mage": 3,
                "Pirate Ninja": 4,
            }
            damage = random.randint(1, 10) + type_bonus[attacker["Type"]]
            defender["Stats"]["Hit Points"]  -= damage 

            print(f"{attacker['Name']} attacks {defender['Name']} " 
                  f"for {damage} damage!")
            print(f"{defender['Name']} has "
                  f"{max(0, defender['Stats']['Hit Points'])} HP left.")

            if defender["Stats"]["Hit Points"] <= 0:
                break

            #We add a feat
            #20% chance to recover a small
            #amount of HP
            if random.random() < 0.20:
                healing = random.randint(5, 15)  
                defender["Stats"]["Hit Points"] = min(
                    starting_hp[defender["Name"]],
                    defender["Stats"]["Hit Points"] + healing,
                )
                print(f"{defender['Name']} finds a healing potion and "
                      f"recovers {healing} HP!")
                print (f"{defender['Name']} now has"
                       f"{defender['Stats']['Hit Points']} HP.")

        round_number += 1     
    if character1["Stats"]["Hit Points"] > 0:
        winner = character1
    else:
        winner = character2

    print(f"\n{winner['Name']} is the champion!")


#now we put the main function
def main():
    random_names = ["Shrek", "Dovakin", "Donkey",
                    "Luigi", "Excelsior", "Roar"] 
    print("Welcome to the Random Character Battle!")

    play_again = ask_yes_no("Would you like" \
    "to generate more characters and try again (y/n): ")

    while play_again:
        name = input(
            "\nEnter your character's name, or" \
            "press Enter for a generated name:"
        ).strip()

        if not name:
            name = random.choice(random_names) 

        #creates a list comprehension given 
        #that it's not the player's name
        #builds a new list
        player = generate_character(name)  
        opponent_name = random.choice(
            [random_name for random_name in random_names
             if random_name != name]
        )
        opponent = generate_character(opponent_name)

        display_character(player)
        print("\nYour opponent:")
        display_character(opponent)

        battle_again = ask_yes_no("\n" \
        "Would you like to battle again? (y/n): ")
        #create a while loop to battle again
        while battle_again:
            #Return both characters' health 
            #To max hp before battling again
            player["Stats"]["Hit Points"] = random.randint(20,100)
            opponent["Stats"]["Hit Points"] = random.randint(20, 100)
            print("\nThe characters' health is back to its original state.")
            battle(player, opponent)
            battle_again = ask_yes_no(
                "\nWould you like to make them battle again? (y/n): "
            )

        play_again = ask_yes_no(
            "\nWould you like to generate a set of fighters and play again? (y/n): "
        )

    print("\nThank you, farewell :) ")

if __name__ == "__main__":
    main()
                     
    




        

