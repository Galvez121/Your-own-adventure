from npcs import Npcs


def choice_right_for_the_forest(
    weapon: list, skills_attacks: dict, spells_atacks: dict
) -> str:
    "This method prints the choices made by the user, killing a enemy, talking the right path"
    while True:
        answer_of_the_weapon = weapon
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
                print("You continue and you find a new spell")
                break
            elif answer_of_the_weapon == "sword":
                for key, power in skills.items():
                    print("your attack is", key, "with power", power)
                enemy.npc_enemy_bat(skills)
                print("You continue and you find a new chest armor")
                break
        elif election == "run":
            pass


def choice_left_for_the_forest(
    weapon: list, skills_attacks: dict, spells_atacks: dict
) -> str:
    pass
