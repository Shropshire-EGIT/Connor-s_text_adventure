
import time

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
        
        'throne_room':{'name': 'Throne_room', 'north': 'Dining_hall', 'east': 'chest_room', 'west': 'Treasure_hall', 'south': 'opening', 'text': 'a large hall with a golden encrusted throne sat atop a pedestal.', 'contents': [], }, 
        
        'treasure_hall':{'name': 'treasure_hall', 'north': 'opening', 'east': 'throne_room', 'text': 'caskets full of jewels', 'contents': ['red_jewel', 'blue_jewel', 'green_jewel'], }, 
        
        'opening': {'name': 'opening', 'east': 'throne_room', 'south': 'treasure_hall', 'west': 'mountain_peak', 'text': 'an open area in the middle of nowhere.', 'contents': [], }, 
        
        'mountain_peak': {'name': 'mountain_peak', 'east': 'opening', 'south': 'graveyard', 'west': 'graveyard', 'text': 'the view is amazing up here. i would say it was roughly a 200ft drop.', 'contents': [], }, 
        
        'graveyard': {'name': 'graveyard', 'north': 'mountain_peak', 'west': 'mountain_peak', 'text': 'a graveyard with only 3 gravestones and a note', 'contents': [], }, 
        
        'opening2': {'name': 'opening', 'west': 'barn_attic', 'text': 'another opening, but with a sword in some stone', 'contents': [], }, 
        
        }

room_reset = rooms

directions = ['north',  'east',  'south',  'west', 'up', 'down']

###################################################################################


#defines the function used to display room context.
def user_look():
    print('\n' + current_room['name'])
    print('_' * len(current_room['name']) + '\n')
    print(current_room['text'])
    print('_' * len(current_room['text']) + '\n')
    print('in the room there is:')
    if len(current_room['contents']) >= 1:
        for s in current_room['contents']:
            print(s)
    else:
        print('there are no objects in this rooms')
#checks for which exits are available in each room.
def exit_check():
        if 'east' in current_room:
            print('east')
            time.sleep(1)
        if 'west' in current_room:
            print('west')
            time.sleep(1)
        if 'north' in current_room:
            print('north')
            time.sleep(1)
        if 'south' in current_room:
            print('south')
            time.sleep(1)
        if 'up' in current_room:
            print('up')
            time.sleep(1)
        if 'down' in current_room:
            print('down')
            time.sleep(1)

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
time.sleep(1)

print('you awake upon a bale of hay in a large, wooden barn.')

current_room = rooms['barn_ground']
gameloop = True
rock_broken = False
corridor_collapse = False

