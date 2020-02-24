
import time
from definitions import *

#classes

#creates the base model for an enemy
class Enemy():
    def __init__(self, name, hp, damage, room):
        self.name = name
        self.hp = int(hp)
        self.damage = int(damage)
        self.room = room

#creates the enemies themselves
serpent = Enemy('Serpent', 10, 1, 'opening')

#sets the users inventory to empty.

inventory = []

#shows which rooms can be access from eachother

rooms = {'barn_attic': {'name': 'barn_attic', 'down': 'barn_ground', 'text': 'a small attic with a door', 'contents': ['shovel'], },
        'barn_ground': {'name': 'barn_ground', 'up': 'barn_attic', 'east': 'east_field', 'west': 'west_field', 'text': 'you are in a large wooden barn.', 'contents': [], },
        'east_field': {'name': 'east_field', 'west': 'barn_ground', 'south': 'behind_barn', 'text': 'a large, open field with lots of crops', 'contents': ['crops'], },
        'west_field': {'name': 'west_field', 'east': 'barn_ground', 'south': 'behind_barn', 'text': 'a large, open field.', 'contents': ['crops'], },
        'behind_barn':{'name': 'behind_barn', 'east': 'east_field', 'west': 'west_field', 'north': 'corridor', 'text': 'behind the large barn, there is a corridor to the north here', 'contents': [], },
        'corridor':{'name': 'corridor', 'south': 'behind_barn', 'east': 'cell_room', 'text': 'you are at the entrance to a slim, stone corridor heading to the east.', 'contents': ['torch'], }, 
        'cell_room':{'name':'cell_room', 'west': 'corridor', 'north': 'cavern', 'east': 'dining_hall', 'text':  'a large room with many cells, some including skeletons.', 'contents': [], },
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
        
        
        
        #tells the user their inventory
        if 'inventory' in command.lower():
            for s in inventory:
                print(s)
            rounddone = True
        
        #calls the look block
        elif 'look' in command.lower():
            user_look(current_room)
            rounddone = True

        #allows the user to exit/quit
        elif command.lower() in ('q', 'quit',):
            print('goodbye')
            rounddone = True
            break
            
        #story section - corridor w/ no torch
        elif current_room['name'] == 'corridor' and 'east' in command:
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
    
        #calling the taking or dropping scripts
        elif len(command) > 0 and rounddone == False:
            if 'take' or 'get' in command:
                takescript(command, inventory, rooms, current_room)
                rounddone = True
            elif 'drop' in command:
                dropscript(command, inventory, rooms, current_room)
                rounddone = True
    
        #story section - graveyard riddle
        elif 'read' in command:
            readcript(command, current_room)
            rounddone = True

        #story section - graveyard dig
        elif 'dig' in command:
            digscript(command, current_room, inventory, dead, gravedug)
            rounddone = True
        
        #story section - opening the chest + open command scipt
        elif len(command) > 1:
            if command.split()[0] == 'open':
                if current_room['name'] == 'chest_room':
                    print('what is the lock combination')
                    combination = input(':')
                    if combination == '51': 
                        print('you open the chest')
                        time.sleep(1)
                        print('you find a rock tumbler')
                        print('keep it?')
                        command = input(':').lower()
                        if 'yes' in command:
                            print('you take the rock tumbler')
                            inventory.append('rock_tumbler')
                            rounddone = True
                            opened = True
                        if 'no' in command:
                            print('you leave the rock tumbler')
                            current_room['contents'].append('rock_tumbler')
                            rounddone = True
                    else:
                        print('wrong combination')
                        rounddone = True
                        opened = True
                if current_room['name'] == 'barn_attic':
                    print('you attempt to open the door')
                    time.sleep(1)
                    if 'key' in inventory:
                        print('you use your key to open the door')
                        current_room['east'] = 'opening2'
                        rounddone = True
                        inventory.remove('key')
                        opened = True
                    else:
                        print('you do not have the key')
                        rounddone = True
                        opened = True
                if current_room['name'] == 'cell_room':
                    print('you attempt to open one of the cell doors')
                    time.sleep(1)
                    if 'cell_key' in inventory:
                        print('you manage to open one of the cell doors.')
                        print('the key was too fragile and broke before you could take it')
                        print('there is a tunic here')
                        print('take it?')
                        command = (user_input)
                        if command in ('y', 'yes'):
                            print('you put the tunic on immediatly')
                            inventory.append('leather_tunic')
                            rounddone = True
                            opened = True
                        elif command in ('n', 'no'):
                            print('you drop the tunic')
                            current_room['contents'].append('leather_tunic')
                            rounddone = True
                            opened = True
                        else:
                            print('ok')
                            current_room['contents'].append('leather_tunic')
                            rounddone = True
                            opened = True
                    elif 'key' in inventory:
                        print('you do not possess the correct key')
                        rounddone = True
                        opened = True
                    else:  
                        print('they are locked shut')
                        rounddone = True
                        opened = True
                elif rounddone != True:
                    print('there is nothing to open here')
        
        #the script for when the user wants to use an object in inventory
        elif 'use' in command:
            if 'rock_tumbler' in command:
                if 'rock_tumbler' and 'a rock' in inventory and rock_broken == False:
                    print('you place the rock in your rock rumbler')
                    time.sleep(2)
                    print('opening the tumbler, you find an old, rusty key')
                    inventory.remove('a rock')
                    inventory.append('key')
                    rock_broken = True
                    rounddone = True
                elif 'rock' not in inventory:
                    print('you cannot use the rock tumbler with a rock')
                    rounddone = True
                elif rock_broken == True:
                    print('unfortunatley, the rock tumbler broke when you used it')
                    rounddone = True
            else:
                print('you cannot use anything here')
        
        if current_room['name'] == 'east_field':
            if 'crops' not in current_room['contents']:
                current_room['contents'].append('crops')
        
        elif 'help' in command:
            print('type look to display room and its description.\ntype take or get to pick up an object.\ntype i or inventory to view your current objects\ntype east, west, north, south, up or down to go in that direction.')

        #story section - placing the circular jewel into the sword
        elif 'insert' in command:
            if current_room['name'] == 'opening' and 'circular_jewel' in command:
                if 'circular_jewel' in inventory:
                    print('you insert the jewel into the hilt of the sword.')
                    print('the stone surrounding the sword breaks apart, revealing a long, silver broadsword')
                    inventory.append('silver_broadsword')
                    current_room['text'] = 'another opening, but with segments of stone scattered around.'
                elif 'circular_jewel' not in inventory:
                    print('you cannot place what do you do not have')
            else:
                print('no')
        
        #developer section
        elif len(command) > 1:
            if command.split()[0] == 'dev' and name == 'connor':
                try:
                    devcom = 'hi'
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

