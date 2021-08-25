# Tis is my adventure. Select the options and enjoy
from npcs import Npcs  # The module NPC contains the npc of this game
import random

# Weather and envioronment

ENVIROMENT = ("windy", "sunny", "rainy", "cloudy")

# Make you player
player = input("What is your adventorous name? ")

# ist of habilities
elements_control = []

# List of my stuff(inventory)
weapons = []
spells = {}
skills = {}
health = 4

# Enemies
enemis = ["goblin", "big bat", "big mouse"]

print(
    "Hi Adventorous",
    player,
    "and welcome to this history, your mision is become The warrior king",
)

answer_of_the_element = input(
    "You have to select one of this two elements control, fire or water. What of those do you want to control? (fire/water) "
).lower()

# Here you select your element
while True:
    if answer_of_the_element == "fire":
        elements_control.append("fire")
        spells[
            "fire ball"
        ] = 600  # This is a spell for the magic book, the number is the power
        skills["fire cut"] = 400
        print("You select fire control.")
        break

    elif answer_of_the_element == "water":
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
print(
    "Welcome new adventorous this is your first day in this world\nGo to the tavern and select your task"
)
print()


# Forest
while health >= 0:
    print(
        "You enter the forest and you find a old men, do you want to talk with him or do you want to continue your way"
    )
    election = input("Write talk or continue ").lower()
    print()
    random_election = random.choice(enemis)
    if election == "continue":
        print(
            "You continue and then you lose yourself and you are hurt by a",
            random_election,
        )
        health -= 1
        print("You come back and you decide to talk with the old men")
        print()
        print(dialogue.npc_old_men())
        your_choice = input(
            "Do you want to go to the rouins or do you want to continue\nWrite go or continue "
        ).lower()
        print()
        if your_choice == "continue":
            print(
                "You continue and then you lose yourself and you are hurt by a",
                random_election,
            )
            health -= 1
            print("You are so dumb, Please go to the rouins")
            print()
            your_choice = input(
                "Do you want to go to the rouins or do you want to continue\nWrite go or continue "
            ).lower()
            if your_choice == "continue":
                print("You die for a", random_election)
                health -= 3
    elif election == "talk":
        print(dialogue.npc_old_men())

    else:
        health -= 4

if health <= 0:
    print("You lost")


# Here is the radom weather (Work with this later)
random_election = random.choice(ENVIROMENT)

print(random_election)
print("The end")
