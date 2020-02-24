import time



#displays the current room of the player
def user_look(current_room):
    print('\n' + current_room['name'])
    print('_' * len(current_room['name']) + '\n')
    print(current_room['text'])
    print('_' * len(current_room['text']) + '\n')
    if len(current_room['contents']) >= 1:
        print('in the room there is:')
        for s in current_room['contents']:
            print(s)
            time.sleep(1)
    else:
        print('there are no obtainable objects in this room')
    
    print('there are exits to the:')
    #checks for which exits are available in each room.
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

def inventory_check(inventory, current_room,):
    if len(inventory) > 10:
        time.sleep(1)
        print("\nyou're carrying too much.")
        print('what will you drop?')
        item = input(':')
        if item in inventory:
            current_room['contents'].append(item)
            inventory.remove(item)
            print('you have dropped ' + item)

        else:
            print(item + ' is not in your inventory')

def torchcheck(command, inventory, rooms, current_room, dead):
    if 'torch' in inventory:
        print('the torchlight reveals ancient scriptures on the wall:')
        current_room = rooms['cell_room']
        
        return 
    elif 'torch' not in inventory:
        print('are you sure you want to continue without the torch?')
        command = input(':').lower()
        if command in ('yes', 'y'):
            print('you trip in the dark and die')
            
            dead = True
            return dead
        elif command in ('no', 'n'):
            print('wise decision')
            current_room = rooms['corridor']
            
            return 

def takescript(command, inventory, rooms, current_room):
    if len(command) - len(command.split()[0]) >= 1:
        item = command.lower().split()[1]
        if item in ('bale', 'hay', 'chest', 'throne', 'door'):
            print('the ' + item + ' is too heavy')
            
            return 
        elif item in current_room['contents']:
            current_room['contents'].remove(item)
            inventory.append(item)
            print(item + ' is now in your inventory')
            
            return 
        else:
            print(item + ' is not in the room')
            
            return 
    elif len(command) - len(command.split()[0]) < 1:
        print("i don't know what you want me to " + command.split()[0])
        
        return 

def dropscript(command, inventory, rooms, current_room):
    if command.lower().split()[0] == 'drop':
        if len(command) - len(command.split()[0]) >= 1:
            item = command.lower().split()[1]
            if item in inventory:
                current_room['contents'].append(item)
                inventory.remove(item)
                print(' you have dropped ' + item)
                 
            else:
                print(item + ' is not in your inventory')
                
        else:
            print("i don't know what you want me to drop")
            

def readcript(command, current_room):
    if current_room['name'] == 'graveyard':
        try: 
            if command.split()[1] == 'gravestones':
                print('On the first is: Elliot Barnster, died at 23 after being hit by a bus.')
                time.sleep(1)
                print('On the second is: Jane Watson, died at 51.') 
                time.sleep(1)
                print('On the third is: Harry McSquire, died at 87. He will be missed.')
                
            if command.split()[1] == 'note':
                print('The note reads: 2 of us died in our prime, one of us did not.')
                time.sleep(1)
                print('Guess the grave I lie in, and you can have the lot.')
                
        except:
            print('that was not clear enough')
            

def digscript(command, current_room, inventory, dead, gravedug):
    if current_room['name'] == 'graveyard' and gravedug == False:
        if 'shovel' in inventory:
            if '2' in command:
                time.sleep(1)
                print('you chose wisely')
                print('now use my number open your treasure')
                time.sleep(1)
                inventory.append('a rock')
                print('at the bottom of the grave is a rock.')
                
                gravedug = True
                return gravedug
            elif '1' in command or '3' in command:
                print('you chose unwisely.')
                time.sleep(1)
                print('hahaha')
                dead = True
                return dead
            else:
                print('which one?')
                command = input(':').lower()
                if '2' in command:
                    time.sleep(1)
                    print('you chose wisely')
                    print('now use my number open your treasure')
                    time.sleep(1)
                    inventory.append('a rock')
                    print('at the bottom of the grave is a rock.')
                    
                    gravedug = True
                    return gravedug
                elif '1' in command or '3' in command:
                    print('you chose unwisely.')
                    time.sleep(1)
                    print('hahaha')
                    dead  = True
        else:
            print('you would need a shovel to do that')
            
            return 
    else:
        print('it would be stupid to dig here')
        
        return 








