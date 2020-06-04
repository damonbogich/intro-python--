from room import Room
from player import Player
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
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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


# def play_game(playerobj = damon):
#     #make this in loop format:
#     print(f'{playerobj.name} is in a room {playerobj.current_room}, which is {playerobj.current_room.description}')
#     #direction prompt
#     direction = input(f"enter direction you would like {playerobj.name} to move:")
#     #if direction = 'n' run playerobj.current_room.n_to function
#     if direction == 'n':
#         print(playerobj.current_room.n_to) 


# play_game()
#new player: 
damon = Player('Damon', room['outside'])
# print(damon)

# while (true):

# player can move in 4 cardinal directions
# game flow : You're a player who starts in a room, 
# you can move from the room you're in to another 

#function for game:
def game(player=damon):
    #looop
    while(True):
    #prints out current room name
        
        print(f'{player.current_room.name}')
    #current room description
        print(f'{player.current_room.description} ')
    #waits for user input and decides what to do
        direction = input('Which way would you like to move?: ')
        print(f'current room:{player.current_room.name}, current direction: {direction} ')
        #set up conditionals for each room/direction for user
        #outisde(north), foyer(north, south, east), overlook(south), narrow(north, west), treasure(south)
        if direction == 'q':
            break
        #this elif prints every time anything other than q is set to direction
        # elif direction != 'q' or direction != 'n' or direction != 'e' or direction != 'w' or direction != 's':
        #     print('not a valid direction for this game')  

        #tried the following as: if player.current_room.name == 'Outside Cave Entrance' or player.current_room.name == 'Foyer' and it did not work... why???
        if player.current_room.name == 'Outside Cave Entrance'  and direction == 'n':
            print('ran cave north function!')
            player.current_room = player.current_room.n_to
        elif player.current_room.name == 'Foyer' and direction == 'n':  
            player.current_room = player.current_room.n_to
        elif player.current_room.name == 'Foyer' and direction == 's':
            player.current_room = player.current_room.s_to
        elif player.current_room.name == 'Foyer' and direction == 'e':
            player.current_room = player.current_room.e_to
        elif player.current_room.name == 'Outside Cave Entrance' and direction == 'e' or  direction == 'w' or direction == 's':
            print('you must move north from here' )
        elif player.current_room.name == 'Foyer' and direction == 'w':
            print('you cannot move west from here')
        #set up foyer now:
        #if player.current_room.name == 'Foyer' and direction == 'n'.... add room foyer to line 105
            # player.current_room == player.current_room.n_to xxxx

        #if player.current_room.name == 'Foyer' and direction == 's'...
            # player.current_room == player.current_room.s_to
        #if player.current_room.name == 'Foyer' and direction == 'e'...
            # player.current_room == player.current_room.e_to
        #if player.current_room.name == 'Foyer' and direction == 'w'...
        #     print('you cannot move west from here')   

        #foyer problems: whenever I set direction to w it prints 'you must move north from here'... should say 'cannot move west'
        #No matter what I type when I'm in 'outside cave entrance' it sends me to foyer.  SHould only send me to foyer if i type 'n'
game()
