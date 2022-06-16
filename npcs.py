class Npcs:
    """Class Npc contains all the people in the games, return dialogues and contain the information of the enemies, as well"""

    def npc_lopez(self) -> str:
        return "Hi my name is Lopez"

    def npc_bartender(self, number_of_dialogue: int) -> str:  # continue later with her
        if number_of_dialogue == 1:
            print(
                " - Welcome advneturer to my tavern, Select one of the tasks on the wall"
            )
            print(
                " - I recomend you don't go to the Forest if you have the spell book and your element is fire. Also, Don't go to the cave if you have the sword"
            )

        elif number_of_dialogue == 2:
            print("Select your task")

    def npc_old_men(self) -> str:
        return " - Hi adventurer, take this mape and go to that ruins. Good luck and I hope that you come back alive"

    def witch_npc(self, name: str, number_of_dialogue: int) -> str:
        your_name = name
        if number_of_dialogue == 1:
            print(
                "You must be",
                your_name,
                "my eye tells me that you will come here. Enter to the cave and good luck.",
            )
        else:
            print("Error, Dialogue has not been't difined")

    def npc_enemy_bat(self, attack: dict) -> str:
        for key, power in attack.items():
            print("You killed the enemy with", key, ",you did", power, "damage")

    def npc_enemy_goblin(self, attack: dict) -> str:
        for key, power in attack.items():
            print("You killed the enemy with", key, ",you did", power, "damage")

    def npc_enemy_big_mouse(self, attack: dict) -> str:
        for key, power in attack.items():
            print("You killed the enemy with", key, ",you did", power, "damage")
