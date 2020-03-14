import time
from random import randint



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

def usescript(command, inventory, rock_broken):
    if 'rock_tumbler' in command:
        if 'rock_tumbler' and 'a rock' in inventory and rock_broken == False:
            print('you place the rock in your rock rumbler')
            time.sleep(2)
            print('opening the tumbler, you find an old, rusty key')
            inventory.remove('a rock')
            inventory.append('key')
            rock_broken = True
            return rock_broken 
        elif 'rock' not in inventory:
            print('you cannot use the rock tumbler with a rock')
        elif rock_broken == True:
            print('unfortunatley, the rock tumbler broke when you used it')
    else:
        print('you cannot use anything here')

def openscript(command, inventory, current_room, rounddone, user_input):
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
                return opened and rounddone
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

def insertcript(command, inventory, current_room, Enemy):
    if current_room['name'] == 'opening' and 'circular_jewel' in command:
        if 'circular_jewel' in inventory:
            print('you insert the jewel into the hilt of the sword.')
            print('the stone surrounding the sword breaks apart, revealing a long, silver broadsword')
            inventory.append('silver_broadsword')
            current_room['text'] = 'another opening, but with segments of stone scattered around.'
            serpent = Enemy('serpent', 1)
            current_room['enemy'] = serpent
        elif 'circular_jewel' not in inventory:
            print('you cannot place what do you do not have')
    else:
        print('no')

def combatscript(command, inventory, current_room, dead):
    from Salute_Mundi import Enemy
    current_enemy = current_room['enemy']
    print('a ' + current_enemy + ' approaches you')
    enemyat = randint(1, 7)
    playerat = randint(1, 10)
    if 'silver_broadsword' in inventory:
        playerat += 3
    if current_enemy[damage] + enemyat > playerat:
        print('your encounter with the beast has lead to your death.')
        dead = True
    elif current_enemy[damage] + enemyat <= playerat:
        print('you kill the beast')
        

