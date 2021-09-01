class Npcs:
    """Class Npc contains all persons of the games, return dialogues and contain the information of the enemies"""

    def npc_lopez(self) -> str:
        return "Hi my name is Lopez"

    def npc_bartender(self, number_of_dialogue: int) -> str:  # continue later with her
        if number_of_dialogue == 1:
            print(
                " - Welcome advneturer to my tavern, Select one of the tasks on the wall"
            )
            print(
                " - I recomend you don't go to the Forest if you have the spell book and you element is fire and Don't go to the cave if you have the sword"
            )

        elif number_of_dialogue == 2:
            print("Select your task")

    def npc_old_men(self) -> str:
        return " - Hi adventurer, take this mape and go to that ruins. Good luck and I hope that you come back alive"

    def npc_enemy_bat(self, attack: dict) -> str:
        for key, power in attack.items():
            print("You kill the enemy with", key, ",you did", power, "damage")
