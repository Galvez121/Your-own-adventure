# This is my adventure. Select the options and enjoy
from npcs import Npcs  # The module NPC contains the npc of this game
import random
import elections

# Weather and envioronment

ENVIROMENT = ("windy", "sunny", "rainy", "cloudy")
random_weather = random.choice(ENVIROMENT)

# Make you player
your_name = input("What is your adventorous name? ")

# ist of habilities
elements_control = []

# List of my stuff(inventory)
pets = []
elements = []
weapons = []
spells = {}
skills = {}
health = 4

# Enemies
ENEMIES = ["goblin", "big bat", "big mouse"]

print(
    "Hi Adventorous",
    your_name,
    "and welcome to this history, your mision is end you day alives",
)

answer_of_the_element = input(
    "You have to select one of this two elements control, fire or water. Which elements do you want to control? (fire/water) "
).lower()

# Here you select your element
while True:
    if answer_of_the_element == "fire":
        elements.append("fire")
        elements_control.append("fire")
        spells[
            "fire ball"
        ] = 600  # This is a spell for the magic book, the number is the power
        skills["fire cut"] = 500
        print("You select fire control.")
        break

    elif answer_of_the_element == "water":
        elements.append("water")
        elements_control.append("water")
        spells[
            "water ball"
        ] = 500  # This is a spell for the magic book, the number is the power
        skills["water movement"] = 600
        print("You select water control.")
        break

    else:
        print("You have to select fire or water. This option is wrong. You lose")
        quit()

# Here you select your weapon
# The class NPC contains the npcs of this game

dialogue = Npcs()

print(dialogue.npc_lopez())
while True:
    answer_of_the_weapon = input(
        "Each new warrior needs to select one of these weapons magic sword or spell book. Select one \nwrite sword or book "
    ).lower()

    if answer_of_the_weapon == "book":
        weapons.append("spell book")
        print("You select a spell book.")
        print()
        break
    elif answer_of_the_weapon == "sword":
        weapons.append("magic sword")
        print("You select a magic sword.")
        print()
        break
    else:
        print("You have to select book or sword. This option is wrong. You lose")
        quit()

print(
    "Your profile is done.\nYour element:",
    elements_control[0],
    "\nYour weapon:",
    weapons[0],
)
print()

# Here start the history
print("Today the weather is", random_weather)
print(
    "Welcome new adventurer this is your first day in this world\nGo to the tavern and select your task"
)
print()

dialogue.npc_bartender(1)  # Number of the dialogue that you want to output

election_forest_cave = input(
    "Where do you want to go? To the Forest or The Cave\nWrite forest or cave "
).lower()

