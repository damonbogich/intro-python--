from room import Room
from player import Player
from item import Item
#steps:
    #Create Room and player classes in their files... done for now
    #figure out how to get the rooms in the room dictionary to be instances of Room class... added through dictionary
    #Look into creating a repl command parser in this files to allow players to move in the four directions
        #n, s, e, w keys should call the corresponding functions
        #Do i need to import players into this file and add instances of it?
    #Figure out how the move in a direction will cause the player to end up in correct room

# Declare all the rooms
#I think this is a dictionary called room where the key is the string and the value is an instance of room class
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('Rock', 'Big big rock'), Item('Another rock', 'even bigger rock')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Grand Piano', 'A big musical instrument'), Item('Air Jordans', 'Shoes that are light sleek and expensive')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#try to add a room to room class
# print(room['outside'])


# Link rooms together
#I think these are functions being added on to each room 
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

damon = Player('Damon', room['outside'], [Item('Sword', 'This sword cuts through butter like steel')])
# damon.get_item()
def game(player= damon):
    #make this in loop format:
    while(True):
        #print current room name
        # print((f'{player.current_room.name.s_to}')) --experiment with putting these in the class person later
        # print (f'Player items: {player.items[0].name}')
        
        print((f'{player.current_room.name}'))
        #current room desc
        print(f'{player.current_room.description}')
        #print items in the room:
        player.list_items()
        player.current_room.list_items()
        player.get_item()
        player.list_items()
        player.drop_item()
        player.current_room.list_items()
        #waits for user input and decides what direction to move
        direction = input('Which way would you like to move?(n,e,s,w): ')
        print(f'current room:{player.current_room.name}, current direction: {direction} ')
        #set conditionals allowing player to move from room to room
        if direction == 'q':
            break
        elif player.current_room.name == 'Outside Cave Entrance'  and direction == 'n' :
            player.current_room = player.current_room.n_to
        elif player.current_room.name == 'Outside Cave Entrance' and direction == 'e':
            print('can not move east from here')
        elif player.current_room.name == 'Outside Cave Entrance' and direction == 'w':
            print('can not move west from here')
        elif player.current_room.name == 'Outside Cave Entrance' and direction == 's':
            print('can not move south from here')
        elif player.current_room.name == 'Foyer' and direction == 'n':  
            player.current_room = player.current_room.n_to
        elif player.current_room.name == 'Foyer' and direction == 's':
            player.current_room = player.current_room.s_to
        elif player.current_room.name == 'Foyer' and direction == 'e':
            player.current_room = player.current_room.e_to
        elif player.current_room.name == 'Foyer' and direction == 'w':
            print('you cannot move west from here')
        elif player.current_room.name == 'Grand Overlook' and direction == 's':
            player.current_room = player.current_room.s_to
        elif player.current_room.name == 'Grand Overlook' and direction == 'n':
            print('you cannot move north from here')
        elif player.current_room.name == 'Grand Overlook' and direction == 'e':
            print('you cannot move east from here')
        elif player.current_room.name == 'Grand Overlook' and direction == 'w':
            print('you cannot move west from here')
        elif player.current_room.name == 'Narrow Passage' and direction == 'n':  
            player.current_room = player.current_room.n_to
        elif player.current_room.name == 'Narrow Passage' and direction == 'w':  
            player.current_room = player.current_room.w_to
        elif player.current_room.name == 'Narrow Passage' and direction == 'e':  
            print('you cannot move east from here')
        elif player.current_room.name == 'Narrow Passage' and direction == 's':  
            print('you cannot move south from here')
        elif player.current_room.name == 'Treasure Chamber' and direction == 's':  
            player.current_room = player.current_room.s_to
        elif player.current_room.name == 'Treasure Chamber' and direction == 'n':  
            print('you cannot move north from here')
        elif player.current_room.name == 'Treasure Chamber' and direction == 'e':  
            print('you cannot move east from here')
        elif player.current_room.name == 'Treasure Chamber' and direction == 'w':  
            print('you cannot move west from here')
        
        
        
        
        
game()

# player can move in 4 cardinal directions
# game flow : You're a player who starts in a room, 
# you can move from the room you're in to another 


# damon = Player('Damon', room['outside'])

# def game(player=damon):
#     #looop
#     while(True):
#     #prints out current room name
        
#         print(f'{player.current_room.name}')
#     #current room description
#         print(f'{player.current_room.description} ')
#     #waits for user input and decides what to do
#         direction = input('Which way would you like to move?: ')
#         print(f'current room:{player.current_room.name}, current direction: {direction} ')
#         #set up conditionals for each room/direction for user
#         #outisde(north), foyer(north, south, east), overlook(south), narrow(north, west), treasure(south)
#         if direction == 'q':
#             break
#         if player.current_room.name == 'Outside Cave Entrance'  and direction == 'n':
#             print('ran cave north function!')
#             player.current_room = player.current_room.n_to
#         elif player.current_room.name == 'Outside Cave Entrance' and direction == 'e' or  direction == 'w' or direction == 's':
#             print('you must move north from here' )
#         elif player.current_room.name == 'Foyer' and direction == 'n':  
#             player.current_room = player.current_room.n_to
#         elif player.current_room.name == 'Foyer' and direction == 's':
#             player.current_room = player.current_room.s_to
#         elif player.current_room.name == 'Foyer' and direction == 'e':
#             player.current_room = player.current_room.e_to
#         elif player.current_room.name == 'Foyer' and direction == 'w':
#             print('you cannot move west from here')

        #set up foyer now:
        #if player.current_room.name == 'Foyer' and direction == 'n'.... add room foyer to line 105
            # player.current_room == player.current_room.n_to xxxx

        #if player.current_room.name == 'Foyer' and direction == 's'...
            # player.current_room == player.current_room.s_to
        #if player.current_room.name == 'Foyer' and direction == 'e'...
            # player.current_room == player.current_room.e_to
        #if player.current_room.name == 'Foyer' and direction == 'w'...
        #     print('you cannot move west from here')   

        #foyer problems: south function returns line 111, direction set to w returns line 111
        #tried the following as: if player.current_room.name == 'Outside Cave Entrance' or player.current_room.name == 'Foyer' and it did not work... why???