#main game loop####################################################################
while gameloop == True:
    while True:
    
        if len(inventory) > 10:
            time.sleep(1)
            print("\nyou're carrying too much.")
            print('what will you drop?')
            item = input(':')
            if item in inventory:
                current_room['contents'].append(item)
                inventory.remove(item)
                print('you have dropped ' + item)
                rounddone = True
            else:
                print(item + ' is not in your inventory')
                rounddone = True
        
        
        rounddone = False
        text = current_room['text']
    
        command = input(user_input)
        command = command.lower()

        if len(command) == 1:
            if command in 'e':
                command = 'east'
                rounddone = True

            if command in 'w':
                command = 'west'
                rounddone = True

            if command in 's':
                command = 'south'
                rounddone = True

            if command in 'n':
                command = 'north'
                rounddone = True

            if command in 'u':
                command = 'up'
                rounddone = True

            if command in 'd':
                command = 'down'
                rounddone = True
        
            if command in 'i':
                command = 'inventory'
                rounddone = True
    
        if 'look' in command.lower():
            user_look()
            rounddone = True

        elif command.lower() in ('q', 'quit',):
            print('goodbye')
            rounddone = True
            break
            
    
        if current_room['name'] == 'corridor':
            if 'east' in command:
                if 'torch' in inventory:
                    print('the torchlight reveals ancient scriptures on the wall:')
                    rounddone = True
                elif 'torch' not in inventory:
                    print('are you sure you want to continue without the torch?')
                    command = input(':').lower()
                    if command in ('yes', 'y'):
                            print('you trip in the dark and die')
                            rounddone = True
                            break
                    elif command in ('no', 'n'):
                        print('wise decision')
                        current_room = rooms['corridor']
                        rounddone = True
                
        elif command.lower() in directions:
            if command in current_room:
                current_room = rooms[current_room[command]]
                print(current_room['name'])
                rounddone = True
            else:
                print("You can't go that way.")
                rounddone = True
    
        if len(command) > 0:
            if command.lower().split()[0] in ('get', 'take'):
                if len(command) - len(command.split()[0]) >= 1:
                    item = command.lower().split()[1]
                    if item in ('bale', 'hay', 'chest', 'throne', 'door'):
                        print('the ' + item + ' is too heavy')
                        rounddone = True
                    elif item in current_room['contents']:
                        current_room['contents'].remove(item)
                        inventory.append(item)
                        print(item + ' is now in your inventory')
                        rounddone = True
                    else:
                        print(item + ' is not in the room')
                        rounddone = True
                else:
                    print("i don't know what you want me to " + command.split()[0])
                    rounddone = True
    
        if len(command) > 0:
            if command.lower().split()[0] == 'drop':
                if len(command) - len(command.split()[0]) >= 1:
                    item = command.lower().split()[1]
                    if item in inventory:
                        current_room['contents'].append(item)
                        inventory.remove(item)
                        print(' you have dropped ' + item)
                        rounddone = True
                    else:
                        print(item + ' is not in your inventory')
                        rounddone = True
                else:
                    print("i don't know what you want me to drop")
                    rounddone = True
        
        
        if 'inventory' in command.lower():
            for s in inventory:
                print(s)
            rounddone = True
    
        if 'exits' in command.lower():
            exit_check()
            rounddone = True
    
        if 'read' in command and current_room['name'] == 'graveyard':
            if command.split()[1] == 'gravestones':
                print('On the first is: Elliot Barnster, died at 23 after being hit by a bus.')
                time.sleep(1)
                print('On the second is: Jane Watson, died at 51.') 
                time.sleep(1)
                print('On the third is: Harry McSquire, died at 87. He will be missed.')
                rounddone = True
            
            if command.split()[1] == 'note':
                print('The note reads: 2 of us died in our prime, one of us did not.')
                time.sleep(1)
                print('Guess the grave I lie in, and you can have the lot.')
                rounddone = True    

        if 'dig' in command:
            if current_room['name'] == 'graveyard':
                if 'shovel' in inventory:
                    if '2' in command:
                        time.sleep(1)
                        print('you chose wisely')
                        print('now use my number open your treasure')
                        time.sleep(1)
                        inventory.append('a rock')
                        rounddone = True
                    elif '1' in command or '3' in command:
                        print('you chose unwisely.')
                        time.sleep(1)
                        print('hahaha')
                        break
                    else:
                        print('which one?')
                        command = input(':').lower()
                        if '2' in command:
                            time.sleep(1)
                            print('you chose wisely')
                            print('now use my number open your treasure')
                            time.sleep(1)
                            inventory.append('a rock')
                            rounddone = True
                        elif '1' in command or '3' in command:
                            print('you chose unwisely.')
                            time.sleep(1)
                            print('hahaha')
                            break
                else:
                    print('you would need a shovel to do that')
            else:
                print('it would be stupid to dig here')
        if 'open' in command:
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
                    if 'no' in command:
                        print('you leave the rock tumbler')
                        current_room['contents'].append('rock_tumbler')
                        rounddone = True
                else:
                    print('wrong combination')
                    rounddone = True
            if current_room['name'] == 'barn_attic':
                print('you attempt to open the door')
                time.sleep(1)
                if 'key' in inventory:
                    print('you use your key to open the door')
                    current_room['east'] = 'opening2'
                    rounddone = True
                    inventory.remove('key')
                    rounddone = True
                else:
                    print('you do not have the key')
                    rounddone = True
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
                    elif command in ('n', 'no'):
                        print('you drop the tunic')
                        current_room['contents'].append('leather_tunic')
                    else:
                        print('ok')
                        current_room['contents'].append('leather_tunic')
                elif 'key' in inventory:
                    print('you do not possess the correct key')
                else:  
                    print('they are locked shut')
            else:
                print('there is nothing to open here')
        
        if 'use' in command:
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

               
    
        #######################
        elif rounddone == False:
            print("sorry, i didn't understand that.")
            rounddone = True
    
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