# Forest
if election_forest_cave == "forest":
    while health >= 0:
        print(
            "You enter the forest and you find a old men, do you want to talk with him or do you want to continue on your way"
        )
        election = input("Write talk or continue ").lower()
        print()
        random_enemy = random.choice(ENEMIES)
        if election == "continue":
            print(
                "You continue and then you get lose and you are hurt by a",
                random_enemy,
            )
            health -= 1
            print("You come back and you decide to talk with the old men")
            print()
            print(dialogue.npc_old_men())
            your_choice = input(
                "Do you want to go to the ruins or do you want to continue\nWrite go or continue "
            ).lower()
            print()
            if your_choice == "continue":
                print(
                    "You continue and then you get lose and you are hurt by a",
                    random_enemy,
                )
                health -= 1
                print("You are so dumb, Please go to the ruins")
                print()
                your_choice = input(
                    "Do you want to go to the rouins or do you want to continue\nWrite go or continue "
                ).lower()
                if your_choice == "continue":
                    print("You die for a", random_enemy)
                    health -= 3
                elif your_choice == "go":
                    election = input(
                        "You enter and there are two ways, left and right.\nWhere do you want to go? (write left or right) "
                    ).lower()

                    if election == "right":
                        elections.choice_right_for_the_forest(
                            weapons, answer_of_the_weapon, skills, spells
                        )
                        break
                    elif election == "left":
                        elections.choice_left_for_the_forest(
                            weapons, answer_of_the_weapon, skills, spells, pets
                        )
                        break

                    else:
                        print(
                            "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
                        )
                        health -= 4
            elif your_choice == "go":
                election = input(
                    "You enter and there are two ways, left and right.\nWhere do you want to go? (write left or right) "
                ).lower()

                if election == "right":
                    elections.choice_right_for_the_forest(
                        weapons, answer_of_the_weapon, skills, spells
                    )
                    break
                elif election == "left":
                    elections.choice_left_for_the_forest(
                        weapons, answer_of_the_weapon, skills, spells, pets
                    )
                    break

                else:
                    print(
                        "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
                    )
                    health -= 5

        elif election == "talk":
            print(dialogue.npc_old_men())
            your_choice = input(
                "Do you want to go to the ruins or do you want to continue\nWrite go or continue "
            ).lower()
            print()
            if your_choice == "continue":
                print(
                    "You continue and then you get lose and you are hurt by a",
                    random_enemy,
                )
                health -= 1
                print("You are so dumb, Please go to the ruins")
                print()
                your_choice = input(
                    "Do you want to go to the rouins or do you want to continue\nWrite go or continue "
                ).lower()
                if your_choice == "continue":
                    print("You die for a", random_enemy)
                    health -= 2

            elif your_choice == "go":
                election = input(
                    "You enter and there are two ways, left and right.\nWhere do you want to go? (write left or right) "
                ).lower()

                if election == "right":
                    elections.choice_right_for_the_forest(
                        weapons, answer_of_the_weapon, skills, spells
                    )
                    break
                elif election == "left":
                    elections.choice_left_for_the_forest(
                        weapons, answer_of_the_weapon, skills, spells, pets
                    )
                    break

                else:
                    print(
                        "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
                    )
                    health -= 4
                    break
        else:
            health -= 4

# Cave
elif election_forest_cave == "cave":
    print("You go into the cave and a witch appears, and she says:")
    dialogue.witch_npc(your_name, 1)
    while True:
        election = input(
            "You enter to the cave and find two ways, left and right.\nWhere do you want to go? (write left or right) "
        ).lower()
        if election == "right":
            elections.choice_right_for_the_cave(
                weapons, answer_of_the_weapon, skills, elements, spells, pets
            )
            break
        elif election == "left":
            elections.choice_left_for_the_cave(
                weapons, answer_of_the_weapon, skills, spells
            )
            break

        else:
            print(
                "You wrote the election wrong or the option is not in the options... You DIE! Dumd"
            )
            break
else:
    print("This option is not valid")

if health <= 0:
    print("You lost")

empty_list = []

# Here is your inventory in the end that his output will be in other file


def inventory_file():
    "Make a ner file .txt with your inventory in the end of the history"
    with open("YourInventory.txt", "a") as file:
        if answer_of_the_weapon == "sword":
            if pets == empty_list:
                pets.append("You don't find any pet")
            file.write(
                """\n******************************************\n/Your end the history with this inventory/\n******************************************
                \n"""
                + "\nYour skill is: "
                + str(skills)
                + "\nYour pet is: "
                + str(pets)
                + "\nYour inventory is "
                + str(weapons)
                + "\nYour health is: "
                + str(health)
                + "\nYou control this element:"
                + str(elements)
                + "\n"
            )
        elif answer_of_the_weapon == "book":
            if "Baby dog" not in pets:
                pets.append("You don't find any pet")
            file.write(
                """\n******************************************\n/Your end the history with this inventory/\n******************************************
                \n"""
                + "\nYour spell is: "
                + str(spells)
                + "\nYour pet is: "
                + str(pets)
                + "\nYour inventory is "
                + str(weapons)
                + "\nYour health is: "
                + str(health)
                + "\nnYou control this element:"
                + str(elements)
                + "\n"
            )
        else:
            file.write("Error ")


inventory_file()
print("The end")
