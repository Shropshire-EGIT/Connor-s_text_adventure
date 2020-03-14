    
import time
from definitions import *
from random import randint

#classes

#creates the base model for an enemy
class Enemy():
    def __init__(self, name, damage):
        self.name = name
        self.damage = int(damage)


#sets the users inventory to empty.

inventory = []

#shows which rooms can be access from eachother

rooms = {'barn_attic': {'name': 'barn_attic', 'down': 'barn_ground', 'text': 'a small attic with a door', 'contents': ['shovel'],},
        'barn_ground': {'name': 'barn_ground', 'up': 'barn_attic', 'east': 'east_field', 'west': 'west_field', 'text': 'you are in a large wooden barn.', 'contents': [], },
        'east_field': {'name': 'east_field', 'west': 'barn_ground', 'south': 'behind_barn', 'text': 'a large, open field with lots of crops', 'contents': ['crops'], },
        'west_field': {'name': 'west_field', 'east': 'barn_ground', 'south': 'behind_barn', 'text': 'a large, open field.', 'contents': ['crops'], },
        'behind_barn':{'name': 'behind_barn', 'east': 'east_field', 'west': 'west_field', 'north': 'corridor', 'text': 'behind the large barn, there is a corridor to the north here', 'contents': [], },
        'corridor':{'name': 'corridor', 'south': 'behind_barn', 'east': 'cell_room', 'text': 'you are at the entrance to a slim, stone corridor heading to the east.', 'contents': ['torch'], }, 
        'cell_room':{'name':'cell_room', 'west': 'corridor', 'north': 'cavern', 'east': 'dining_hall', 'text':  'a large room with many cells, one of which contains a serpent guarding a helmet.', 'contents': [], },
        'dining_hall': {'name': 'dining_hall', 'west': 'cell_room', 'south': 'throne_room', 'text': 'a large hall used for dining', 'contents': [], },
        'cavern': {'name': 'cavern', 'north': 'cavern', 'east': 'chest_room', 'south': 'cell_room', 'text': "it's just a cavern", 'contents': [], },
        'chest_room': {'name': 'chest_room', 'east': 'throne_room', 'west': 'cavern', 'text': 'a small room with a chest in the the centre.', 'contents':[], },
        'throne_room':{'name': 'Throne_room', 'north': 'Dining_hall', 'east': 'chest_room', 'west': 'treasure_hall', 'south': 'opening', 'text': 'a large hall with a golden encrusted throne sat atop a pedestal.', 'contents': [], }, 
        'treasure_hall':{'name': 'treasure_hall', 'north': 'opening', 'east': 'throne_room', 'text': 'caskets full of jewels', 'contents': ['circular_jewel', 'triangluar_jewel', 'square_jewel'], }, 
        'opening': {'name': 'opening', 'east': 'throne_room', 'south': 'treasure_hall', 'west': 'mountain_peak', 'text': 'an open area in the middle of nowhere.', 'contents': [], }, 
        'mountain_peak': {'name': 'mountain_peak', 'east': 'opening', 'south': 'graveyard', 'west': 'graveyard', 'text': 'the view is amazing up here. i would say it was roughly a 200ft drop.', 'contents': [], }, 
        'graveyard': {'name': 'graveyard', 'north': 'mountain_peak', 'west': 'mountain_peak', 'text': 'a graveyard with only 3 gravestones and a note', 'contents': [], }, 
        'opening2': {'name': 'opening', 'west': 'barn_attic', 'text': 'another opening, but with a sword in some stone', 'contents': [], }, 
        }

room_reset = rooms

gravedug = False

directions = ['north',  'east',  'south',  'west', 'up', 'down']

###################################################################################
#starting text and variables
if 1 == 1:
    user_input = '\n'':'
    print('\n' * 2)

    name = str(input("Hi, what's your name? "))
    welcome = str('hello, ' + name)

    print('\n' * 2)
    print(welcome)
    print('*' * len(welcome))

    print('welcome to my prototype of my text adventure game')
    print('enter commands to control your character')
    print('type exits to view the exits for each room you are in' + '\n' * 2)
    print('type help for list of commands')
    time.sleep(1)

    print('you awake upon a bale of hay in a large, wooden barn.')

    current_room = rooms['barn_ground']
    gameloop = True
    rock_broken = False
    corridor_collapse = False

