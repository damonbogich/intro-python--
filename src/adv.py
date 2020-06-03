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
print(room['outside'])


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
damon = Player('Damon', room['outside'])
print(damon)
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

#def game(playerobj):
    #will need user to set the argument in function... look at how you did calendar
    #prints the current room player is in
    #prints description of room player is in
    #prompt user to enter a direction(n,e,s,w)
        #if direction is valid attempt to move player to correct room
        #elif user enters q quit the game
        #else print error message
def play_game(playerobj = damon):
    #make this in loop format:
    print(f'{playerobj.name} is in a room {playerobj.current_room}, which is {playerobj.current_room.description}')
    #direction prompt
    direction = input(f"enter direction you would like {playerobj.name} to move:")
    #if direction = 'n' run playerobj.current_room.n_to function
    if direction == 'n':
        print(playerobj.current_room.n_to) 


play_game()

