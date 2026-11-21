# Starting file for PROJECT 3
# Include your course number, student first and last name, and date in the comment header
#CS 31, josh lucero, 11-21-26

#here we import
import random

#function for random character type
def choose_character_type():
    """Choose a character type"""
    type_number = random.randint(1, 5)

    if type_number == 1:
        return "Nordic Warrior"
    elif type_number == 2:
        return "Void Assassin"
    elif type_number == 3:
        return "Wood Elf"
    elif type_number == 4:
        return "Water Mage"
    else:
        return "Pirate Ninja"

#now we make a function for generating a character
def generate_character(name):
    """Generate and makes a character with chosen name"""
    stat_names = [
        "Strength",
        "Intellect",
        "Hit Points",
        "Wisdom",
        "Charisma",
        "Dexterity"
    ]

    #for the character, key value pairs
    character = {
        "Name": name,
        "Type": choose_character_type(),
        "Stats": {}
    }

    #stat points rng
    for stat in stat_names:
        if stat == "Hit Points":
            character["Stats"][stat] = random.randint(20, 100)
        else:
            character["Stats"][stat] = random.randint(1,20)

    return character

#function for character's overall summary
def display_character(character):
    """Display the character's name, type, and stats."""
    print("\n" + "=" * 36)
    print("       YOUR RANDOM CHARACTER")
    print("=" * 36)
    print(f"Name: {character['Name']}")
    print(f"Type: {character['Type']}")
    print("-" * 36)

    for stat, value in character["Stats"].items():
        print(f"{stat:<15}: {value}")

    print("=" * 36)


#here we keep asking for the user's input to keep playing
def ask_yes_no(question):
    """Keep asking for users input"""
    while True:
        answer = input(question).strip().lower()

        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please enter y/n...")

#function for random alias
def main():
    random_names = ["Shrek", "Dovakin", "Donkey", "Luigi", "Excelsior", "Roar"]

    print("Welcome to the Random Character Generator!")

    create_another = ask_yes_no(
        "Would you like to generate a character? (yes/no):"
    )

    while create_another:
        name = input(
            "\nEnter a character name please... Or press Enter for a random name....:"
        ).strip()

        if not name:
            name = random.choice(random_names)

        character = generate_character(name)
        display_character(character)

        create_another = ask_yes_no(
            "\nWould you like to create another random character?!y/n?:"
        )
    print ("\nThanks for using the Random Character Generator!")

if __name__ == "__main__":
    main()