from npcs import Npcs


def choice_right_for_the_forest(
    weapon: list, answer_weapon: list, skills_attacks: dict, spells_atacks: dict
) -> str:
    "This method prints the choices made by the user, killing a enemy, talking the right path in the forest"
    while True:
        weapons = weapon
        answer_of_the_weapon = answer_weapon
        skills = skills_attacks
        spells = spells_atacks
        election = input(
            "A big bat appears, Do you want to run or fight? (write run or fight) "
        ).lower()
        if election == "fight":
            enemy = Npcs()
            if answer_of_the_weapon == "book":
                for key, power in spells.items():
                    print("your attack is", key, "with power", power)
                enemy.npc_enemy_bat(spells)
                print("You continue and you find a new spell, Regeneration")
                spells["Regeneration"] = 80
                break
            elif answer_of_the_weapon == "sword":
                for key, power in skills.items():
                    print("your attack is", key, "with power", power)
                enemy.npc_enemy_bat(skills)
                print("You continue and you find a new chest armor")
                weapons.append("Chest Armor")
                break
            else:
                print("This option is not correct, the goblin kill you. Dumd ")
                break
        elif election == "run":
            print(
                "You run far away of the big bat and find a exit of the ruins, you find anything"
            )
            break
        else:
            print("This option is not correct, try again")


def choice_left_for_the_forest(
    weapon, answer_weapon: list, skills_attacks: dict, spells_atacks: dict, pets: list
) -> str:
    "This method prints the choices made by the user, killing a enemy, talking the left path in the forest"
    while True:
        weapons = weapon
        enemy_left = Npcs()
        pets = pets
        answer_of_the_weapon = answer_weapon
        skills = skills_attacks
        spells = spells_atacks
        election = input(
            "A goblin appears, Do you want to run or fight him? (write run or fight) "
        ).lower()
        if election == "fight":
            print()
            if answer_of_the_weapon == "book":
                for key, power in spells.items():
                    print("your attack is", key, "with power", power)
                enemy_left.npc_enemy_goblin(spells)
                print("You continue and find a new spell, Poison")
                spells["Posion"] = 900
                break
            elif answer_of_the_weapon == "sword":
                for key, power in skills.items():
                    print("your attack is", key, "with power", power)
                enemy_left.npc_enemy_goblin(skills)
                print("You continue and you find a shield")
                weapons.append("Shield")
                break
            else:
                print("This option is not correct, the goblin kill you. Dumd ")
                break
        elif election == "run":
            print(
                "You run far away of the goblin and find a exit of the ruins, you find a baby dog"
            )
            pets.append("Baby dog")
            break
        else:
            print("This option is not correct, try again")


def choice_left_for_the_cave(
    weapon, answer_weapon: list, skills_attacks: dict, spells_atacks: dict
) -> str:
    "This method prints the choices made by the user, killing a enemy, talking the left path in the cave"
    while True:
        weapons = weapon
        answer_of_the_weapon = answer_weapon
        skills = skills_attacks
        spells = spells_atacks
        election = input(
            "A big bat appears, Do you want to run or fight? (write run or fight) "
        ).lower()
        if election == "fight":
            enemy = Npcs()
            if answer_of_the_weapon == "book":
                for key, power in spells.items():
                    print("your attack is", key, "with power", power)
                enemy.npc_enemy_bat(spells)
                print("You continue and you find a new spell, Landslide")
                spells["Landslide"] = 490
                break
            elif answer_of_the_weapon == "sword":
                for key, power in skills.items():
                    print("your attack is", key, "with power", power)
                enemy.npc_enemy_bat(skills)
                print("You continue and you find a new warrior helmet")
                weapons.append("Warrior Helmet")
                break
            else:
                print("This option is not correct, the goblin kill you. Dumd ")
                break
        elif election == "run":
            print(
                "You run far away of the big bat and find a exit of the cave, you find a knife"
            )
            weapons.append("Knife")
            break
        else:
            print("This option is not correct, try again")


def choice_right_for_the_cave(
    weapon,
    answer_weapon: list,
    skills_attacks: dict,
    spells_atacks: dict,
    elements: list,
    pets: list,
) -> str:
    "This method prints the choices made by the user, killing a enemy, talking the right path in the cave"
    while True:
        element = elements
        weapons = weapon
        enemy_left = Npcs()
        pets = pets
        answer_of_the_weapon = answer_weapon
        skills = skills_attacks
        spells = spells_atacks
        election = input(
            "A big mouse appears, Do you want to run or fight him? (write run or fight) "
        ).lower()
        if election == "fight":
            print()
            if answer_of_the_weapon == "book":
                for key, power in spells.items():
                    print("your attack is", key, "with power", power)
                enemy_left.npc_enemy_goblin(spells)
                print(
                    "You continue and find a amulet that gives you a new element, Thunder"
                )
                element.append("Thunder")
                break
            elif answer_of_the_weapon == "sword":
                for key, power in skills.items():
                    print("your attack is", key, "with power", power)
                enemy_left.npc_enemy_goblin(skills)
                print("You continue and you find a shield")
                weapons.append("Shield")
                break
            else:
                print("This option is not correct, the goblin kill you. Dumd ")
                break
        elif election == "run":
            print(
                "You run far away of the big mouse and find a exit of the ruins, you find a baby bat"
            )
            pets.append("Baby bat")
            break
        else:
            print("This option is not correct, try again")
