"""Class Npc contains all persons of the games"""


class Npcs:
    def npc_lopez(self):
        return "Hi my name is Lopez"

    def npc_bartender(self, number_of_dialogue):  # continue later with her
        if number_of_dialogue == 1:
            print(
                " - Welcome advneturer to my tavern, Select one of the tasks on the wall"
            )
            print(
                " - I recomend you don't go to the Forest if you have the spell book and you element is fire and Don't go to the cave if you have the sword"
            )

        elif number_of_dialogue == 2:
            print("Select your task")

    def npc_old_men(self):
        return " - Hi adventurer, take this mape and go to that ruins. Good luck and I hope that you come back alive"

    def npc_enemy_bat(attack):
        health = 500
        if skills["fire ball"] > health:  # This is not ready yet
            print("nice")
        else:
            print("bad")
