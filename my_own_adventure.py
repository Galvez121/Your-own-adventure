#this is my adventure. Select the options and enjoy
#The module NPC contains the npc of this game
import npcs

player = input("What is your adventorous name? ")

#List of habilities
elements_control = []

#List of my stuff(inventory)
weapons = []

print('Hi Adventorous',player, 'and welcome to this history, your mision is become The warrior king')

answer_of_the_element = input('You have to select one of this two elements control, fire or water. What of those do you want to control? (fire/water) ').lower()

#Here you select your element
while True:
    if answer_of_the_element == 'fire':
        elements_control.append('fire')
        print("You select fire control.")
        break

    elif answer_of_the_element == 'water':
        elements_control.append('water')
        print("You select water control.")
        break
    
    else:
        print('You have to select fire or water. This option is wrong. You lose')
        quit()
            
#Here you select your weapon
#The module NPC contains the npc of this game

print('Hi my name is',npcs.lopez()) 
while True:
    answer_of_the_weapon = input('Each new warrior needs to select one of these weapons magic sword or spell book. Select one \nwrite sword or book ').lower()

    if answer_of_the_weapon == 'book':
        weapons.append('spell book')
        print("You select a spell book.")
        print()
        break
    elif answer_of_the_weapon == 'sword':
        weapons.append('magic sword')
        print("You select a magic sword.")
        print()
        break
    else:
        print('You have to select book or sword. This option is wrong. You lose')
        quit()
        
print('Your profile is done.\nYour element:',elements_control[0],'\nYour weapon:',weapons[0])
print('The end')