#main game loop####################################################################
while gameloop == True:
    while True:
        dead = False

        #limits the amount of objects in the inventory
        if len(inventory) > 10:
            inventory_check(inventory, current_room)
        
        
        rounddone = False
        text = current_room['text']
    
        command = input(user_input)
        command = command.lower()

        #command conversion from single letter to a word
        if len(command) == 1:
                if command in 'e':
                    command = 'east'
                if command in 'w':
                    command = 'west'
                if command in 's':
                    command = 'south'
                if command in 'n':
                    command = 'north'
                if command in 'u':
                    command = 'up'
                if command in 'd':
                    command = 'down'
                if command in 'i':
                    command = 'inventory'
        
        #calls the look block
        elif 'look' in command.lower():
            user_look(current_room)
            rounddone = True

        #story section - corridor w/ no torch
        if current_room['name'] == 'corridor' and 'east' in command:
            torchcheck(command, inventory, rooms, current_room, dead)
            rounddone = True
        
        #player movement       
        if command.lower() in directions:
            if command in current_room:
                current_room = rooms[current_room[command]]
                print(current_room['name'])
                rounddone = True
            else:
                print("You can't go that way.")
                rounddone = True
    
        #enemy combat
        if 'enemy' in current_room:
            combat_script()
        
        #developer section
        if len(command) > 1:
            if command.split()[0] == 'dev' and name == 'connor':
                try:
                    devcom = command.split()[1]
                    if devcom == 'tp':
                        try:
                            current_room = rooms[command.split()[2]]
                            print(current_room['name'])
                        except:
                            print('you have not specified your tp location')
                    elif devcom == 'gain':
                        try:
                            inventory.append(command.split()[2])
                            print(command.split()[2] + 'has been added, creator')
                        except:
                            print('what did you want?')
                except:
                    print('sorry, i dont know what you want me to do')
        
        #all verb commands
        elif len(command) > 1:
            #story section - opening the chest + open command scipt
            if command.split()[0] == 'open':
                openscript(command, inventory, current_room, rounddone, user_input)
            #the script for when the user wants to use an object in inventory
            elif command.split()[0] == 'use':
                usescript(command, inventory, rock_broken)
            #calls the insert script
            elif command.split()[0] == 'insert':
                insertcript(command, inventory, current_room, Enemy)
            #story section - graveyard dig
            elif command.split()[0] == 'dig':
                digscript(command, current_room, inventory, dead, gravedug)
            #story section - graveyard riddle
            elif command.split()[0] == 'read':
                readcript(command, current_room)
            #calls the take and get script
            elif command.split()[0] == 'get' or 'take':
                takescript(command, inventory, rooms, current_room)
            #calls the drop script
            elif command.split()[0] == 'drop':
                dropscript(command, inventory, rooms, current_room)
            #script for looking
            elif command.split()[0] == 'look':
                user_look(current_room)
            #prints the items from the inventory
            elif command.split()[0] == 'inventory':
                for s in inventory:
                    print(s)
            #gives the user help
            elif command.split()[0] == 'help':
                print('type look to display room and its description.')
                print('type take or get to pick up an object.')
                print('type i or inventory to view your current objects')
                print('type east, west, north, south, up or down to go in that direction.')



            rounddone = True
        

        if current_room['name'] == 'east_field':
            if 'crops' not in current_room['contents']:
                current_room['contents'].append('crops')
        

        #developer section
        if len(command) > 1:
            if command.split()[0] == 'dev' and name == 'connor':
                try:
                    devcom = command.split()[1]
                    if devcom == 'tp':
                        try:
                            current_room = rooms[command.split()[2]]
                            print(current_room['name'])
                        except:
                            print('you have not specified your tp location')
                    elif devcom == 'gain':
                        try:
                            inventory.append(command.split()[2])
                            print(command.split()[2] + 'has been added, creator')
                        except:
                            print('what did you want?')
                except:
                    print('sorry, i dont know what you want me to do')
        
    
        #######################
        elif rounddone == False:
            print("sorry, i didn't understand that.")
            rounddone = True
        
        if dead == True:
            break

        #allows the user to exit/quit
        if command.lower() in ('q', 'quit',):
            print('goodbye')
            rounddone = True
            break
    
    print('try again?')
    command = input(':')
    if 'yes' in command:
        print('good')
        time.sleep(1)
        print('you awake upon a bale of hay in a large, wooden barn.')
        current_room = rooms['barn_ground']
        inventory = []
        rooms = room_reset
    else:
        print('ok. \ngoodbye')
        break

