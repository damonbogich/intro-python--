# Write a class to hold player information, e.g. what room they are in
# currently.
#player will have name, what room they're in, items they have, methods to move north, south, east, west, and method to pickup items

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def __str__(self): 
        return f"This is {self.name}, they are located in {self.current_room}"
    #add functions to move in each direction:
    def north(self):
        #what would the result of this function even be? string saying player moved north
        print(f"{self.name} moved north out of {self.current_room}")
    def east(self):
        print(f"{self.name} moved east out of {self.current_room}")
    def west(self):
        print(f"{self.name} moved west out of {self.current_room}")
    def south(self):
        print(f"{self.name} moved south out of {self.current_room}")


